from models.base_model import BaseModel
from models.user import User
from models.store import Store
from enum import Enum
import peewee as pw
# from helpers import s3
# from config import S3_BUCKET, S3_LOCATION, S3_PROFILE_IMAGE_FOLDER
# from playhouse.hybrid import hybrid_property


class Booking(BaseModel):
    class BookingType(Enum):
        CONFIRMED = 1
        CHECKED_IN = 2
        COMPLETE = 3

    user = pw.ForeignKeyField(User, backref='bookings')
    store = pw.ForeignKeyField(Store, backref='bookings')
    check_in_date_time = pw.DateTimeField()
    check_out_date_time = pw.DateTimeField()
    number_of_bag = pw.IntegerField()
    price = pw.IntegerField()
    status = pw.IntegerField(default=BookingType.CONFIRMED.value)
    # payment = pw.ForeignKeyField(User, backref='payments')

    def validate(self):
        pass
