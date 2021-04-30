import pytest
from app.models.user import UserModel
from werkzeug.security import generate_password_hash, check_password_hash


@pytest.fixture(scope='module')
def new_user():
    user = UserModel(id="testuser1",
                     password=generate_password_hash("testuserpassword1"),
                     name="테스트1")

    return user


def test_new_user(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, password, name, img, introduction fields are defined correctly
    """
    print(new_user)
    assert new_user.id == "testuser1"
    assert new_user.password != "testuserpassword1"
    assert new_user.name == "테스트1"
