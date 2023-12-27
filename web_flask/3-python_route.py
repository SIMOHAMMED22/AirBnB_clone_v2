#!/usr/bin/python3
from flask import Flask
from werkzeug.utils import escape
"""
    This is a multi-line comment describing the purpose of the class.
    It can span multiple lines and is enclosed within triple quotes.
    """

app = Flask(__name__)


# Route definitions
@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text='is_cool'):
    text = text.replace('_', ' ')
    return f'C {escape(text)}'


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    text = text.replace('_', ' ')
    return f'Python {escape(text)}'


if __name__ == '__main__':
    # Running the Flask app on 0.0.0.0, port 5000
    app.run(host='0.0.0.0', port=5000)
