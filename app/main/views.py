from flask import render_template, request, redirect, url_for,abort
from . import main
from .. import db
from .forms import PitchForm
from flask import render_template, flash,request
from flask import render_template,redirect,url_for
from ..models import User,Pitch
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


    if pitch is None:
        abort(404)
    title = "pitches"
    return render_template("pitch.html", pitches = pitches )


@main.route('/pitch', methods = ['GET','POST'])
@login_required
def pitch():  

    form = PitchForm()
    if form.validate_on_submit():
        pitch = Pitch(pitch = form.pitch.data,pitch_title = form.pitch_title.data,pitch_category = form.pitch_category.data ,pitch_upvotes = 0, pitch_downvotes = 0)
        db.session.add(pitch)
        db.session.commit()
        return redirect(url_for('main.index'))
        title = "pitches"
    return render_template('new_pitch.html',pitch_form = form)

    


