from sqlalchemy import Column, String, ForeignKey, Boolean

from app.models import Base, session, catch_exception


class Friend(Base):
    __tablename__ = 'friends'

    user_id = Column(String(45), ForeignKey('users.id'), primary_key=True)
    friend_user_id = Column(String(45), ForeignKey('users.id'), primary_key=True)
    blocking_state = Column(Boolean, nullable=False, default=False)


# @catch_exception
def get_friendship_data(owner_user_id):
    friendships = session.query(Friend).filter(Friend.user_id == owner_user_id).all()

    return friendships


# @catch_exception
def get_friend_state(owner_user, other_user):
    friendship = session.query(Friend).filter(Friend.user_id == owner_user).\
                          filter(Friend.friend_user_id == other_user).first()

    return friendship
