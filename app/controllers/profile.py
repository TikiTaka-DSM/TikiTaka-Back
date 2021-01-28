from flask import abort
from uuid import uuid4
import json

from app.services.user import get_user_data_by_user_id, update_profile
from app.services.friend import get_friend_state
from app.services.member import get_room_id_by_member
from utils.s3 import upload_image_to_s3


def get_myprofile(user_id):

    user = get_user_data_by_user_id(user_id)

    return {
        "profileData": {
            "id": user_id,
            "img": user.img,
            "name": user.name,
            "statusMessage": user.introduction
        }
    }


def get_profile(owner_user_id, other_user_id):

    if owner_user_id == other_user_id:
        abort(409, "Please use 'GET /profile' api")

    user_data = get_user_data_by_user_id(other_user_id)
    friend_state = get_friend_state(owner_user_id, other_user_id)
    room_id = get_room_id_by_member(owner_user_id, other_user_id)
    return json.dumps({
        "profileData": {
            "id": other_user_id,
            "img": user_data.img,
            "name": user_data.name,
            "statusMessage": user_data.introduction
        },
        "state": {
            "friend": True if friend_state else False,
            "block": friend_state.blocking_state
        },
        "roomData": {
            "roomId": room_id if room_id else None
        }
    })


def edit_profile(user_id, img, name, status_message):

    if not get_user_data_by_user_id(user_id):
        abort(404, "This id not found")

    image_name = uuid4()
    user_data = {
        "name": name,
        "img": image_name,
        "status_message": status_message
    }

    if img:
        upload_image_to_s3(img, image_name)

    update_profile(user_id, user_data)

    return {
        "message": "Successfully edit profile"
    }
