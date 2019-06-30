from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    pitch = db.relationship('Pitch',backref = 'user',lazy = "dynamic")
    password_hash = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)


    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.username}'



class Pitch(db.Model):

    __tablename__ = 'pitch'
    id = db.Column(db.Integer,primary_key = True)
    pitch_category = db.Column(db.String)
    pitch_title = db.Column(db.String)
    pitch_upvotes = db.Column(db.Integer)
    pitch = db.Column(db.String)
    pitch_downvotes = db.Column(db.Integer)
    posted = db.Column(db.Time,default=datetime.utcnow())
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))



    def save_review(self):
        db.session.add(self)
        db.session.commit()



    @classmethod
    def get_reviews(cls,id):

        pitches = Pitch.query.filter_by(movie_id=id).all()
        return pitches

