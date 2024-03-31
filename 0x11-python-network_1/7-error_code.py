#!/usr/bin/python3
"""
takes in a URL
sends a request to the URL
displays the body of the response.
"""

import sys

import requests

r = requests.get('http://0.0.0.0:5000')
if r.status_code >= 400:
    print("Error code: {}".format(r.status_code))
else:
    print(r.text)
