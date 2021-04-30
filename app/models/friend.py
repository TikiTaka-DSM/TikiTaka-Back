from sqlalchemy import Column, String, ForeignKey, Boolean
from app.models import Base, session


class FriendModel(Base):
    __tablename__ = 'friends'

    user_id: str = Column(String(45), ForeignKey('users.id'), primary_key=True)
    friend_user_id: str = Column(String(45), ForeignKey('users.id'), primary_key=True)
    blocking_state: bool = Column(Boolean, nullable=False, default=False)

    def __init__(self, user_id: str, friend_user_id: str):
        self.user_id = user_id
        self.friend_user_id = friend_user_id
        self.blocking_state = False

    @staticmethod
    def get_friendship_data(owner_user_id):
        friendships = session.query(FriendModel).filter(FriendModel.user_id == owner_user_id).all()

        return friendships

    @staticmethod
    def get_friend_state(owner_user, other_user):
        friendship = session.query(FriendModel).filter(FriendModel.user_id == owner_user). \
            filter(FriendModel.friend_user_id == other_user).first()

        return friendship

    @staticmethod
    def insert_friend(owner_user_id, other_user_id):
        friendship = FriendModel(user_id=owner_user_id, friend_user_id=other_user_id)
        additional_friendship = FriendModel(user_id=other_user_id, friend_user_id=owner_user_id)

        session.add(friendship)
        session.add(additional_friendship)
        session.commit()

    @staticmethod
    def switching_blocking_state(owner_id, friend_id):
        friendship = session.query(FriendModel).filter(FriendModel.user_id == owner_id). \
            filter(FriendModel.friend_user_id == friend_id).first()

        friendship.blocking_state = False if friendship.blocking_state else True
        session.commit()


