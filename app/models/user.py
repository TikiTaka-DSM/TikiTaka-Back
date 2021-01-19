from sqlalchemy import Column, String, Integer

from app.models import Base, session


class User(Base):
    __tablename__ = 'users'

    id = Column(String(45), nullable=False, primary_key=True)
    password = Column(String(45), nullable=False)
    name = Column(String(45), nullable=False)
    img = Column(String(100), nullable=True)
    introduction = Column(String(100), nullable=True)


def get_user_data_by_user_id(user_id):
    return session.query(User).filter(User.id == user_id).first()
