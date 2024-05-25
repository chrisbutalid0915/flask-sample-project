from flask_restx import fields
from werkzeug.exceptions import BadRequest
from app.extensions import api

# Custom validation function for latitude
def validate_latitude(value):
    if -90 <= value <= 90:
        return True
    else:
        raise BadRequest("Latitude must be between -90 and 90 degrees")


def validate_longitude(value):
    if -180 <= value <= 180:
        return True
    else:
        raise BadRequest("Longitude must be between -180 and 180 degrees")
        

address_input_model = api.model("AddressInput", {
    "location": fields.String(required=True, description='Address Description'),
    "latitude": fields.Float(required=True, description='Address latitude', action=validate_latitude),
    "longitude": fields.Float(required=True, description='Address longitude', action=validate_longitude)
})

address_base_model = api.model("Address", {
    "id": fields.Integer(description='The address unique identifier'),
    "location": fields.String(description='Address description'),
    "latitude": fields.Float(description='Address latitude'),
    "longitude": fields.Float(description='Address longitude')
})

address_model = api.model("ResponseModel", {
    "data": fields.Nested(address_base_model)
})

distance_input_model = api.model('DistanceInput',{
    "distance": fields.Float(required=True, description='Distance in kilometers'),
    "latitude": fields.Float(required=True, description='Current location latitude'),
    "longitude": fields.Float(required=True, description='Current location longitude')
})