import requests
from static_strings import GET_PARENT_CATEGORIES, GET_CHILDREN, HEADERS

def get_categories():

    payload = {}
    response = requests.post(GET_PARENT_CATEGORIES, json=payload, headers=HEADERS)

    # Raise exception for HTTP errors (like 415)
    response.raise_for_status()

    data = response.json()
    categories = data["data"]["categories"]

    category_hierarchy_list = []
    for category in categories:
        category_info = {
            "id": category.get('id'),
            "name": category.get('name'),
            "children": getChildCategories(category.get('id'))
        }

        category_hierarchy_list.append(category_info)

    # json_str = json.dumps(
    #     [dataclasses.asdict(p) for p in categories],
    #     ensure_ascii=False,
    #     indent=2
    # )
    # print(json_str)

    return category_hierarchy_list


def getChildCategories(parent_id):

    payload = {"parentId": parent_id}
    response = requests.post(GET_CHILDREN, json=payload, headers=HEADERS)
    response.raise_for_status()  # Raise HTTPError if the status code is 4xx/5xx

    data = response.json()
    children_data = data["data"]["children"]

    return children_data

