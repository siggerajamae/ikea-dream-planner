import json

products_file = open("products.json", "r", encoding="utf8")
products_json = json.load(products_file)

annotated_file = open("annotated.json", "r", encoding="utf8")
annotated_json = json.load(annotated_file)

product_ids = set()
for product in products_json:
    product_ids.add(product["id"])

for entry in annotated_json:
    if entry["id"] not in product_ids:
        print(f"unrecognized id: {entry["id"]}")
