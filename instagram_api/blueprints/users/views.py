from flask import Blueprint
from models.user import User

users_api_blueprint = Blueprint('users_api',
                             __name__,
                             template_folder='templates')


@users_api_blueprint.route('/<id>', methods=["GET"])
def show(id):
    pass
