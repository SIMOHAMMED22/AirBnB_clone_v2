#!/usr/bin/python3
"""5. Number template"""


from flask import Flask
from flask import render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """print hello"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """Display HBNB"""
    return "HBNB"


@app.route("/c/<text>")
def c(text):
    """Display C followed by the value of the text"""
    return f"C {text.replace('_', ' ')}"


@app.route("/python/", defaults={'text': 'is cool'})
@app.route("/python/<text>")
def py(text):
    """Display Python followed by the value of the text"""
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>")
def number(n):
    """Display “n is a number” only if n is an integer"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>")
def number_temp(n):
    """Display a HTML page only if n is an integer"""
    return render_template('5-number.html', number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
