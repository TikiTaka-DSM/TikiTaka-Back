from sqlalchemy import Column, String, ForeignKey

from app.models import Base


class Member(Base):
    __tablename__ = 'members'

    user_id = Column(String(45), ForeignKey('users.id'), primary_key=True)
    room_id = Column(String(45), ForeignKey('rooms.id'), primary_key=True)