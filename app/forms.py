from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, SubmitField, validators

class ContactForm(FlaskForm):
    name = StringField("Name", [validators.InputRequired("Please enter your full name."), validators.length(max=32)])
    email = EmailField("E-mail", [validators.InputRequired("Please enter your e-mail address."), validators.Email()])
    subject = StringField("Subject", [validators.InputRequired("Please enter the subject for your message."), validators.length(max=256)])
    message = TextAreaField("Message", [validators.InputRequired("Please enter the message you would like to send.")])
    submit = SubmitField("Send")
