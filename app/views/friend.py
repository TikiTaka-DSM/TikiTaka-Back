from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.controllers.friend import create_new_friend, get_friends, search_friend_by_user_id, search_friend_by_user_name, block_friend


class Friends(Resource):

    @jwt_required
    def get(self):
        owner_user = get_jwt_identity()

        return get_friends(owner_user)

    @jwt_required
    def post(self):
        owner_user = get_jwt_identity()
        user_id = request.json['friendId']

        return create_new_friend(owner_user, user_id)


class Friend(Resource):
    def get(self):
        user_id = request.args['id']

        return search_friend_by_user_id(user_id)

    @jwt_required
    def put(self, user_id):
        owner_user = get_jwt_identity()

        return block_friend(owner_user, user_id)


class SearchFriendName(Resource):
    @jwt_required
    def get(self):
        owner_user = get_jwt_identity()
        user_name = request.args['name']

        return search_friend_by_user_name(owner_user, user_name)

