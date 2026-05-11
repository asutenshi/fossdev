import os

import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional


app = FastAPI(title="Order Service")


PRODUCT_SERVICE_IP = os.getenv("PRODUCT_SERVICE_IP", "http://127.0.0.1")
PRODUCT_SERVICE_PORT = os.getenv("PRODUCT_SERVICE_PORT", "8001")

PRODUCT_SERVICE_URL = PRODUCT_SERVICE_IP + ":" + PRODUCT_SERVICE_PORT

DISCOUNT_SERVICE_IP = os.getenv("DISCOUNT_SERVICE_IP", "http://127.0.0.1")
DISCOUNT_SERVICE_PORT = os.getenv("DISCOUNT_SERVICE_PORT", "8003")

DISCOUNT_SERVICE_URL = DISCOUNT_SERVICE_IP + ":" + DISCOUNT_SERVICE_PORT


class OrderRequest(BaseModel):
    product_id: str
    quantity: int = Field(gt=0)
    promo_code: Optional[str] = None


class OrderResponse(BaseModel):
    product_id: str
    quantity: int
    unit_price: float
    total_before_discount: float
    discount_percent: float
    discount_amount: float
    total_after_discount: float
    discount_reason: str


class ProductFromService(BaseModel):
    id: str
    name: str
    price: float
    available: bool


class DiscountFromService(BaseModel):
    discount_percent: float
    reason: str


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "order-service"}


@app.post("/orders", response_model=OrderResponse)
async def create_order(order: OrderRequest) -> OrderResponse:
    product = await fetch_product(order.product_id)

    if not product.available:
        raise HTTPException(
            status_code=400,
            detail=f"Product '{order.product_id}' is not available",
        )

    discount_data = await fetch_discount(
        product_id=product.id,
        quantity=order.quantity,
        price=product.price,
        promo=order.promo_code,
    )

    total_before = product.price * order.quantity
    discount_amount = total_before * (discount_data.discount_percent / 100)
    total_after = total_before - discount_amount

    return OrderResponse(
        product_id=product.id,
        quantity=order.quantity,
        unit_price=product.price,
        total_before_discount=round(total_before, 2),
        discount_percent=discount_data.discount_percent,
        discount_amount=round(discount_amount, 2),
        total_after_discount=round(total_after, 2),
        discount_reason=discount_data.reason,
    )


async def fetch_discount(
    product_id: str, quantity: int, price: float, promo: Optional[str]
) -> DiscountFromService:
    url = f"{DISCOUNT_SERVICE_URL}/discounts/calculate"
    payload = {
        "product_id": product_id,
        "quantity": quantity,
        "unit_price": price,
        "promo_code": promo,
    }
    try:
        async with httpx.AsyncClient(timeout=3.0) as client:
            response = await client.post(url, json=payload)
    except httpx.RequestError as exc:
        raise HTTPException(
            status_code=503, detail=f"Discount service is unavailable: {exc}"
        )

    if response.status_code >= 400:
        raise HTTPException(
            status_code=502, detail="Discount service returned an error"
        )

    return DiscountFromService.model_validate(response.json())


async def fetch_product(product_id: str) -> ProductFromService:
    url = f"{PRODUCT_SERVICE_URL}/products/{product_id}"

    try:
        async with httpx.AsyncClient(timeout=3.0) as client:
            response = await client.get(url)

    except httpx.RequestError as exc:
        raise HTTPException(
            status_code=503,
            detail=f"Product service is unavailable: {exc}",
        ) from exc

    if response.status_code == 404:
        raise HTTPException(
            status_code=404,
            detail=f"Product '{product_id}' was not found",
        )

    if response.status_code >= 400:
        raise HTTPException(
            status_code=502,
            detail="Product service returned an unexpected error",
        )

    return ProductFromService.model_validate(response.json())
