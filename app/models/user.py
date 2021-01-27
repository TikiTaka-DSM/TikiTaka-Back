from sqlalchemy import Column, String

from app.models import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(String(45), nullable=False, primary_key=True)
    password = Column(String(45), nullable=False)
    name = Column(String(45), nullable=False)
    img = Column(String(100), nullable=True)
    introduction = Column(String(100), nullable=True)


class UserDefaultValue:
    image = 'default.png'
    introduction = ''
