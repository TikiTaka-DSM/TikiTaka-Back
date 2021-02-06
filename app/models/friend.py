from sqlalchemy import Column, String, ForeignKey, Boolean

from app.models import Base


class Friend(Base):
    __tablename__ = 'friends'

    user_id = Column(String(45), ForeignKey('users.id'), primary_key=True)
    friend_user_id = Column(String(45), ForeignKey('users.id'), primary_key=True)
    blocking_state = Column(Boolean, nullable=False, default=False)
