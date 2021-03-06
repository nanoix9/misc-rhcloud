#!/usr/bin/python
import os

virtenv = os.environ.get('OPENSHIFT_PYTHON_DIR', '.') + '/virtenv/'
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass

from flaskapp import app as application

#
# Below for testing only
#
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    port = 8051
    httpd = make_server('', port, application)
    print "Serving HTTP on port %d..." % port
    # Wait for a single request, serve it and quit.
    #httpd.handle_request()
    httpd.serve_forever()
