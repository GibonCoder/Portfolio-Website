import os
from datetime import date
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
# Forms import from forms.py
from forms import ContactForm, AddProjectForm
# Db and models import from models.py
from models import db, Project
# Contact Model import
from mailer import Mailer

load_dotenv()

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config['SECRET_KEY'] = os.getenv('APP_SECRET_KEY')

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')

# Mail configuration
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')


# Initialize mailer
mailer = Mailer(app)

# Initialize bootstrap and ckeditor
bootstrap = Bootstrap5(app)
ckeditor = CKEditor(app)
db.init_app(app)

# Create database
with app.app_context():
    db.create_all()


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


@app.route('/projects')
def get_all_projects():
    res = db.session.execute(db.select(Project))
    projects = res.scalars().all()
    return render_template('projects.html', projects=projects)


@app.route('/project/<int:project_id>')
def get_project(project_id):
    requested_project = db.get_or_404(Project, project_id)
    return render_template('project.html', project=requested_project)


@app.route('/add-project/<login>/<password>', methods=['GET', 'POST'])
def add_project(login, password):
    if login == 'admin' and password == 'admin':  # dummy values. TODO: Change for actual values (actual identification)
        project_form = AddProjectForm()
        if project_form.validate_on_submit():
            new_project = Project(
                title=project_form.title.data,
                gh_link=project_form.link.data,
                description=project_form.description.data
            )
            db.session.add(new_project)
            db.session.commit()
            flash('Project added successfully')
            return redirect(url_for('get_all_projects'))
        else:
            return render_template('add-project.html', form=project_form)
    else:
        flash("You don't have permission to add new projects")
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
