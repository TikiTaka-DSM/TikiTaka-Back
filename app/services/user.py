from app.models import session, catch_exception
from app.models.user import User
from app.services.friend import friend_state


def insert_user(user_id, user_password, user_name):

    user = User(
            id=user_id,
            password=user_password,
            name=user_name
            )

    session.add(user)
    session.commit()
    session.close()


@catch_exception
def user_data_by_user_id(user_id):
    return session.query(User).filter(User.id == user_id).first()


@catch_exception
def user_data_by_user_name(owner, user_name):
    current_users = []
    users = session.query(User).filter(User.name.like(f'%{user_name}%')).all()
    for user in users:
        if friend_state(owner, user.id):
            current_users.append(user)

    return current_users


@catch_exception
def update_profile(user_id, user_data):
    user = session.query(User).filter(User.id == user_id).first()

    user.name = user_data['name'] if user_data['name'] else user.name
    user.img = user_data['img'] if user_data['img'] else user.img
    user.introduction = user_data['status_message'] if user_data['status_message'] else user.introduction

    session.commit()
