from flask import Blueprint, jsonify, request
from models.store import Store
from models.user import User
from models.store import Store
from models.booking import Booking
from models.payment import Payment

payments_api_blueprint = Blueprint('payments_api',
                                   __name__,
                                   template_folder='templates')


@payments_api_blueprint.route('/', methods=["POST"])
def create():
    p = Payment(
        user = request.json.get('user'),
        booking = request.json.get('booking'),
        trans_id = request.json.get('trans_id'),
        currency = request.json.get('currency'),
        amount = request.json.get('amount')
    )

    if p.save():
            return jsonify({
                'id': p.id,
                'message': "Payment successfully created"
            }), 200

    else:
        # the following error doesn't actually work if it's a DB integrity error; can improve error handling here in future if required.
        return jsonify(p.errors), 400  # bad request
