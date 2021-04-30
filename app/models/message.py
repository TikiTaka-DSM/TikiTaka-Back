from sqlalchemy import Column, String, Integer, ForeignKey, TIMESTAMP, text
from app.models import Base, session


class MessageType:
    message = "text"
    photo = "png"
    voice = "mp3"


class MessageModel(Base):
    __tablename__ = 'messages'

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(String(45), ForeignKey('users.id'))
    room_id = Column(Integer, ForeignKey('rooms.id'))
    content = Column(String(300), nullable=False)
    type = Column(String(10), nullable=False)
    created_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))

    @staticmethod
    def insert_message(user_id, room_id, content, type):
        message = MessageModel(user_id=user_id,
                               room_id=room_id,
                               content=content,
                               type=type)

        session.add(message)
        session.commit()

    @staticmethod
    def get_latest_message_in_room(room_id):
        _message = session.query(MessageModel). \
            filter(MessageModel.room_id == room_id). \
            order_by(MessageModel.created_at.desc()).first()

        return _message

    @staticmethod
    def get_messages(room_id):
        _messages = session.query(MessageModel). \
            filter(MessageModel.room_id == room_id). \
            order_by(MessageModel.created_at).all()

        return _messages


