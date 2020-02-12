from models.base_model import BaseModel
from models.user import User
from models.store import Store
import peewee as pw
# from helpers import s3
# from config import S3_BUCKET, S3_LOCATION, S3_PROFILE_IMAGE_FOLDER
# from playhouse.hybrid import hybrid_property


class Booking(BaseModel):
    class BookingType(Enum):
        CONFIRMED = 1
        CHECKED_IN = 2
        COMPLETE = 3

    user_id = pw.ForeignKeyField(User, backref='users')
    store_id = pw.ForeignKeyField(Store, backref='stores')
    payment_id = pw.ForeignKeyField(User, backref='payments')
    check_in_date_time = pw.DateTimeField()
    check_out_date_time = pw.DateTimeField()
    number_of_bags = pw.IntegerField()
    price = pw.IntegerField()
    total_price = pw.IntegerField()
    status = pw.IntegerField(default=BookingType.CONFIRMED.value)

    def validate(self):
        pass
