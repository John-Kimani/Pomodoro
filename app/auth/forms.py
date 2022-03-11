from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError
# from wtforms.validators import Required,Email,EqualTo
from ..models import registration, postlikes,posts,comment,userprofile

class RegistrationForm(FlaskForm):
    
    def validate_email(self,data_field):
      if registration.query.filter_by(useremail =data_field.data).first():
        raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
      if registration.query.filter_by(username = data_field.data).first():
        raise ValidationError('That username is taken')