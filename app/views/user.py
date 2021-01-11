from flask_restful import Resource
from flask import request


class Auth(Resource):
    def post(self):
        """

        :return:
        """
        user_id = request.json['id']
        user_pw = request.json['password']

        pass


class User(Resource):
    def post(self):
        """
        User Registration
        :return:
        """

        user_id = request.json['id']
        user_pw = request.json['password']
        user_name = request.json['name']

        pass




