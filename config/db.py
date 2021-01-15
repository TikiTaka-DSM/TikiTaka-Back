from config.config import DB_NAME, DB_USER, DB_HOST, DB_PORT, DB_PASSWORD


class LocalDBConfig:
    DB_URL = f'mysql+pymysql://root:heunyam@localhost:3306/tikitaka?charset=utf8mb4'


class RemoteDBConfig:
    DB_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4"
