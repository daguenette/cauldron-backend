"""
Description: The file containing Pydantic schemas for taxes resource.
"""

## -- 3rd Party Imports -- ##

from pydantic import BaseModel

## -- Pydantic Schema For Taxes Resource -- ##

class Taxes(BaseModel):
    email: str
    name: str
    year: int
    salary_income: int
    salary_hours: int