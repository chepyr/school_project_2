from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired


class GetPointsForm(FlaskForm):
    points = TextAreaField('Точки', validators=[DataRequired()])
    submit = SubmitField('Найти')
