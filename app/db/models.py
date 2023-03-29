from sqlalchemy import Column, Integer, String, Boolean
from .session import Base
from app.db.session import engine

class Declaration(Base):
    __tablename__ = "declaration"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    year = Column(Integer)
    salary_income = Column(Integer)
    salary_hours = Column(Integer)

Base.metadata.create_all(engine)