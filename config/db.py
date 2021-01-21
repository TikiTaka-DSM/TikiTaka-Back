from config.config import (
    DB_NAME,
    DB_USER,
    DB_HOST,
    DB_PORT,
    DB_PASSWORD,
    S3_REGION,
    S3_ACCESS_KEY,
    S3_SECRET_ACCESS,
    S3_BUCKET_NAME
)


class LocalDBConfig:
    DB_URL = f'mysql+pymysql://root:heunyam@localhost:3306/tikitaka?charset=utf8mb4'


class RemoteDBConfig:
    S3_ACCESS_KEY = S3_ACCESS_KEY
    S3_SECRET_ACCESS = S3_SECRET_ACCESS
    S3_REGION = S3_REGION
    S3_BUCKET_NAME = S3_BUCKET_NAME
    DB_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4"
