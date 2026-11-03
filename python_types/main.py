def get_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print(get_name("Jane", "Doe"))
# Result is Jane Doe


'''
Add data types
'''
def get_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print(get_name("Jane", "Doe"))
# Result is Jane Doe


'''
Try some more data types
'''
def get_name_with_age(name: str, age: int):
    return name + " is " + age + " years old."

print("Mai", 22)
# Result is Mai 22


'''
typing module
To declare that data can have any type
'''
from typing import Any

def func(data: Any):
    print(data)

func("Jane")
func(21)
func(True)


'''
Generic types: list, tuple, set, dict
'''
# List
def lst(items: list[str]):
    for item in items:
        print(item)

lst(["salt", "pepper", "sugar"])


# Tuple and Set
def items(items_tuple: list[str, int], item_set: set[bytes]):
    print(len(items_tuple))
    print(len(item_set))

items((("Shirt", 1), ("Jeans", 3)), (1,2,3,4,5,6))


# Dict
def items_(prices: dict[str, float]):
    for name, price in prices.items():
        print(name, price)

items_({"Item": "Shirt",
        "Price": 100})


'''
Union
Can be one of these data types
'''
def process_item(item: int | str):
    print(items)


'''
None
You can declare a value could have a type or None
'''
def greeting(name: str | None=None):
    if name is not None:
        print("hello " + name)
    else:
        print("hello world")

greeting("Emma")
greeting()


'''
Classes as type
'''
class Person:
    def __init__(self):
        pass

    def __init__(self, name: str):
        self.name = name

def get_name(person: Person):
    return person.name

person = Person(name="Mai")
print(get_name(person))