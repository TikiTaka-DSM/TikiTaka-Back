from datetime import timedelta


class LocalAppConfig:
    JWT_SECRET_KEY = 'XJ3vmK&5SQ}SS9WN?smA'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=15)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=1)


class ProductionAppConfig:
    pass
