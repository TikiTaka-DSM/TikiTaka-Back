from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.controllers.friend import create_new_friend, get_friends, search_friend_by_user_id, search_friend_by_user_name


class SearchToAddFriend(Resource):
    def get(self):
        user_id = request.args['id']

        return search_friend_by_user_id(user_id)


class AddFriend(Resource):
    @jwt_required
    def post(self, user_id):
        owner_user = get_jwt_identity()

        return create_new_friend(owner_user, user_id)


class GetFriends(Resource):
    @jwt_required
    def get(self):
        owner_user = get_jwt_identity()

        return get_friends(owner_user)


class SearchFriendName(Resource):
    @jwt_required
    def get(self, user_name):
        owner_user = get_jwt_identity()

        return search_friend_by_user_name(owner_user, user_name)