from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import validators

class Submissionform(FlaskForm):
	text = StringField('text',[validators.InputRequired(),validators.Length(min=2,max=50)])
	submit = SubmitField('Tweet')
