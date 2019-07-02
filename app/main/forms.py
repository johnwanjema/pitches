from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,TextAreaField,SelectField
from wtforms.validators import Required,DataRequired
from wtforms import ValidationError
from wtforms.validators import Required,Email,EqualTo
from ..models import Pitch

class PitchForm(FlaskForm):
    pitch_category = SelectField('Pitch Category', coerce=int,
            choices=[(0, 'Please Input your Category...'), (1, 'Interview'),(2, 'pickup_lines'),(3, 'product_pitch'),(4, 'promotion_pitch')],
            validators=[DataRequired()])
    pitch_title = StringField('Pitch title',validators=[Required()])
    pitch = TextAreaField('Pitch',validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('comment',validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')