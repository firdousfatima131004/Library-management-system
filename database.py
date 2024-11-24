from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import base

DATABASE_URL = "sqlite:///Library.db"
engine = create_engine(DATABASE_URL)
base.metadata.create_all(engine)

session = sessionmaker(bind = engine)
session = session()