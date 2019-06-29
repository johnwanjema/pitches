from flask import render_template, request, redirect, url_for,abort
from . import main
from .. import db
from .forms import RegistrationForm,LoginForm
from flask import render_template, flash,request
from flask import render_template,redirect,url_for
from ..models import User
from .forms import RegistrationForm
from .. import db
from flask_login import login_user,logout_user,login_required



@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = "pitches"
    return render_template('index.html',title = title)


