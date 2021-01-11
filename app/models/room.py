from sqlalchemy import Column, String, Integer

from app.models import Base


class Room(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(40), nullable=False)