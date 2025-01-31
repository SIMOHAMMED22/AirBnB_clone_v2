#!/usr/bin/python3
""" script that starts a Flask web application. """


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb')
def display_hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<path:text>', strict_slashes=False)
def display_python(text):
    text = text.replace('_', ' ')
    return f'Python {text}'


@app.route('/number/<int:n>')
def display_number(n):
    if isinstance(n, int):
        return f'{n} is a number'


@app.route('/number_template/<int:n>')
def display_number_template(n):
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_number_odd_or_even(n):
    if isinstance(n, int):
        result = 'even' if n % 2 == 0 else 'odd'
        return render_template("6-number_odd_or_even.html", n=n, ntyp=result)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000
    )
