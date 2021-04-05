from sqlalchemy import Column, String

from app.models import Base


class UserDefaultValue:
    image = 'default.png'
    introduction = ''


class User(Base):
    __tablename__ = 'users'

    id = Column(String(45), nullable=False, primary_key=True)
    password = Column(String(100), nullable=False)
    name = Column(String(45), nullable=False)
    img = Column(String(100), nullable=True, server_default=UserDefaultValue.image)
    introduction = Column(String(100), nullable=True, server_default=UserDefaultValue.introduction)

    def __init__(self, id, password, name):
        self.id = id
        self.password = password
        self.name = name
