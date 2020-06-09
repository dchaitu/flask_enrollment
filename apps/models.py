import flask
from apps import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Document):
    user_id = db.IntField(unique=True)
    first_name = db.StringField(max_length=30)
    last_name = db.StringField(max_length=30)
    email = db.StringField(max_length=30,unique=True)
    password = db.StringField()

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def get_password(self, password):
        return check_password_hash(self.password, password)


class Course(db.Document):
    courseID = db.StringField(max_length=10, unique=True)
    title = db.StringField(max_length=30)
    description = db.StringField(max_length=200)
    credits = db.IntField()
    term = db.StringField(max_length=30)


class Enrollment(db.Document):
    user_id = db.IntField()
    courseID = db.StringField(max_length=30)
