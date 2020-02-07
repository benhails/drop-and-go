from models.base_model import BaseModel
import peewee as pw
from werkzeug.security import generate_password_hash
# from helpers import s3
# from config import S3_BUCKET, S3_LOCATION, S3_PROFILE_IMAGE_FOLDER
# from playhouse.hybrid import hybrid_property
from enum import Enum


class User(BaseModel):
    class UserType(Enum):
        STORE_OWNER = 1
        CUSTOMER    = 2

    # DEFAULTS unique=False, null=False
    name = pw.CharField(null=True, default='')
    user_type = pw.IntegerField(default=UserType.CUSTOMER.value) 
    email = pw.CharField(unique=True)
    password = pw.CharField()
    image = pw.CharField(unique=False, null=True, default='')
    

    def validate(self):
        pass