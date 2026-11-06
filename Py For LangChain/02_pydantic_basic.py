from pydantic import BaseModel


#topic 1 - basic example of pydantic model
class student(BaseModel):
    name: str
    

new_student = {'name' : 'rahat'}

student_obj = student(**new_student) 

print(type(student_obj.name)) 


new_student_2 = {'name' : 23}

# student_obj_2 = student(**new_student_2)  # This will raise a validation error



