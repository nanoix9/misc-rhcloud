#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import flask

app = flask.Flask(__name__)

@app.route('/')
def root():
    return '404'

@app.route('/<path:resource>')
def static_resource(resource):
    return flask.send_from_directory('static', resource)

@app.route('/hello')
def hello():
    return '<h1>Hello World!</h1>'

def main():
    app.run()

if __name__ == '__main__':
    main()
