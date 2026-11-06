#topic 2 - default value of pydantic model field
from pydantic import BaseModel

class student_with_default(BaseModel):
    name: str = "rahat"
    age: int = 18

new_student_with_default = {}

student_with_default_obj = student_with_default(**new_student_with_default)

print(student_with_default_obj.name)  # Output: "rahat"
print(student_with_default_obj.age)   # Output: 18  