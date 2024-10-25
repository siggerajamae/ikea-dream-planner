import atexit
import copy
import itertools
import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path_products = os.path.join(script_dir, "products.json")
file_path_annotated = os.path.join(script_dir, "annotated.json")

with open(file_path_products, "r") as file:
    data = json.load(file)

with open(file_path_annotated, "r") as file:
    json_objects = json.load(file)

predicates = [
    "temp",
    "age",
]

predicate_types = ("min", "max", "e", "lt", "gt", "le", "ge")
logic_types = ("and", "or")


def get_product_name_from_id(id):
    for item in data:
        if item["id"] == id:
            return item["name"]

    return None


def write_to_json():
    print("\nProgram stopped, saving JSONS")
    file_path = os.path.join(script_dir, "annotated.json")

    with open(file_path, "w", encoding="utf-8") as file:
        file.write("[\n")
        for index, obj in enumerate(json_objects):
            json.dump(obj, file, indent=4)

            # no comma on last object
            if index != len(json_objects) - 1:
                file.write(",\n")
            else:
                file.write("\n")
        file.write("]")


def condition_to_string(condition):
    # For displaying condition when building it
    # sucks but who cares it's not that useful
    if condition["type"] in logic_types:
        left_str = condition_to_string(condition["left"])
        right_str = condition_to_string(condition["right"])
        return f"{condition['type']}({left_str}, {right_str})"
    elif condition["type"] in predicate_types:
        return f"[{condition['key']}: {condition['value']}]"
    else:
        return "Unknown"


def build_condition():
    # This function builds a condition (tree)
    print("\nNew condition type:")
    print("[Min] value, [Max] value")
    print("[E]qual value")
    print("[LT], [GT], [LE], [GE]")
    print("[A]nd")
    print("[O]r")

    condition_type = input().strip().lower()

    # i.e not a logic gate
    if condition_type in predicate_types:
        print("\nChoose a predicate:")
        for index, predicate in enumerate(predicates):
            print(f"{index +1}: {predicate}")

        predicate_index = int(input()) - 1
        if predicate_index < 0 or predicate_index >= len(predicates):
            print("invalid predicate, try again")
            build_condition()

        key = predicates[predicate_index]

        # maybe force int but idk keys, maybe some keys int some not, maybe?
        value = input(f"Choose a value for {key}: ")

        predicate = {"type": condition_type, "key": key, "value": value}

        print("\nCurrent condition tree:")
        print(condition_to_string(predicate))

        return predicate

    # if logic then build left and right trees for logic gate
    elif condition_type in logic_types:
        operator = condition_type
        print(f"\nBuilding left tree for: {operator}")
        left_condition = build_condition()
        print(f"\nBuilding right tree for: {operator}")
        right_condition = build_condition()

        condition = {
            "type": operator,
            "left": left_condition,
            "right": right_condition,
        }

        print("\nCurrent condition tree:")
        print(condition_to_string(condition))

        return condition

    else:
        print("invalid condition hoe")
        return build_condition()


def edit_condition(product_id):
    # Det här är planen:
    # Get JSON object and print it
    # At each node, print arbitrary index for that node
    # E.g: "type": "AND" <-- INDEX 1
    # User selects index and that node gets deleted
    # User builds a new tree to replace it

    # Adds index numbers to object, and stores the path
    # Path is used to edit node later
    def add_index_to_type(obj, counter, index_to_path, path=[]):
        if isinstance(obj, dict):
            if "type" in obj:
                index = next(counter)
                obj["type"] += f" <--- {index}"
                index_to_path[index] = path.copy()
            for key, value in obj.items():
                add_index_to_type(value, counter, index_to_path, path + [key])
        elif isinstance(obj, list):
            for idx, item in enumerate(obj):
                add_index_to_type(item, counter, index_to_path, path + [idx])

    # ended up not use but maybe later?
    def get_node_by_path(obj, path):
        for key in path:
            obj = obj[key]
        return obj

    def set_node_by_path(obj, path, new_node):
        for key in path[:-1]:
            obj = obj[key]
        obj[path[-1]] = new_node

    # product_obj is the JSON obj to edit
    for obj in json_objects:
        if obj["id"] == product_id:
            product_obj = obj
            break
    else:
        print("Product not found :/")

    # used to print obj with indices
    product_indices = copy.deepcopy(product_obj)
    counter = itertools.count(1)

    index_to_path = {}

    add_index_to_type(product_indices, counter, index_to_path)
    print(json.dumps(product_indices, indent=4))

    node_to_edit = int(input("\nChoose index to replace: "))

    if node_to_edit in index_to_path:
        path_to_node = index_to_path[node_to_edit]

        new_node = build_condition()

        set_node_by_path(product_obj, path_to_node, new_node)

        print("\nUpdated JSON:")
        print(json.dumps(product_obj, indent=4))
        return product_obj
    else:
        print("Index not found wtf yo?? ? ?? NEEEJ")


def build_json(id, tree):
    return {
        "id": id,
        "conditions": tree,
    }


def upsert_json():
    print("\nChoose a product to edit (sample id: 40309870)")
    print("\nSome examples: \n40309870\n60573251\n40571248")
    print("\nEnter a product id: ", end="")
    product_id = input()
    product_name = get_product_name_from_id(product_id)

    # Go on until valid id
    while not product_name:
        if not product_name:
            print("Invalid try again")
        print("\nEnter a product id: ", end="")
        product_id = input()
        product_name = get_product_name_from_id(product_id)

    print(f"Selected product: {product_name}")

    print("[N]ew conditions")
    print("[E]dit condition")
    condition_choice = input().strip().upper()

    while condition_choice not in ("N", "E"):
        print("\n TRY AGAIN PLEASE")
        print("[N]ew conditions")
        print("[E]dit condition")
        condition_choice = input().strip().upper()

    if condition_choice == "N":
        new_obj = build_json(product_id, build_condition())
    elif condition_choice == "E":
        new_obj = edit_condition(product_id)

    # remove old obj
    json_objects[:] = [
        obj for obj in json_objects if obj.get("id") != new_obj.get("id")
    ]
    json_objects.append(new_obj)


# mega gaaay
if __name__ == "__main__":
    atexit.register(write_to_json)
    running = True

    while running:
        upsert_json()

        terminate = input("Another product? (Y/N) ")
        running = False if terminate == "N" or terminate == "n" else True
