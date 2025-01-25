from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, EmailField, SubmitField, Label
from wtforms.validators import DataRequired, Email, length
from flask_ckeditor import CKEditorField


class ContactForm(FlaskForm):
    title = StringField("Title", default="Contact request")
    email = EmailField("*Email", validators=[DataRequired(), Email("Please enter a valid email address")])
    content = TextAreaField("*Message", validators=[DataRequired(), length(max=400)])
    submit = SubmitField("Send Message")


class AddProjectForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    link = StringField("GitHub Link", validators=[DataRequired()])
    description = CKEditorField("Description", validators=[DataRequired()])
    submit = SubmitField("Add Project")
