"""
Description: The file containing the crud operations for the taxes resource.
"""

## -- 3rd Party Imports -- ##

from sqlalchemy.orm import Session
import typing as t

## -- Project Imports -- ##

from . import models, schemas

## -- Crud Operations -- ##

# Get all entries of taxes declarations
def get_all_taxes(db: Session, skip: int = 0, limit: int = 100) -> t.List[schemas.Taxes]:
    
    return db.query(models.Taxes).offset(skip).limit(limit).all()

# Create a new entry of taxes declarations
def create_taxes(db: Session, taxes: schemas.Taxes):

    db_taxes= models.Taxes(
        email=taxes.email,
        name = taxes.name,
        year = taxes.year,
        salary_income = taxes.salary_income,
        salary_hours = taxes.salary_hours
    )

    db.add(db_taxes)
    db.commit()
    db.refresh(db_taxes)

    return db_taxes