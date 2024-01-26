#!/usr/bin/python3
""" adds a text saying Ci s fun """

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """returns the string Hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """return the string HBNB"""
    return 'HBNB'


@app.route('/c/<text>')
def cis_fun(text):
    """adds a text that says C is fun"""
    text_with_spaces = text.replace('_', ' ')
    return 'C {}'.format(text_with_spaces)


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
