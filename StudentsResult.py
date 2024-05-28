from pydantic import BaseModel

# 2. Class which describes Student Cgpa and Iq

class StudentResult(BaseModel):
    cgpa: float
    iq: float