from flask import Blueprint, jsonify, request
from models.store import Store
from models.user import User
from models.booking import Booking
from models.payment import Payment
from playhouse.shortcuts import model_to_dict

bookings_api_blueprint = Blueprint('bookings_api',
                                   __name__,
                                   template_folder='templates')


@bookings_api_blueprint.route('/', methods=["POST"])
def create():
    # CREATE BOOKING
    b = Booking(
        user=request.json.get('user'),
        store=request.json.get('store'),
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
        bookings = Booking.select().where(Booking.user_id == user_id_args)
        if bookings:
            booking_list = []
            for booking in bookings:
                booking_list.append(model_to_dict(booking))
            return jsonify(booking_list)
        else:
            return jsonify({
                'message': "User doesn't exist"
            }), 418  # teapot error

    elif booking_id_args:
        bookings = Booking.select().where(Booking.id == booking_id_args)
        if bookings:
            booking_list = []
            for booking in bookings:
                booking_list.append(model_to_dict(booking))
            return jsonify(booking_list)
        else:
            return jsonify({
                'message': "Booking doesn't exist"
            }), 418  # teapot error
    return jsonify({
        'message': "Wrong argument input"
    }), 418  # teapot error


@bookings_api_blueprint.route('/<b_id>/update/', methods=["GET"])
def update(b_id):
    # bookings/1/update/?status=2
    b = Booking.get_or_none(Booking.id == b_id)

    if b:
        status_args = request.args.get('status')
        if status_args:
            Booking.update(status=status_args).where(
                Booking.id == b).execute()
            return jsonify({
                'message': 'Status has successfully updated'
            })
        else:
            return jsonify({
                'message': "Wrong argument input for status"
            }), 418  # teapot error

    else:
        return jsonify({
            "message": 'No booking id'
        })

        
@bookings_api_blueprint.route('/<id>', methods=["GET"])
def delete(id):
    # work in progress; need to check and ensure this works
    Booking.get_or_none(Booking.id == id).deleteinstance()
    return jsonify({
        'message': "Booking deleted"
    }), 200
