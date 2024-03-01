from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired

class ImageForm(FlaskForm):
    photo = FileField("Photo", validators=[DataRequired()])
    submit = SubmitField("Find")

