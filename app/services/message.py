from app.models.message import Message
from app.models import session


def insert_message(user_id, room_id, content, type):
    message = Message(user_id=user_id,
                      room_id=room_id,
                      content=content,
                      type=type)

    session.add(message)
    session.commit()
    session.close()

    return message