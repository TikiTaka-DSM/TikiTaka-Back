from sqlalchemy import Column, String

from app.models import Base, session, catch_exception


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


def insert_user(user_id, user_password, user_name):

    user = User(id=user_id,
                password=user_password,
                name=user_name,
                img=UserDefaultValue.image,
                introduction=UserDefaultValue.introduction)

    session.add(user)
    session.commit()
    session.close()


@catch_exception
def get_user_data_by_user_id(user_id):
    user_data = session.query(User).filter(User.id == user_id).first()

    return user_data


@catch_exception
def update_profile(user_id, user_data):
    user = get_user_data_by_user_id(user_id)

    user.name = user_data.name if user_data.name else user.name
    user.img = user_data.img if user_data.img else user.img
    user.introduction = user_data.status_message if user_data.status_message else user.introduction

    session.commit()
    session.close()
