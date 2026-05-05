# order_service/app/settings.py
import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    product_service_url: str
    database_url: str


def get_settings() -> Settings:
    return Settings(
        product_service_url=os.getenv(
            "PRODUCT_SERVICE_URL",
            "http://127.0.0.1:8001",
        ),
        database_url=os.getenv(
            "DATABASE_URL",
            "postgresql://app:app@127.0.0.1:5432/orders",
        ),
    )