#!/usr/bin/python3
"""List of states
"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    """display a html page of states from the database
    """
    states_list = storage.all("State").values()
    return render_template("7-states_list.html", states=states_list)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """display the cities of each state
    """
    states_list = storage.all("State").values()
    # print(states_list)
    return render_template("8-cities_by_states.html", states=states_list)


@app.teardown_appcontext
def teardown_sqlalchemy_session(closed):
    """removes the current SQLAlchemy session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
