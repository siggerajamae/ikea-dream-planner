import json
import requests


# Localization
LOCALE = "se/en"

# All categories
CATEGORIES_URL = f"https://www.ikea.com/{LOCALE}/meta-data/navigation/catalog-products-slim.json"

# Url used by IKEA for listing products by category
SEARCH_URL = f"https://sik.search.blue.cdtapps.com/{LOCALE}/search"


def search_products(category_id):
    # The structure of the body of a search request
    request_body = {
        "searchParameters": {
            # Category id
            "input": category_id,
            "type": "CATEGORY"
        },
        "isUserLoggedIn": False,
        "optimizely": {
            "listing_2911_fastly_latency_test": None
        },
        "components": [
            {
                "component": "PRIMARY_AREA",
                "columns": 4,
                "types": {
                    "main": "PRODUCT",
                    "breakouts": [
                        # Some products were not included without these
                        # Appears to be the same for most/all categories
                        "PLANNER",
                        "LOGIN_REMINDER",
                        "MATTRESS_WARRANTY"
                    ]
                },
                "filterConfig": {
                    "max-num-filters": 7
                },
                "window": {
                    # Limited to 1000 results per request
                    "size": 1000,
                    "offset": 0
                },
                "forceFilterCalculation": True
            }
        ]
    }

    # Convert to json
    request_body_json = json.dumps(request_body, indent=4)

    # Blocking request
    response = requests.post(SEARCH_URL, request_body_json)
    response_body = response.json()

    # Check status
    if response.status_code != 200:
        raise Exception(f"Error in response:\n{response_body}")

    # Extract the items list
    items = response_body["results"][0]["items"]

    # Filter for products
    items = filter(lambda i: "product" in i, items)

    # Map to products
    products = map(lambda i: i["product"], items)

    # Refine product information
    # Change this to include more product information
    products_refined = map(
        lambda p: {
            "name": p["name"],
            "id": p["id"]
        },
        products
    )

    return products_refined


def get_all_category_ids():
    response = requests.get(CATEGORIES_URL)
    response_body = response.json()

    # Check status
    if response.status_code != 200:
        raise Exception(f"Error in response:\n{response_body}")

    result = []

    # Extract all sub categories
    for cat in response_body:
        # We are only interested in sub categories
        # Assuming each sub category has less than 1000 products, we can then
        # get all of them in a single request
        for sub in cat["subs"]:
            result.append(sub["id"])

    return result


if __name__ == "__main__":
    categories = get_all_category_ids()
    products = []
    for cat_id in categories:
        results = search_products(cat_id)
        products.extend(results)

    # Dump to json
    with open("products.json", "w") as fp:
        json.dump(products, fp, indent=2)
