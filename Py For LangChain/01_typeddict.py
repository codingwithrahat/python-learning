from typing import TypedDict

class person(TypedDict):
    name: str
    age: int
    

new_person : person = {
    "name" : "rahat",
    "age" : 23
}


#it will not give any error
another_person : person = {
    "name" : "rakib",
    "age" : "27"
}


#typeddict is a way to define a dictionary with specific key-value types.
#but it has a limitation that it does not enforce type checking at runtime.

print(new_person["age"])  # Output: 23
print(another_person["age"])  # Output: "27" (even though it should be an int)