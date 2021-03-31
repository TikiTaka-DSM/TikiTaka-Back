import pytest
from app import create_app
from config.app import LocalAppConfig
from config.db import LocalDBConfig


@pytest.fixture
def api():
    test_app = create_app(LocalAppConfig, LocalDBConfig)
    test_app.config['TEST'] = True
    api = test_app.test_client()
    return api
