#!/usr/bin/python3
"""
takes in a URL,
sends a request to the URL
displays the body of the response (decoded in utf-8).
"""
import sys

from urllib import request, error

try:
        with request.urlopen('http://0.0.0.0:5000') as response:
             body = response.read().decode('utf-8')
             print(body)
except error.HTTPError as error:
             print('Error code:', er.code)
