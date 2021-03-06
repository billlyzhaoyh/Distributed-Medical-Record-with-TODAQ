from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    name = StringField('Patient name',
                           validators=[DataRequired()])
    date = StringField('Date',
                        validators=[DataRequired()])
    symptom = StringField('Symptoms', validators=[DataRequired()])

    diagnosis = StringField('Diagnosis', validators=[DataRequired()])

    prescription = StringField('Prescription', validators=[DataRequired()])

    image = FileField('Medical certificate', validators=[DataRequired()])

    # confirm_password = PasswordField('Confirm Password',
    #                                  validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit appointment details')
