from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer,primary_key = True)
    comment = db.column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    users = db.relationship('User',backref = 'comment',lazy="dynamic")
    def save_review(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_reviews(cls,id):
        comment = Comment.query.filter_by(comment_id=id).all()
        return Comment
    
    def __repr__(self):
      return f'User {self.comment}'




class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)    
    password_hash = db.Column(db.String(255))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitch.id'))
    comment_id = db.Column(db.Integer,db.ForeignKey('comment.id'))

   
    def __repr__(self):
        return f'User {self.username}'


class Pitch(db.Model):
    __tablename__ = 'pitch'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    pitch  = db.column(db.String(255))
    upvote = db.column(db.Integer)
    downvote = db.column(db.Integer)
    users = db.relationship('User',backref = 'pitch',lazy="dynamic")

    def __repr__(self):
        return f'Pitch {self.name}'