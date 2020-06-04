import flask
from apps import db


class User(db.Document):
    user_id = db.IntField(unique=True)
    first_name = db.StringField(max_length=30)
    last_name = db.StringField(max_length=30)
    email = db.StringField(max_length=30)
    password = db.StringField(max_length=30)


class Course(db.Document):
    course_id = db.StringField(max_length=30,unique=True)
    title = db.StringField(max_length=30)
    description = db.StringField(max_length=30)
    credits = db.StringField(max_length=30)
    term = db.StringField(max_length=30)


class Enrollment(db.Document):
    user_id = db.IntField(unique=True)
    course_id = db.StringField(max_length=30, unique=True)
