from flask import abort
from uuid import uuid4

from app.services.user import user_data_by_user_id, update_profile
from app.services.friend import friend_state
from app.services.member import room_id_by_member
from utils.s3 import upload_image_to_s3


def get_myprofile(user_id):

    user = user_data_by_user_id(user_id)

    return {
        "profileData": {
            "id": user_id,
            "img": user.img,
            "name": user.name,
            "statusMessage": user.introduction
        }
    }


def get_profile(owner_user_id, other_user_id):
    if not user_data_by_user_id(other_user_id):
        abort(404, "This user not found")

    if owner_user_id == other_user_id:
        abort(409, "Please use 'GET /profile' api")

    user_data = user_data_by_user_id(other_user_id)
    friend_state = friend_state(owner_user_id, other_user_id)
    room_id = room_id_by_member(owner_user_id, other_user_id)
    return {
        "profileData": {
            "id": other_user_id,
            "img": user_data.img,
            "name": user_data.name,
            "statusMessage": user_data.introduction
        },
        "state": {
            "friend": True if friend_state else False,
            "block": False if not friend_state else friend_state.blocking_state
        },
        "roomData": {
            "roomId": room_id if room_id else None
        }
    }


def edit_profile(user_id, img, name, status_message):

    if not user_data_by_user_id(user_id):
        abort(404, "This id not found")

    if img:
        image_name = str(uuid4()) + ".png"
        upload_image_to_s3(img, image_name)
    else:
        image_name = None

    user_data = {
        "name": name,
        "img": image_name,
        "status_message": status_message
    }

    update_profile(user_id, user_data)

    return {
        "message": "Successfully edit profile"
    }
