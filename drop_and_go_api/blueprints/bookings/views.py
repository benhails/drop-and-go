from flask import Blueprint, jsonify, request
from models.store import Store
from models.user import User
from models.booking import Booking
from models.payment import Payment
from playhouse.shortcuts import model_to_dict
from app import gateway

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
            'is_success': True,
            'id': b.id,
            'message': "User successfully booked"
        }), 200
    else:
        # the following error doesn't actually work if it's a DB integrity error; can improve error handling here in future if required.
        return jsonify(b.errors), 400  # bad request


@bookings_api_blueprint.route('/inc_payment', methods=["POST"])
def create_inc_payment():
    # CREATE BOOKING & PAYMENT SIMULTANEOUSLY
    try:
        user_id = request.json.get('user')
        amount = request.json.get('price')
        # TO INCLUDE OPTIONAL ITEMS SUCH AS STATUS BELOW THEN WE WOULD NEED TO CONSTRUCT A DICTIONARY AND EXCLUDE COMPLETELY WHEN NOT PRESENT
        b = Booking(
            user=user_id,
            store=request.json.get('store'),
            check_in_date_time=request.json.get('check_in_date_time'),
            check_out_date_time=request.json.get('check_out_date_time'),
            number_of_bag=request.json.get('number_of_bag'),
            price=amount
        )
        b.save()

    except:
        return jsonify({
                'is_success': False,
                'message': "There was an error when trying to create the booking"
            }), 400

    else:
        nonce = request.json.get('nonce')
        result = gateway.transaction.sale({
            "amount": amount,
            "payment_method_nonce": nonce,
            "options": {
            "submit_for_settlement": True
            } 
        })
        if result.is_success:
            try:
                p = Payment(
                    user = user_id,
                    booking = b.id,
                    trans_id = result.transaction.id,
                    amount = amount
                )
                p.save()
                return jsonify({
                    'is_success': True,
                    'booking_id': b.id,
                    'payment_id': p.id,
                    'message': "Booking and payment successfully created and payment sent to Braintree for settlement"
                }), 200
            except: 
                # Booking.get_or_none(Booking.id == b.id).delete_instance()
                return f'Please delete the booking with id:{b.id} manually!', 400  # bad request
        else:
            return jsonify({
                'is_success': False,
                'message': f"The payment to Braintree failed with result:{result} - please delete booking with id:{b.id} manually"
            })


@bookings_api_blueprint.route('/', methods=["GET"])
def show():

    user_id_args = request.args.get('user_id')
    booking_id_args = request.args.get('book_id')

    if user_id_args:
        bookings = Booking.select().where(Booking.user_id == user_id_args).order_by(-Booking.status, Booking.check_in_date_time)
        if bookings:
            booking_list = []
            for booking in bookings:
                booking_list.append(model_to_dict(booking))
            return jsonify(booking_list)
        else:
            return jsonify({
                'is_success': False,
                'message': "User doesn't exist or doesn't have any bookings"
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
                'is_success': False,
                'message': "Booking doesn't exist"
            }), 418  # teapot error
    return jsonify({
        'is_success': False,
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
                'is_success': True,
                'message': 'Status has successfully updated'
            })
        else:
            return jsonify({
                'is_success': False,
                'message': "Wrong argument input for status"
            }), 418  # teapot error

    else:
        return jsonify({
            'is_success': False,
            "message": 'No booking id'
        })

        
@bookings_api_blueprint.route('/<id>', methods=["POST"])
def delete(id):
    Booking.get_or_none(Booking.id == id).delete_instance()
    return jsonify({
        'is_success': True,
        'message': "Booking deleted"
    }), 200
