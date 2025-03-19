from fastapi import APIRouter

from importer.importer import import_prices
from services.price_service import get_prices_by_product_id


router = APIRouter(prefix="/prices", tags=["Prices"])

@router.get("/product/{product_id}")
async def hello(product_id: int):
    return get_prices_by_product_id(product_id)

@router.post("/import")
async def import_prices_from_site():
    import_prices()

