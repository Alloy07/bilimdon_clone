from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase

from app.dependencies import get_db

from typing import Annotated

from fastapi import Depends

from dotenv import load_dotenv
import os

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

class Base(DeclarativeBase):
    pass

SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"



engine = create_engine( 
    SQLALCHEMY_DATABASE_URL 
)


SessionLocal = sessionmaker(bind=engine) 


# Base = declarative_base()




db_dep = Annotated[Session, Depends(get_db)]
