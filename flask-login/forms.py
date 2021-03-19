from wtforms import Form, BooleanField, PasswordField, validators, TextAreaField, IntegerField,StringField
from wtforms.validators import DataRequired

class LoginForm(Form):
    email = StringField("Email", validators=[validators.Length(min =7, max=50),validators.DataRequired(message="Please Fill this Field")])
    password = PasswordField("Password" ,validators=[validators.DataRequired(message="Please Fill this Field")])



class RegisterForm(Form):
    name = StringField("Ad", validators=[validators.Length(min =3, max=25),validators.DataRequired(message="Please Fill this Field")])
    username = StringField("Username", validators=[validators.Length(min =3, max=25),validators.DataRequired(message="Please Fill this Field")])
    email = StringField("Email", validators=[validators.DataRequired(message="Please Fill this Field")])
    password = PasswordField("Password", validators=[
        validators.DataRequired(message="Please fill this field!"),
        validators.EqualTo(fieldname="confirm",message="Yout passwords Do not match")
    ])
    confirm = PasswordField("confirm Password", validators=[validators.DataRequired(message="Please Fill This Field")])