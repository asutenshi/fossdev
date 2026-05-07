from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI(title='Discount Service')

class DiscountRequest(BaseModel):
    product_id: str
    quantity: int = Field(gt=0)
    unit_price: float = Field(gt=0)
    promo_code: Optional[str] = None

class DiscountResponse(BaseModel):
    discount_percent: float
    reason: str

@app.post('/discounts/calculate', response_model=DiscountResponse)
def calculate_discount(request: DiscountRequest):
    percent = 0.0
    reason = 'No discount applied'

    if request.promo_code == "STUDENT10":
        percent = 10.0
        reason = "Student promo code"
    
    elif request.quantity >= 10:
        percent = 15.0
        reason = "Bulk order discount"

    return DiscountResponse(discount_percent=percent, reason=reason)
