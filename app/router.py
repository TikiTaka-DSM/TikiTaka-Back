from flask_restful import Api
from flask import Blueprint, current_app

from app.views.ping import Ping
from app.views.user import Auth, User
from app.views.friend import AddFriend, GetFriends, SearchToAddFriend
from app.views.room import CreateNewRoom
from app.views.profile import Profile, MyProfile


class CustomApi(Api):
    def handle_error(self, e):
        for val in current_app.error_handler_spec.values():
            for handler in val.values():
                registered_error_handlers = list(filter(lambda x: isinstance(e, x), handler.keys()))
                if len(registered_error_handlers) > 0:
                    raise e
        return super().handle_error(e)


bp = Blueprint("api", __name__, url_prefix="")
api = CustomApi(bp)

api.add_resource(Ping, '/ping')

api.add_resource(User, '/user')
api.add_resource(Auth, '/user/auth')

api.add_resource(AddFriend, '/friend/<user_id>')
api.add_resource(GetFriends, '/friends')
api.add_resource(SearchToAddFriend, '/friend')

api.add_resource(CreateNewRoom, '/room')

api.add_resource(Profile, '/profile/<user_id>')
api.add_resource(MyProfile, '/profile')
