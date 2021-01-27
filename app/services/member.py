from app.models.member import Member
from app.models import session
from sqlalchemy import func


def get_room_id(user_id, friend_user_id):
    room_id = session.query(Member).\
                filter((Member.user_id == user_id) | (Member.user_id == friend_user_id)).\
                group_by(Member.room_id).\
                having(func.count(Member.room_id) > 1).first()

    return room_id
