from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class RegisterForm(FlaskForm):
    user1 = StringField(label='Player 1')
    user2 = StringField(label='Player 2')
    selected_string = StringField(label='Enter user2')
    submit = SubmitField(label='Start Game')


class Proceed(FlaskForm):
    submit = SubmitField(label='Proceed')


class Scenario(FlaskForm):
    submit1 = SubmitField(label='Formal')
    submit2 = SubmitField(label='Informal')
    submit3 = SubmitField(label='Public Speaking')
    submit4 = SubmitField(label='Any')


class Guess1(FlaskForm):
    chance1 = StringField(label='Take a Guess')
    submit = SubmitField(label='Verify')


class GetWord(FlaskForm):
    word = StringField('getword')
    submit = SubmitField('submit')
