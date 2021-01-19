from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.controllers.profile import get_profile


class MyProfile(Resource):
    @jwt_required
    def get(self):
        owner_user = get_jwt_identity()

        pass

    @jwt_required
    def put(self):
        owner_user = get_jwt_identity()

        pass


class Profile(Resource):
    @jwt_required
    def get(self, user_id):
        owner_user = get_jwt_identity()

        return get_profile(owner_user, user_id)
