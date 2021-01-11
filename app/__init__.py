from flask import Flask
from flask_socketio import SocketIO
from app.router import bp
from flask_jwt_extended import JWTManager


def create_app(*config_cls):

    _app = Flask(__name__)
    _app.register_blueprint(bp)

    for config in config_cls:
        _app.config.from_object(config)

    JWTManager(_app)

    return _app


def create_socketio(app):
    socketio = SocketIO(app)

    return socketio
