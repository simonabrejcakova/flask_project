from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash


db = SQLAlchemy()

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    html_render = db.Column(db.String)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    

class Newsletter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)


class Manual(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    html_render = db.Column(db.String)


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    html_render = db.Column(db.String)


class Shifts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String)
    truck= db.Column(db.String)
    date= db.Column(db.String)
    start_time= db.Column(db.String)
    end_time= db.Column(db.String)
    notes=db.Column(db.String)

class Shift(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String)
    typ=db.Column(db.String)
    truck= db.Column(db.String)
    date= db.Column(db.String)
    start_time= db.Column(db.String)
    end_time= db.Column(db.String)
    notes=db.Column(db.String)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    html_render = db.Column(db.String)