from app.services.member import get_room_id_by_member, get_chatting_member, get_members_by_user_id
from app.services.room import insert_room
from app.services.user import get_user_data_by_user_id
from app.services.member import insert_member
from app.services.message import get_latest_message, get_messages
from app.models.message import MessageType
from flask import abort


def create_new_chatting_room(owner_user_id, friend_user_id):
    room_id = get_room_id_by_member(owner_user_id, friend_user_id)

    if not room_id:
        room_id = insert_room()
        insert_member(room_id, owner_user_id)
        insert_member(room_id, friend_user_id)

    return {
        "roomData": {
            "id": room_id
        }
    }


def get_chatting_rooms(owner_user_id):
    rooms = []
    friends = []
    messages = []
    friend_members = []

    owner_user_members = get_members_by_user_id(owner_user_id)
    for member in owner_user_members:
        friend_members.append(get_chatting_member(member.room_id, owner_user_id))

    for member in friend_members:
        rooms.append(member.room_id)
        friends.append(get_user_data_by_user_id(member.user_id))
        messages.append(get_latest_message(member.room_id))

    return {
        "rooms": [{
            "roomId": room_id,
            "user": {
                "id": user.id,
                "img": user.img,
                "name": user.name
            },
            "lastMessage": message.content if message else ""
        } for room_id, user, message in zip(rooms, friends, messages)]
    }


def get_chatting_room_detail(room_id, owner_user_id):
    member = get_chatting_member(room_id, owner_user_id)
    if not member:
        abort(404, "No Member Data in Room")

    friend = get_user_data_by_user_id(member.user_id)
    messages = get_messages(room_id)

    return {
        "roomData": {
            "id": room_id,
            "name": friend.name,
            "img": friend.img
        },
        "messageData": [{
            "user": {
                "id": message.user_id,
                "name": get_user_data_by_user_id(message.user_id).name,
                "img": get_user_data_by_user_id(message.user_id).img
            },
            "message": message.content if message.type == MessageType.message else None,
            "photo": message.content if message.type == MessageType.photo else None,
            "voice": message.content if message.type == MessageType.voice else None,
            "created_at": str(message.created_at)
        } for message in messages]
    }
