from pydantic import BaseModel



#topic 1 - basic example of pydantic model
class student(BaseModel):
    name: str
    

new_student = {'name' : 'rahat'}

student_obj = student(**new_student) 

print(type(student_obj.name)) 


new_student_2 = {'name' : 23}

# student_obj_2 = student(**new_student_2)  # This will raise a validation error




#topic 2 - default value of pydantic model field
class student_with_default(BaseModel):
    name: str = "rahat"
    age: int = 18

new_student_with_default = {}

student_with_default_obj = student_with_default(**new_student_with_default)

print(student_with_default_obj.name)  # Output: "rahat"
print(student_with_default_obj.age)   # Output: 18  




#topic 3 - pydantic model with optional field
from typing import Optional

class student_with_optional(BaseModel):
    name: str
    age: Optional[int] = None

new_student_with_optional = {'name' : 'rahat'}

student_with_optional_obj = student_with_optional(**new_student_with_optional)

print(student_with_optional_obj.name)  # Output: "rahat"
print(student_with_optional_obj.age)   # Output: None   