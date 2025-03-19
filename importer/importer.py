import logging
from datetime import datetime

from importer.import_validation import validate_import_prices_date
from services.category_service import get_categories
from services.price_service import upload_prices
from services.product_service import update_product_list

logging.basicConfig(level=logging.INFO)

def import_prices():

    logging.info(f"Running scheduled import prices at {datetime.now()}")

    try:
        if not validate_import_prices_date():
            logging.info(f"Price for {datetime.date.today()} already exists. Skipping insertion.")

        categories = get_categories()
        upload_prices(categories)

        logging.info(f"Scheduled import prices done at {datetime.now()}")

    except Exception as e:
        logging.error(f"Error importing prices: {e}", exc_info=True)

def import_products():
    logging.info(f"Running scheduled import products at {datetime.now()}")

    try:
        categories = get_categories()
        update_product_list(categories)

    except Exception as e:
        logging.error(f"Error importing products: {e}")
