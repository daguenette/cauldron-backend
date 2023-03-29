from pydantic import BaseModel
import typing as t

class DeclarionBase(BaseModel):
    email: str
    name: str
    year: int
    salary_income: int
    salary_hours: int