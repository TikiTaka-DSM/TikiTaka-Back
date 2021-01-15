from app import create_app, create_socketio
from config.app import LocalAppConfig
from config.db import RemoteDBConfig


if __name__ == '__main__':
    app = create_app(LocalAppConfig, RemoteDBConfig)
    socketio = create_socketio(app)

    socketio.run(app, debug=True)
