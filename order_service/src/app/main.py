import os

import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


app = FastAPI(title="Order Service")


PRODUCT_SERVICE_IP = os.getenv("PRODUCT_SERVICE_IP", "http://127.0.0.1")
PRODUCT_SERVICE_PORT = os.getenv("PRODUCT_SERVICE_PORT", "8001")

PRODUCT_SERVICE_URL = PRODUCT_SERVICE_IP + ":" + PRODUCT_SERVICE_PORT


class OrderRequest(BaseModel):
    product_id: str
    quantity: int = Field(gt=0)


class OrderResponse(BaseModel):
    product_id: str
    quantity: int
    unit_price: float
    total: float


class ProductFromService(BaseModel):
    id: str
    name: str
    price: float
    available: bool


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "order-service"}


@app.post("/orders", response_model=OrderResponse)
async def create_order(order: OrderRequest) -> OrderResponse:
    product = await fetch_product(order.product_id)

    if not product.available:
        raise HTTPException(
            status_code=401,
            detail=f"Product '{order.product_id}' is not available",
        )

    total = product.price * order.quantity

    return OrderResponse(
        product_id=product.id,
        quantity=order.quantity,
        unit_price=product.price,
        total=total,
    )


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
