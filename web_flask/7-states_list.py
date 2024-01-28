#!/usr/bin/python3
"""starts web application with two routings"""

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states_list')
def states_list():
    """Renders template with states"""
    html_file = '7-states_list.html'
    states = storage.all(State)
    sort_states = sorted(states.values(), key=lambda state: state.name)
    return render_template(html_file, sort_states=sort_states)


@app.teardown_appcontext
def app_teardown(arg=None):
    """Clean up session"""
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
