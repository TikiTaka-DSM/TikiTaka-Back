from config.config import DB_NAME, DB_USER, DB_HOST, DB_PORT, DB_PASSWORD


class LocalDBConfig:
    DB_URL = f'mysql+pymysql://root:heunyam@localhost:3306/tikitaka?charset=utf8mb4'


class RemoteDBConfig:
    DATABASE_USER = DB_USER
    DATABASE_PASSWORD = DB_PASSWORD
    DATABASE_HOST = DB_HOST
    DATABASE_PORT = DB_PORT
    DATABASE_NAME = DB_NAME
