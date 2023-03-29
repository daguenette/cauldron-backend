from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from app.config import engine

Base = declarative_base()

class Declaration(Base):
    __tablename__ = "declarations"

    id = Column(Integer, primary_key=True)
    user = Column(String)
    year = Column(Integer)
    salary_income = Column(Integer)
    salary_hours = Column(Integer)

Base.metadata.create_all(engine)


