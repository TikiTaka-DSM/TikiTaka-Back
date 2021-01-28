from app.models import session, catch_exception
from app.models.user import User, UserDefaultValue


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
    return session.query(User).filter(User.id == user_id).first()


@catch_exception
def update_profile(user_id, user_data):
    user = session.query(User).filter(User.id == user_id).first()

    user.name = user_data['name']
    user.img = user_data['img']
    user.introduction = user_data['status_message']

    session.commit()
