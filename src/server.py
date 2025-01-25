import os
from datetime import date
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from forms import ContactForm, AddProjectForm

load_dotenv()

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config['SECRET_KEY'] = os.getenv('APP_SECRET_KEY')
bootstrap = Bootstrap5(app)
ckeditor = CKEditor(app)


@app.context_processor
def inject_year():
    return {'year': date.today().year}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about-me')
def about_me():
    return render_template('about-me.html')


@app.route('/contact-me', methods=['GET', 'POST'])
def contact_me():
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        flash('Message sent successfully')
        # TODO: Add functionality for sending emails
        return render_template('contact-me.html', form=contact_form)
    return render_template('contact-me.html', form=contact_form)


@app.route('/add-project/<login>/<password>', methods=['GET', 'POST'])
def add_project(login, password):
    if login == 'admin' and password == 'admin':  # dummy values. TODO: Change for actual values
        project_form = AddProjectForm()
        if project_form.validate_on_submit():
            flash('Project added successfully')
            return redirect(url_for('index'))   # TODO: Change for projects page
        else:
            return render_template('add-project.html', form=project_form)
    else:
        flash("You don't have permission to add new projects")
        return redirect(url_for('index'))




if __name__ == '__main__':
    app.run(debug=True)
