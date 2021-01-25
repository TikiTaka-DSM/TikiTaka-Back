import jwt
from config.app import LocalAppConfig


def get_jwt_identity_by_token(token, jwt_secret_key):
    jwt_token = jwt.decode(token, jwt_secret_key, algorithms="HS256")

    return jwt_token['identity']
