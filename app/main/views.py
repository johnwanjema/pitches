from flask import render_template, request, redirect, url_for,abort
from . import main
from .. import db

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = "pitches"
    return render_template('index.html',title = title)
