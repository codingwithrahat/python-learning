#topic 4 - pydantic type concersion
from pydantic import BaseModel

class student_with_type_conversion(BaseModel):
    name: str
    age: int 

new_student_with_type_conversion = {'name' : 'rahat', 'age' : '23'}

student_with_type_conversion_obj = student_with_type_conversion(**new_student_with_type_conversion)

print(student_with_type_conversion_obj.name)  # Output: "rahat"
print(student_with_type_conversion_obj.age)   # Output: 23 (converted from string to int)   

#here we can see that the age field is converted from string to int automatically by pydantic 
#sometimes pydantic can automatically convert types if the input data is compatible with the expected type.
#in this case, the string '23' can be converted to an integer, so pydantic performs the conversion for us.
print(type(student_with_type_conversion_obj.age))  # Output: <class 'int'>