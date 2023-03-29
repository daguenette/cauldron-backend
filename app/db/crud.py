from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import typing as t

from . import models, schemas

def get_declarations(db: Session, skip: int = 0, limit: int = 100) -> t.List[schemas.DeclarionBase]:
    
    return db.query(models.Declaration).offset(skip).limit(limit).all()

def create_declaration(db: Session, declaration: schemas.DeclarionBase):

    db_declarations = models.Declaration(
        email=declaration.email,
        name = declaration.name,
        year = declaration.year,
        salary_income = declaration.salary_income,
        salary_hours = declaration.salary_hours
    )

    db.add(db_declarations)
    db.commit()
    db.refresh(db_declarations)

    return db_declarations