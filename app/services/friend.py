from app.models import session, catch_exception
from app.models.friend import Friend


@catch_exception
def get_friendship_data(owner_user_id):
    friendships = session.query(Friend).filter(Friend.user_id == owner_user_id).all()

    return friendships


@catch_exception
def get_friend_state(owner_user, other_user):
    friendship = session.query(Friend).filter(Friend.user_id == owner_user).\
                          filter(Friend.friend_user_id == other_user).first()

    return friendship


@catch_exception
def insert_friend(owner_user_id, other_user_id):
    friendship = Friend(user_id=owner_user_id,
                        friend_user_id=other_user_id)

    additional_friendship = Friend(user_id=other_user_id,
                                   friend_user_id=owner_user_id)

    session.add(friendship)
    session.add(additional_friendship)
    session.commit()
    session.close()
