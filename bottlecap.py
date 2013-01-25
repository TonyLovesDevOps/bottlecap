# Simple python app to spit out request parameters
from bottle import *
from pprint import pprint
import json
import re
import logging

def print_request_params(request):
  pprint( request )

@get('/')
def respond():
  print_request_params( request.body.read() )
  return "ok"

@post('/')
def print_post():
  print_request_params( request.body.read() )
  
  formdata = request.forms.get('foo')
  print formdata
  if not formdata:
    abort(400, 'No data received')

  return "ok"

@put('/')
def print_put():
  print_request_params( request.body.read() )
  
  return "ok"

run(host='0.0.0.0', port=8071, debug=True)
