import requests

from dao import price_dao
from dao.price_dao import instertProductPrices
from static_strings import GET_BY_LAST_CATEGORY, HEADERS


def upload_prices(categories):
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

            product_price_info = {
                "id": item["id"],
                "name": item["name"],
                "price": item["price"],
                "discountedPrice": item["discountedPrice"],
                "categoryName": item["categoryName"]
            }

            products_to_save.append(product_price_info)
            all_products.append(product_price_info)

        instertProductPrices(products_to_save)

    # print(all_products.__len__())

def get_prices_by_product_id(product_id):
    return price_dao.get_prices_by_product_id(product_id)