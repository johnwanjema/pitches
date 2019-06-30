from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,TextAreaField
from wtforms.validators import Required
from wtforms import ValidationError
from wtforms.validators import Required,Email,EqualTo
from ..models import Pitch

class PitchForm(FlaskForm):
    pitch_category = StringField('Pitch Category',validators=[Required()])
    pitch_title = StringField('Pitch title',validators=[Required()])
    pitch = TextAreaField('Pitch',validators=[Required()])
    submit = SubmitField('Submit')
