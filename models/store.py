from models.base_model import BaseModel
from models.user import User
import peewee as pw
# from helpers import s3
# from config import S3_BUCKET, S3_LOCATION, S3_PROFILE_IMAGE_FOLDER
# from playhouse.hybrid import hybrid_property


class Store(BaseModel):

    # DEFAULTS unique=False, null=False
    price = pw.IntegerField(null=True, default='')
    star_rating = pw.IntegerField(null=True, default=5)
    operating_day = pw.CharField(null=True, default='')
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
    store_image = pw.CharField(
        default='https://lh3.googleusercontent.com/proxy/NjslLpx0TARRoIGk9d47DNO-jCpvf_puajCcY6pxgq2tnc0xNA-VtikFEytFbDwxqa1Yur_8oRi6oSZ0-HpY8NvOVCf6kIJg9-1VGO3tftiqUyZKeztX29eVw9y3c9SGFx0')
    owner = pw.ForeignKeyField(User, backref='stores', default=1)

    def validate(self):
        pass
