from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,TextAreaField
from wtforms.validators import Required
from wtforms import ValidationError
from wtforms.validators import Required,Email,EqualTo
from ..models import Pitch

class PitchForm(FlaskForm):

    name = StringField('Pitch title',validators=[Required()])
    pitch = TextAreaField('your pitch')    
    submit = SubmitField('Submit')
