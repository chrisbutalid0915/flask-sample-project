import logging
from flask_restx import Namespace, Resource
from app.schemas.user import user_base_model, user_input_model
from app.services import get_password_hash
from app.models import User
from app import db
from flask_jwt_extended import get_jwt_identity, jwt_required

logging = logging.getLogger(__name__)

authorizations = {
    "jsonWebToken": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization"
    }
}

ns = Namespace("api", authorizations=authorizations)

@ns.route("/v1/users")
class UserAPI(Resource):
    @ns.expect(user_input_model)
    @ns.marshal_with(user_base_model)
    def post(self):
        try:
            user = ns.payload
            # get the hashed password
            hashed_password = get_password_hash(user["password_hash"])
            user["password_hash"] = hashed_password
            user = User(**dict(user))
            db.session.add(user)
            db.session.commit()
            logging.info(f'User successfully created.')
            return user, 201
        except Exception as e:
            logging.error(f'Error occured: {e}')


@ns.route("/v1/users/me")
class UserMe(Resource):
    @ns.marshal_with(user_base_model)
    @jwt_required()
    @ns.doc(security="jsonWebToken")
    def get(self):
        current_user = get_jwt_identity()
        user = User.query.filter(User.username == current_user).first()
        return user