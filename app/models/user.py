from sqlalchemy import Column, String
from app.models import Base, session
from .friend import FriendModel


class UserDefaultValue:
    image = 'default.png'
    introduction = ''


class UserModel(Base):
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

    @staticmethod
    def insert_user(user_id, password, name):

        user = UserModel(user_id, password, name)

        session.add(user)
        session.commit()
        session.close()

    @staticmethod
    def get_user_data_by_user_id(user_id):
        return session.query(UserModel).filter(UserModel.id == user_id).first()

    @staticmethod
    def get_user_data_by_user_name(owner, user_name):
        current_users = []
        users = session.query(UserModel).filter(UserModel.name.like(f'%{user_name}%')).all()
        for user in users:
            if FriendModel.get_friend_state(owner, user.id):
                current_users.append(user)

        return current_users

    @staticmethod
    def update_profile(user_id, user_data):
        user = session.query(UserModel).filter(UserModel.id == user_id).first()

        user.name = user_data['name'] if user_data['name'] else user.name
        user.img = user_data['img'] if user_data['img'] else user.img
        user.introduction = user_data['status_message'] if user_data['status_message'] else user.introduction

        session.commit()

