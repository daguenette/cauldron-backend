"""
Description: The file containing SQLAlchemy models for taxes resource.
"""

## -- 3rd Party Imports -- ##

from sqlalchemy import Column, Integer, String

## -- Project Imports -- ##

from app.database.base import Base

## -- SQLAlchemy Models For Taxes Resource -- ##

class Taxes(Base):
    __tablename__ = "taxes"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    year = Column(Integer)
    salary_income = Column(Integer)
    salary_hours = Column(Integer)