from flask import Blueprint, jsonify, request
from models.store import Store

stores_api_blueprint = Blueprint('stores_api',
                                 __name__,
                                 template_folder='templates')


@stores_api_blueprint.route('/', methods=["POST"])
def create():
    s = Store(
        name=request.json.get('name'),
        building_number=request.json.get('building_number'),
        street_name=request.json.get('street_name'),
        city=request.json.get('city'),
        country=request.json.get('country'),
        location_index=request.json.get('location_index'),
        postal_zip_code=request.json.get('postal_zip_code'),
        area=request.json.get('area'),
        nearby=request.json.get('nearby'),
        opening_hours=request.json.get('opening_hours'),
    )
    if s.save():
        return jsonify({
            'id': s.id,
            'message': "Store successfully created"
        }), 200
    else:
        # the following error doesn't actually work if it's a DB integrity error; can improve error handling here in future if required.
        return jsonify(s.errors), 400  # bad request


# GET A SINGLE STORE (NOT SURE IF THIS ENDPOINT IS NEEDED)
@stores_api_blueprint.route('/<id>', methods=["GET"])
def show(id):
    s = Store.get_or_none(Store.id == id)
    if s:
        return jsonify({
            'name': s.name
        }), 200
    else:
        return jsonify({
            'message': "Stores doesn't exist"
        }), 418  # teapot error


# GET STORES BASED ON LOCATION INDEX
# EXAMPLE REQUEST URL: https://dropandgo.herokuapp.com/api/v1/stores?location=1
@stores_api_blueprint.route('/', methods=["GET"])
def index():
    s = Store.select().where(Store.location_index == request.args.get('location'))
    # WILL NEED TO LOOP THROUGH RESULTS HERE TO CREATE JSON OBJECT
    if s:
        return jsonify({
            'name': s.name
        }), 200
    else:
        return jsonify({
            'message': "User doesn't exist"
        }), 418  # teapot error
