from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL


# @TODO include inside config file
url = URL.create(
    drivername="postgresql",
    username="hcwhkcgn",
    password="kXwauflXJABKwvdOXe96TjFhIMmcWfip",
    host="raja.db.elephantsql.com",
    database="hcwhkcgn",
    port=5432
)

engine = create_engine(url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()