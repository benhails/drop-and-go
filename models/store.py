from models.base_model import BaseModel
from models.user import User
import peewee as pw
# from helpers import s3
# from config import S3_BUCKET, S3_LOCATION, S3_PROFILE_IMAGE_FOLDER
# from playhouse.hybrid import hybrid_property


class Store(BaseModel):

    # DEFAULTS unique=False, null=False
    name = pw.CharField()
    building_number = pw.CharField()
    street_name = pw.CharField()
    city = pw.CharField()
    country = pw.CharField()
    location_index = pw.IntegerField()
    postal_zip_code = pw.CharField()
    area = pw.CharField(null=True, default='')
    nearby = pw.CharField(null=True, default='')
    nearby2 = pw.CharField(null=True, default='')
    opening_hours = pw.CharField(null=True, default='')
    store_image = pw.CharField(null=True, 
        default='http://nextagram-syafiq.s3.amazonaws.com/store_default.png')
    owner = pw.ForeignKeyField(User, backref='stores')
    price = pw.IntegerField(null=True, default=0)
    star_rating = pw.IntegerField(null=True, default=5)
    operating_day = pw.CharField(null=True, default='')

    def validate(self):
        pass
