#!/usr/bin/python3
"""This script adds another slash and displays just HBNB"""


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


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
