from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap5

app = Flask(__name__, template_folder='../templates', static_folder='../static')
bootstrap = Bootstrap5(app)


@app.get('/')
def hello():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
