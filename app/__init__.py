from flask import Flask


def create_app(*config_cls):

    _app = Flask(__name__)
    # _app.register_blueprint()

    for config in config_cls:
        _app.config.from_object(config)

    return _app
