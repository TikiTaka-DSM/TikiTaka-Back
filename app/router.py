from flask_restful import Api
from flask import Blueprint

from app.views.ping import Ping
from app.views.user import Auth, User
from app.views.friend import AddFriend, GetFriends
from app.views.room import CreateNewRoom
from app.views.profile import Profile


bp = Blueprint("api", __name__, url_prefix="")
api = Api(bp)

api.add_resource(Ping, '/ping')

api.add_resource(User, '/user')
api.add_resource(Auth, '/user/auth')
api.add_resource(AddFriend, '/friend/<user_id>')
api.add_resource(GetFriends, '/friends')
api.add_resource(CreateNewRoom, '/room')
api.add_resource(Profile, '/profile/<user_id>')
