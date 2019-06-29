from flask import render_template, request, redirect, url_for,abort
from . import main
from .. import db
from .forms import PitchForm
from flask import render_template, flash,request
from flask import render_template,redirect,url_for
from ..models import User,Pitch

from .. import db
from flask_login import login_user,logout_user,login_required



@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = "pitches"
    return render_template('index.html',title = title)

@main.route('/pitch')
@login_required
def pitch():  

    '''
    View movie page function that returns the movie details page and its data
    '''
    form = PitchForm()
    if form.validate_on_submit():
           

        # Updated pitch instance
        new_pitch = Pitch(pitch = form.pitch.data,name = form.name.data)

        #   save pitch method
        # new_pitch.save_pitch()
        # return redirect(url_for('.',id = movie.id ))

    title = "pitches"
    return render_template('pitch.html',pitch_form = form)


