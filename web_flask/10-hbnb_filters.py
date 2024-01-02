#!/usr/bin/python3
"""11. HBNB filters"""


from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_appcontext(response_or_exc):
    """ """
    storage.close()


@app.route("/hbnb_filters")
def states_list():
    """list of all State objects present in DBStorage sorted by name"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html',
                           state=states.values(),
                           amenity=amenities.values())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
