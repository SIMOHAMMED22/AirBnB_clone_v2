#!/usr/bin/python3
"""12. HBNB is alive!"""


from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_appcontext(response_or_exc):
    """ """
    storage.close()


@app.route("/hbnb")
def hbnb():
    """State, City, Amenity and Place objects must be loaded from DBStorage"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    pls = storage.all(Place)
    usrs = storage.all(User)

    return render_template('100-hbnb.html',
                           state=states.values(),
                           amenity=amenities.values(),
                           places=pls.values(),
                           users=usrs.values())



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
