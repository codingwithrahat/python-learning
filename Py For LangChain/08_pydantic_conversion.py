#Topic 7 - convert to dictionary and json

from pydantic import BaseModel


class student_with_dict_json(BaseModel):
    name: str
    age: int    

student_with_dict_json_obj = student_with_dict_json(name="rahat", age=23)

print(student_with_dict_json_obj.name)  # Output: "rahat"

stu_dict = student_with_dict_json_obj.model_dump()  # Convert to dictionary
print(stu_dict['name'])  

stu_json = student_with_dict_json_obj.model_dump_json()  # Convert to JSON
print(stu_json)  

