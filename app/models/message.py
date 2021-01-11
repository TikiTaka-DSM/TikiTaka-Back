from sqlalchemy import Column, String, Integer, ForeignKey, TIMESTAMP, text

from app.models import Base


class Message(Base):
    __tablename__ = 'messages'

    user_id = Column(String(45), ForeignKey('users.id'), primary_key=True)
    room_id = Column(Integer, ForeignKey('rooms.id'), primary_key=True)
    content = Column(String(300), nullable=False)
    type = Column(String(10), nullable=False)
    created_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
