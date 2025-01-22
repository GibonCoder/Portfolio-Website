from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    content = StringField("Content", validators=[DataRequired()])
    submit = SubmitField("Send Message")
