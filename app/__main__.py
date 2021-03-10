from app import create_app
from app.models import Base, db_engine

from config.app import LocalAppConfig
from config.db import RemoteDBConfig


if __name__ == '__main__':
    app = create_app(LocalAppConfig, RemoteDBConfig)
    Base.metadata.create_all(db_engine)

    app.run()
