from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, EmailField, SubmitField, Label
from wtforms.validators import DataRequired, Email, length


class ContactForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    email = EmailField("*Email", validators=[DataRequired(), Email("Please enter a valid email address")])
    content = TextAreaField("*Message", validators=[DataRequired(), length(max=400)])
    submit = SubmitField("Send Message")
