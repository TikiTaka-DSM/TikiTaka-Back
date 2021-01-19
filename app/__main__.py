from app import create_app, create_socketio
from app.models import Base, db_engine

from config.app import LocalAppConfig
from config.db import RemoteDBConfig


if __name__ == '__main__':
    app = create_app(LocalAppConfig, RemoteDBConfig)
    socketio = create_socketio(app)

    Base.metadata.create_all(db_engine)

    socketio.run(app, debug=True)
