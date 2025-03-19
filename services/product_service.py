import requests

from dao.import_dao import instert_product
from static_strings import *

def update_product_list(categories):
    # If the API does not require actual data, send empty JSON:

    all_products = []

    for category in categories:

        category_id = category.get('id')
        payload = {"count": 5000, "page": 1, "parentId": category_id}

        response = requests.post(GET_BY_LAST_CATEGORY, json=payload, headers=HEADERS)
        response.raise_for_status()

        data = response.json()
        items = data.get("data", {}).get("list", [])

        products_to_save = []
        for item in items:

            product_id = item.get("id")
            product_name = item.get("name")
            if product_id is None:
                print("Warning: null product id for product " + str(product_name))

            product_info = {
                "id": item["id"],
                "name": item["name"],
                "category_name": item["categoryName"],
                "photo_url": item["photo"]
            }

            products_to_save.append(product_info)

        instert_product(products_to_save)

    # print(all_products.__len__())
