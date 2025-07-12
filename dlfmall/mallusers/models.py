# users/models.py
from mongoengine import Document, StringField,IntField

class UserDetails(Document):
    name = StringField(required=True)
    email = StringField(required=True)
    mobile = IntField(required=True)
    address = StringField()

    meta = {'collection': 'user_details'}
