import os
from datetime import date
from dotenv import load_dotenv
from flask import Flask, render_template, url_for, flash
from flask_bootstrap import Bootstrap5
from forms import ContactForm

load_dotenv()

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config['SECRET_KEY'] = os.getenv('APP_SECRET_KEY')
bootstrap = Bootstrap5(app)


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


if __name__ == '__main__':
    app.run(debug=True)
