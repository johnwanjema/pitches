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
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    comment = db.relationship('Comments',backref = 'user',lazy = "dynamic")
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
    pitch_title = db.Column(db.String)
    pitch_upvotes = db.Column(db.Integer)
    pitch = db.Column(db.String)
    pitch_downvotes = db.Column(db.Integer)
    posted = db.Column(db.Time,default=datetime.utcnow())
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    pitch_category = db.Column(db.String)
    comment_id = db.relationship("Comments", backref="pitch", lazy="dynamic")



    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls,id):
        pitches = Pitch.query.filter_by(id=id).all()
        return pitches

    @classmethod
    def get_pitches_by_category(cls,pitch_category):
        pitches = Pitch.query.filter_by(pitch_category = pitch_category).all()
        return pitches

class Comments(db.Model):
    __tablename__ = 'comments'    
    id = db.Column(db. Integer, primary_key=True)
    comment = db.Column(db.String(255))
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    pitch_id = db.Column(db.Integer, db.ForeignKey("pitch.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(self, id):
        comments = Pitch.query.filter_by(pitches_id=id).all()          
        return comments



    

    