from flask import Blueprint, jsonify, request
from models.store import Store
from models.user import User
from models.booking import Booking

bookings_api_blueprint = Blueprint('bookings_api',
                              __name__,
                              template_folder='templates')


@bookings_api_blueprint.route('/', methods=["POST"])
def create():
    # GET THE BOOKING BASED ON ID
    # GET BOOKING BASED ON USER ID
    # CREATE BOOKING
      b = Booking(
            check_in_date_time=request.json.get('check_in_date_time'),
            check_out_date_time=request.json.get('check_out_date_time'),
            number_of_bag=request.json.get('number_of_bag'),
            price=request.json.get('price'),
            # total_price=price * number_of_bag,
            status=request.json.get('status')
      )
      if b.save():
            return jsonify({
            'id': b.id,
            'message': "User successfully booked"
            }), 200
      else:
            # the following error doesn't actually work if it's a DB integrity error; can improve error handling here in future if required.
            return jsonify(b.errors), 400  # bad request
