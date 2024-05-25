from flask_restx import fields
from app.extensions import api

token_model = api.model('Token', {
    'access_token': fields.String(description='Access token')
})