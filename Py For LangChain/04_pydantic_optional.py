#topic 3 - pydantic model with optional field
from pydantic import BaseModel
from typing import Optional

class student_with_optional(BaseModel):
    name: str
    age: Optional[int] = None

new_student_with_optional = {'name' : 'rahat'}

student_with_optional_obj = student_with_optional(**new_student_with_optional)

print(student_with_optional_obj.name)  # Output: "rahat"
print(student_with_optional_obj.age)   # Output: None   
