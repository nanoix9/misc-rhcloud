#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import flask

app = flask.Flask(__name__)

@app.route('/')
def root():
    return '404 Not Found'

@app.route('/hello')
def hello():
    return '<h1>Hello World!</h1>'

@app.route('/rzrq')
def rzrq():
    return flask.redirect('/static/html/rzrq.html')

##################

#@app.route('/lib/<path:resource>')
#def lib(resource):
#    return flask.send_from_directory('lib', resource)

@app.route('/test/<path:path>')
def test(path):
    return 'Test: ' + path

#@app.route('/<path:resource>')
#def static_resource(resource):
#    return flask.send_from_directory('static', resource)

def main():
    with app.test_request_context():
        print flask.url_for('rzrq')
    app.run()

if __name__ == '__main__':
    main()
