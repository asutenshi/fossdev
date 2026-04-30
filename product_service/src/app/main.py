from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Product Service")


class Product(BaseModel):
    id: str
    name: str
    price: float
    available: bool


PRODUCTS: dict[str, Product] = {
    "pencil": Product(
        id="pencil",
        name="Pencil",
        price=1.50,
        available=True,
    ),
    "notebook": Product(
        id="notebook",
        name="Notebook",
        price=4.20,
        available=True,
    ),
    "backpack": Product(
        id="backpack",
        name="Backpack",
        price=35.00,
        available=False,
    ),
}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "product-service"}


@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: str) -> Product:
    product = PRODUCTS.get(product_id)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail=f"Product '{product_id}' was not found",
        )

    return product
