from flask import render_template, request, redirect, url_for,abort
from . import main
from .. import db
from .forms import PitchForm,CommentForm
from flask import render_template, flash,request
from flask import render_template,redirect,url_for
from ..models import User,Pitch,Comments
from .. import db
from flask_login import login_user,logout_user,login_required,current_user



@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    title = "pitches"
    return render_template('index.html',title = title )


@main.route('/pitches')
@login_required
def pitches():
    pitches =  Pitch.query.all()
    interview_pitch = Pitch.get_pitches_by_category('1')
    pickup_lines = Pitch.get_pitches_by_category('2')
    product_pitch = Pitch.get_pitches_by_category('3')
    promotion_pitch = Pitch.get_pitches_by_category('4')  
    if pitches is None:
        return redirect(url_for('main.pitch'))
        title = "pitches"
    return render_template("pitch.html", pitches = pitches, interviews = interview_pitch, pickups = pickup_lines,products = product_pitch,promotions = promotion_pitch )


@main.route('/pitch', methods = ['GET','POST'])
@login_required
def pitch():  

    form = PitchForm()
    if form.validate_on_submit():
        pitch = Pitch(pitch = form.pitch.data, user_id = current_user.id,pitch_title = form.pitch_title.data,pitch_category = form.pitch_category.data ,pitch_upvotes = 0, pitch_downvotes = 0)
        db.session.add(pitch)
        db.session.commit()
        return redirect(url_for('main.index'))
        title = "pitches"
    return render_template('new_pitch.html',pitch_form = form)

@main.route('/comment/<int:id>', methods=['GET', 'POST'])
@login_required
def post_comment(id):
    
    form = CommentForm()
    title = 'post comment'
    pitches = Pitch.query.filter_by(id=id).first()
    comments = Comments.query.filter_by().all()

    if pitches is None:
         abort(404)

    if form.validate_on_submit():
        comment = form.comment.data
        new_comment = Comments( comment = comment, user_id = current_user.id, pitch_id = pitches.id)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('main.pitches'))

    return render_template('post_comment.html', comment_form=form, title=title,comments=comments , pitches = pitches)

@main.route('/user/<uname>/<int:id>')
def profile(uname,id):
    user = User.query.filter_by(username = uname).first()
    pitches = Pitch.query.filter_by(user_id=id)
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user , pitches = pitches)


