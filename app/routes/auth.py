import logging
from flask_restx import Namespace, Resource
from app.schemas.user import auth_model
from app.schemas.token import token_model
from app.models import User
from app.services import authtenticate_user
from flask_jwt_extended import create_access_token

logging = logging.getLogger(__name__)

ns = Namespace("api")

@ns.route("/token")
class TokenAPI(Resource):
    @ns.expect(auth_model)
    @ns.marshal_with(token_model)
    def post(self):
        username = ns.payload["username"]
        password_hash = ns.payload["password_hash"]
        user = authtenticate_user(User, username, password_hash)
        if not user:
            return {'message': 'Invalid credentials'}, 401
        access_token = create_access_token(identity=user.username)
        return {'access_token': access_token}, 200