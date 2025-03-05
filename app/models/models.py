from pydantic import BaseModel

class Person(BaseModel):
    age: int
    height: float
    weight: float
    family_history: int