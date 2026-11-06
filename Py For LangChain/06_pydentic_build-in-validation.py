#topic 5 - email validation using pydantic (built-in validation)
from pydantic import BaseModel, EmailStr

class student_with_email_validation(BaseModel):
    name: str
    email: EmailStr     

new_student_with_email_validation = {'name' : 'rahat', 'email' : 'rahat@example.com'}

student_with_email_validation_obj = student_with_email_validation(**new_student_with_email_validation)