#!/usr/bin/python3
""" Prints n as a number if n is an integer"""

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


@app.route('/python/')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """A text python is cool"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>')
def print_int(n):
    """Allows to print a number"""
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
