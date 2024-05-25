
import logging
from app.schemas.address import address_input_model, address_model, distance_input_model, validate_latitude, validate_longitude
from app.models import Address
from app import db
from flask_restx import Namespace, Resource
from werkzeug.exceptions import NotFound
from geopy.distance import geodesic

logging = logging.getLogger(__name__)

ns = Namespace("api")

@ns.route("/v1/addresses")
class AddressListApi(Resource):
    @ns.expect(address_input_model)
    # return a dict base from the model ex. `address_model`
    @ns.marshal_with(address_model) 
    def post(self):
        logging.info("Processing add new address")
        latitude = ns.payload["latitude"]
        longitude = ns.payload["longitude"]
        # validate the range of latitude and longitude
        if validate_latitude(latitude) and validate_longitude(longitude): 
            address = Address(**dict(ns.payload))
            db.session.add(address)
            # commit the transaction
            db.session.commit() 
            logging.info(f'Address successfully created: {address}')
            return {"data": address}, 201

    @ns.marshal_list_with(address_model)
    def get(self):
        logging.info("Processing get all address")
        addresses = Address.query.all()
        return {"data": addresses}
    
    
@ns.route("/v1/addresses/<int:address_id>")
class AddressApi(Resource):
    @ns.marshal_with(address_model)
    def get(self, address_id):
        logging.info("Processing get address")
        address = Address.query.get(address_id)
        if address is None:
            logging.error("Address not found")
            raise NotFound("Address not found")
        return {"data": address}
    
    
    @ns.expect(address_input_model)
    @ns.marshal_with(address_model)
    def put(self, address_id):
        logging.info("Processing update address")
        # get the address by ID
        address = Address.query.filter(Address.id==address_id).first() 
        if address is None:
            logging.error("Address not found")
            raise NotFound("Address not found")
        
        # update the selected query
        for key, value in dict(ns.payload).items():
            setattr(address, key, value)

        # commit the transaction
        db.session.commit() 
        return {"data": address}
    

    @ns.marshal_with(address_model)
    def delete(self, address_id):
        logging.info("Processing delete address")
        address = Address.query.get(address_id)
        if address is None:
            logging.error("Address not found")
            raise NotFound("Address not found")
        db.session.delete(address)
        db.session.commit()
        return {"data": address}, 204


@ns.route("/v1/distances")
class AddressDistanceApi(Resource):
    @ns.expect(distance_input_model)
    @ns.marshal_list_with(address_model)
    def post(self):
        try:
            logging.info("Processing get by distance address")
            current_location = (ns.payload['latitude'], ns.payload['longitude'])
            
            # Extract the input data from the request
            data = ns.payload
            current_location = (ns.payload['latitude'], ns.payload['longitude'])
            distance = data['distance']

            # Query all addresses
            all_addresses = Address.query.all()

            # get the addresses within the range
            addresses_within_distance = [
                address for address in all_addresses 
                if geodesic(current_location, (address.latitude, address.longitude)).km <= distance
            ] 
            return {"data": addresses_within_distance}
        except Exception as e:
            logging.error(f'error: {e}')