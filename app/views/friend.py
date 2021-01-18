from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.controllers.friend import create_new_friend


class SearchToAddFriend(Resource):
    def get(self, user_id):
        pass


class AddFriend(Resource):
    @jwt_required
    def post(self, user_id):
        owner_user = get_jwt_identity()

        return create_new_friend(owner_user, user_id)


class GetFriends(Resource):
    @jwt_required
    def get(self):
        owner_user = get_jwt_identity()
        pass