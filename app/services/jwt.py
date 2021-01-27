import jwt
from config.app import LocalAppConfig


def get_jwt_identity_by_token(token):
    jwt_token = jwt.decode(token, LocalAppConfig.JWT_SECRET_KEY, algorithms="HS256")

    return jwt_token['identity']
