from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config.db import RemoteDBConfig

db_engine = create_engine(RemoteDBConfig.DB_URL, encoding="utf-8", pool_size=20,
                          pool_recycle=3600, max_overflow=20, pool_pre_ping=True)

Base = declarative_base()
Session = scoped_session(sessionmaker(bind=db_engine, autocommit=False, autoflush=False))
session = Session()
