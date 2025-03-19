from fastapi import APIRouter
from importer.importer import import_products

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/import")
async def import_prices_from_site():
    import_products()

@router.get("/{product_id}")
async def hello(product_id: int):
    return get_prices_by_product_id(product_id)
