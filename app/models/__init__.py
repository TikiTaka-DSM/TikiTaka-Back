from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config.db import LocalDBConfig

Base = declarative_base()

db_engine = create_engine(LocalDBConfig.DB_URL, echo=False)
Session = scoped_session(sessionmaker(bind=db_engine, autocommit=False, autoflush=False))
session = Session()
