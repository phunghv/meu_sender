from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///testdb.sqlite', echo=False)
Base = declarative_base()