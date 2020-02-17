from flask import Blueprint, jsonify, request
from models.store import Store
from models.user import User

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
        nearby2=request.json.get('nearby2'),
        opening_hours=request.json.get('opening_hours'),
        store_image=request.json.get('store_image'),
        owner=request.json.get('owner'),
        price=request.json.get('price'),
        star_rating=request.json.get('star_rating'),
        operating_day=request.json.get('operating_day')
    )
    if s.save():
        return jsonify({
            'is_success': True,
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
            'is_success': True,
            'name': s.name,
            'building_number': s.building_number,
            'street_name': s.street_name,
            'city': s.city,
            'country': s.country,
            'location_index': s.location_index,
            'postal_zip_code': s.postal_zip_code,
            'area': s.area,
            'nearby': s.nearby,
            'nearby2': s.nearby2,
            'opening_hours': s.opening_hours,
            'store_image': s.store_image,
            'owner_id': s.owner_id,
            'price': s.price,
            'star_rating': s.star_rating,
            'operating_day': s.operating_day
        }), 200
    else:
        return jsonify({
            'is_success': False,
            'message': "Stores doesn't exist"
        }), 418  # teapot error


# GET STORES BASED ON LOCATION INDEX
# EXAMPLE REQUEST URL: https://dropandgo.herokuapp.com/api/v1/stores/?loc=1
@stores_api_blueprint.route('/', methods=['GET'])
def loc_show():

    loc_args = request.args.get('loc')

    if loc_args:
        stores = Store.select().where(Store.location_index == loc_args)
        if stores:
            store_list = []
            for store in stores:
                store_list.append({
                    'id': store.id,
                    'name': store.name,
                    'building_number': store.building_number,
                    'street_name': store.street_name,
                    'city': store.city,
                    'country': store.country,
                    'location_index': store.location_index,
                    'postal_zip_code': store.postal_zip_code,
                    'area': store.area,
                    'nearby': store.nearby,
                    'nearby2': store.nearby2,
                    'opening_hours': store.opening_hours,
                    'store_image': store.store_image,
                    'owner_id': store.owner_id,
                    'price': store.price,
                    'star_rating': store.star_rating,
                    'operating_day': store.operating_day,
                    
                })
            return jsonify(store_list)

        else:
            return jsonify({
                'is_success': False,
                'message': "Store doesn't exist"
            }), 418  # teapot error
    else:
        return jsonify({
            'is_success': False,
            'message': "Wrong argument input"
        }), 418  # teapot error
