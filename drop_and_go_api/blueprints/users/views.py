from flask import Blueprint, jsonify, request
from models.user import User

users_api_blueprint = Blueprint('users_api',
                             __name__,
                             template_folder='templates')



@users_api_blueprint.route('/', methods=["POST"])
def create():
    u = User(
        name=request.json.get('name'),
        user_type=request.json.get('user_type'),
        email=request.json.get('email'),
        password=request.json.get('password'),
        phone_number=request.json.get('phone_number'),
        image_filename=request.json.get('image_filename')
    )
    if u.save():
        return jsonify({
            'id': u.id,
            'message': "User successfully created"
        }), 200
    else:
        # the following error doesn't actually work if it's a DB integrity error; can improve error handling here in future if required.
        return jsonify(u.errors), 400 # bad request


@users_api_blueprint.route('/<id>', methods=["GET"])
def show(id):
    u = User.get_or_none(User.id == id)
    if u:
        return jsonify({
            'id': u.id,
            'name': u.name,
            'email': u.email,
            'user_type': u.user_type,
            'phone_number': u.phone_number, 
            'image_filename': u.image_filename
        }), 200
    else:
        return jsonify({
            'message': "User doesn't exist"
        }), 418 # teapot error
