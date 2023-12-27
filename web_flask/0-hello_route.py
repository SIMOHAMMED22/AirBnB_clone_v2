#!/usr/bin/python3
""" script that starts a Flask web application. """

from flask import Flask

app = Flask(__name__)


# Route definition
@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB!'


if __name__ == '__main__':
    # Running the Flask app on 0.0.0.0, port 5000
    app.run(host='0.0.0.0', port=5000)
