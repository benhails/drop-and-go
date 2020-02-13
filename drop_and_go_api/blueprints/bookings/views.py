from flask import Blueprint, jsonify, request
from models.store import Store
from models.user import User
from models.booking import Booking
from playhouse.shortcuts import model_to_dict

bookings_api_blueprint = Blueprint('bookings_api',
                                   __name__,
                                   template_folder='templates')


@bookings_api_blueprint.route('/', methods=["POST"])
def create():
    # CREATE BOOKING
    b = Booking(
        user=request.json.get('user_id'),
        store=request.json.get('store_id'),
        check_in_date_time=request.json.get('check_in_date_time'),
        check_out_date_time=request.json.get('check_out_date_time'),
        number_of_bag=request.json.get('number_of_bag'),
        price=request.json.get('price'),
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


@bookings_api_blueprint.route('/', methods=["GET"])
def show():

    user_id_args = request.args.get('user_id')
    booking_id_args = request.args.get('book_id')

    if user_id_args:
        booking = Booking.get_or_none(Booking.user_id == user_id_args)

        if booking:
            return jsonify(model_to_dict(booking))
        else:
            return jsonify({
                'message': "User doesn't exist"
            }), 418  # teapot error

    elif booking_id_args:
        booking = Booking.get_or_none(Booking.id == booking_id_args)
        if booking:
            return jsonify(model_to_dict(booking))
        else:
            return jsonify({
                'message': "Booking doesn't exist"
            }), 418  # teapot error
    return jsonify({
        'message': "Wrong argument input"
    }), 418  # teapot error

    # # GET THE BOOKING BASED ON ID
    # show            / <id >

    # # GET BOOKING BASED ON USER ID
    # show         bookings?user_id = <id>
    #    /user/<id >
