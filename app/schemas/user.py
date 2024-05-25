from flask_restx import fields
from app.extensions import api


user_base_model = api.model("User", {
    "username": fields.String(required=True, description="Username"),
    "email": fields.String(required=True, unique=True, description="Email Address"),
})


user_input_model = api.inherit("UserInput", user_base_model, {
    "password_hash": fields.String(required=True, description="Password"),
})


auth_model = api.model('Auth', {
    'username': fields.String(required=True, description='The username'),
    'password_hash': fields.String(required=True, description='The password')
})