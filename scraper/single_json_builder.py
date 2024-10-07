import json
import os

# 40309870 sample id40309870

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'products.json') 

with open(file_path, "r") as file:
  data = json.load(file)

predicates = [
  "min_temp",
  "max_temp",
]

json_objects = []

def get_product_name_from_id(id):
  for item in data:
    if item['id'] == id:
      return item['name']
  
  return None

def condition_to_string(condition):
    if condition['type'] == 'predicate':
        return f"[{condition['name']}: {condition['value']}]"
    elif condition['type'] in ('and', 'or'):
        left_str = condition_to_string(condition['left'])
        right_str = condition_to_string(condition['right'])
        return f"{condition['type']}({left_str}, {right_str})"
    else:
        return "Unknown"

def build_condition():
  print("\nNew condition type:")
  print("[P]redicate")
  print("[A]nd")
  print("[O]r")

  condition_type = input().strip().upper()

  if condition_type == 'P':
    # predicate node
    print("\nChoose a predicate:")
    for index, predicate in enumerate(predicates):
      print(f"{index +1}: {predicate}")

    predicate_index = int(input()) -1
    if predicate_index < 0 or predicate_index >= len(predicates):
      print("invalid predicate, try again")
      build_condition()
  
    name = predicates[predicate_index]
    value = input("Choose a value for your predicate: ")
    
    predicate = {
      "type": "predicate",
      "name": name,
      "value": value
    }

    print("\nCurrent condition tree:")
    print(condition_to_string(predicate))

    return predicate
  
  elif condition_type in ('A', 'O'):
    operator = "and" if condition_type == 'A' else "or"
    left_condition = build_condition()
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

def build_json(id, name, tree):
  return {
    "id": id,
    "name": name, 
    "conditions": tree,
  }

def edit_product():
  product_name = False
  while not product_name:
    print("\nChoose a product to edit")
    print("Enter a product id: ", end='')
    product_id = input()
    product_name = get_product_name_from_id(product_id)
    if not product_name: print("Invalid try again")
  
  print(f"Selected product: {product_name}")
  
  print("[N]ew condition")
  print("[E]dit condition")
  condition_choice = input().strip().upper()
  
  if condition_choice == 'N': tree = build_condition() 
  else: print("runka balle")

  json_objects.append(build_json(product_id, product_name, tree))

# mega gaaay
if __name__ == "__main__":
  running = True

  while running: 
    edit_product()

    terminate = input("Another product? (Y/N) ")
    file_path = os.path.join(script_dir, "annotated.json")
    with open(file_path, "w", encoding="utf-8") as file: 
      for obj in json_objects:
        json.dump(obj, file, indent=4)

    running = False if terminate == "N" or terminate == "n" else True
