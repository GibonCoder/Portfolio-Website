from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, length


class ContactForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    content = TextAreaField("Content", validators=[DataRequired(), length(max=400)])
    submit = SubmitField("Send Message")
