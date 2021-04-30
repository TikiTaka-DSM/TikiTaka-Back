from sqlalchemy import Column, String, ForeignKey
from app.models import Base, session
from sqlalchemy import func


class MemberModel(Base):
    __tablename__ = 'members'

    user_id = Column(String(45), ForeignKey('users.id'), primary_key=True)
    room_id = Column(String(45), ForeignKey('rooms.id'), primary_key=True)

    @staticmethod
    def insert_member(room_id, user_id):
        member = MemberModel(room_id=room_id,
                             user_id=user_id)

        session.add(member)
        session.commit()

    @staticmethod
    def get_room_id_by_member(user_id, friend_user_id):
        member = session.query(MemberModel). \
            filter((MemberModel.user_id == user_id) | (MemberModel.user_id == friend_user_id)). \
            group_by(MemberModel.room_id). \
            having(func.count(MemberModel.room_id) > 1).first()

        return member.room_id if member else None

    @staticmethod
    def get_members_by_user_id(user_id):
        member = session.query(MemberModel).filter(MemberModel.user_id == user_id).all()

        return member

    @staticmethod
    def get_chatting_member(room_id, user_id):
        member = session.query(MemberModel).filter(MemberModel.room_id == room_id).filter(MemberModel.user_id != user_id).first()

        return member