#!/usr/bin/python3
"""10. States and State"""


from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_appcontext(response_or_exc):
    """ """
    storage.close()


@app.route("/states")
def states_list():
    """list of all State objects present in DBStorage sorted by name"""
    sts = storage.all(State)
    return render_template('9-states.html', states=sts)


@app.route("/states/<id>")
def state(id):
    """list of City objects linked to the State sorted by name"""
    sts = storage.all(State)
    for st in sts.values():
        if st.id == id:
            return render_template('9-states.html', state=st)
    return render_template('9-states.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
