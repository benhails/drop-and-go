from models.base_model import BaseModel
from models.user import User
from models.booking import Booking
import peewee as pw


class Payment(BaseModel):

    # DEFAULTS unique=False, null=False
    user = pw.ForeignKeyField(User, backref='payments')
    booking = pw.ForeignKeyField(Booking, backref='payments')
    trans_id = pw.CharField(null=True, default='')
    currency = pw.CharField(default='MYR')
    amount = pw.IntegerField()
    
    
    def validate(self):
        pass
