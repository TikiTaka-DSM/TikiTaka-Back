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
    session.close()

    return message


@catch_exception
def get_latest_message(room_id, user_id):
    return session.query(Message).\
        filter(Message.room_id == room_id).\
        filter(Message.user_id == user_id).\
        order_by(Message.created_at.desc()).first()


@catch_exception
def get_messages(room_id):
    return session.query(Message).\
        filter(Message.room_id == room_id).\
        order_by(Message.created_at).all()
