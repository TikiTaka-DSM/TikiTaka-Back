from app.models.member import Member
from app.models import session, catch_exception
from sqlalchemy import func


@catch_exception
def insert_member(room_id, user_id):
    member = Member(room_id=room_id,
                    user_id=user_id)

    session.add(member)
    session.commit()


@catch_exception
def room_id_by_member(user_id, friend_user_id):
    member = session.query(Member).\
                filter((Member.user_id == user_id) | (Member.user_id == friend_user_id)).\
                group_by(Member.room_id).\
                having(func.count(Member.room_id) > 1).first()

    return member.room_id if member else None


@catch_exception
def members_by_user_id(user_id):
    member = session.query(Member).filter(Member.user_id == user_id).all()

    return member

@catch_exception
def chatting_member(room_id, user_id):
    member = session.query(Member).filter(Member.room_id == room_id).filter(Member.user_id != user_id).first()

    return member