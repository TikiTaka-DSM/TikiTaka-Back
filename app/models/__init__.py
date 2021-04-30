import boto3
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config.db import RemoteDBConfig

db_engine = create_engine(RemoteDBConfig.DB_URL, encoding="utf-8", pool_size=20,
                          pool_recycle=3600, max_overflow=20, pool_pre_ping=True)

Session = scoped_session(sessionmaker(bind=db_engine, autocommit=False, autoflush=False))
Base = declarative_base()
session = Session()

s3 = boto3.client(service_name='s3',
                  aws_access_key_id=RemoteDBConfig.S3_ACCESS_KEY,
                  aws_secret_access_key=RemoteDBConfig.S3_SECRET_ACCESS,
                  region_name=RemoteDBConfig.S3_REGION)

