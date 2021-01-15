from flask_restful import Resource
from flask import request

from app.controllers.user import login, sign_up


class Auth(Resource):
    def post(self):

        user_id = request.json['id']
        user_password = request.json['password']

        return login(user_id, user_password)


class User(Resource):
    def post(self):

        user_id = request.json['id']
        user_password = request.json['password']
        user_name = request.json['name']

        return sign_up(user_id, user_password, user_name)






