from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

class rollForm(FlaskForm):
    numberDice = IntegerField('Number of Dice')
    roll = SubmitField('Roll!')
