from app.models.message import Message
from app.models import session, catch_exception


@catch_exception
def insert_message(user_id, room_id, content, type):
    message = Message(user_id=user_id,
                      room_id=room_id,
                      content=content,
                      type=type)

    session.add(message)
    session.commit()


@catch_exception
def latest_message(room_id):
    _message = session.query(Message).\
                    filter(Message.room_id == room_id).\
                    order_by(Message.created_at.desc()).first()

    return _message


@catch_exception
def messages(room_id):
    _messages = session.query(Message).\
                filter(Message.room_id == room_id).\
                order_by(Message.created_at).all()

    return _messages
