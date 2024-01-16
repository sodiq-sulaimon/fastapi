# from typing import List
# Playing around with python type hints
def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return (full_name)

name = get_full_name("Sodiq", "Sulaimon")
print(name)

def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + str(age)
    return name_with_age

print(get_name_with_age("Jane", 30))

# Type hints for generic types and there internal types

# Lists
def process_items(items: list[int]): 
    for item in items:
        print(item)


# Dict
def process_dict(prices: dict[str, int]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)

# Possibly None
from typing import Optional
def say_hi(name: Optional[str] = None): # None is the default value
    if name is not None:
        print(f"Hi, {name}!")
    else:
        print("Hello, World!")

say_hi()
say_hi("Bridget")
