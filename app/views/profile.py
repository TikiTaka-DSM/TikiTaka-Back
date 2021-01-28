from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.controllers.profile import get_profile, get_myprofile, edit_profile


class MyProfile(Resource):
    @jwt_required
    def get(self):
        owner_user = get_jwt_identity()

        return get_myprofile(owner_user)

    @jwt_required
    def put(self):
        print(request.files)
        img = request.files['img']
        name = request.form['name']
        status_message = request.form['statusMessage']

        owner_user = get_jwt_identity()
        return edit_profile(user_id=owner_user,
                            img=img,
                            name=name,
                            status_message=status_message)


class Profile(Resource):
    @jwt_required
    def get(self, user_id):
        owner_user = get_jwt_identity()

        return get_profile(owner_user, user_id)
