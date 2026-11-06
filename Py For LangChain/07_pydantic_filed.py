#Topic 6 - pydantic field functions
from pydantic import BaseModel, Field

class student_with_field_functions(BaseModel):
    cgpa: float = field(gt=0, lt=4, defalut=3.0, description="CGPA must be between 0 and 4")