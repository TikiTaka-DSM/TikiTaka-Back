from flask_restful import Resource
from flask import request

from app.controllers.user import login, sign_up
from schematics.models import Model
from schematics.types import StringType
from app.views import validate_json


class Auth(Resource):
    class Schema(Model):
        id = StringType(
            serialized_name='id',
            required=True
        )

        password = StringType(
            serialized_name='password',
            required=True
        )

    @validate_json(Schema)
    def post(self):

        user_id = request.json['id']
        user_password = request.json['password']

        return login(user_id, user_password)


class User(Resource):
    class Schema(Model):
        id = StringType(
            serialized_name='id',
            required=True,
            max_length=45
        )

        password = StringType(
            serialized_name='password',
            required=True
        )

        name = StringType(
            serialized_name='name',
            required=True,
            max_length=45
        )

    @validate_json(Schema)
    def post(self):

        user_id = request.json['id']
        user_password = request.json['password']
        user_name = request.json['name']

        return sign_up(user_id, user_password, user_name)






