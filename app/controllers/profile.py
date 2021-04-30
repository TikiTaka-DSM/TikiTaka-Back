from flask import abort
from uuid import uuid4

from app.models.user import UserModel
from app.models.member import MemberModel
from app.models.friend import FriendModel
from utils.s3 import upload_image_to_s3


def get_myprofile(user_id):

    user = UserModel.get_user_data_by_user_id(user_id)

    return {
        "profileData": {
            "id": user_id,
            "img": user.img,
            "name": user.name,
            "statusMessage": user.introduction
        }
    }


def get_profile(owner_user_id, other_user_id):
    if not UserModel.get_user_data_by_user_id(other_user_id):
        abort(404, "This user not found")

    if owner_user_id == other_user_id:
        abort(409, "Please use 'GET /profile' api")

    user_data = UserModel.get_user_data_by_user_id(other_user_id)
    friend_state = FriendModel.get_friend_state(owner_user_id, other_user_id)
    room_id = MemberModel.get_room_id_by_member(owner_user_id, other_user_id)
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

    if not UserModel.get_user_data_by_user_id(user_id):
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

    UserModel.update_profile(user_id, user_data)

    return {
        "message": "Successfully edit profile"
    }
