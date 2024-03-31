#!/usr/bin/python3
"""
takes in a URL
sends a POST request to the passed URL
takes email as a parameter
displays the body of the response
"""
import sys

import urllib.request

request = urllib.request.Request('http://0.0.0.0:5000', data)
with urllib.request.urlopen(request) as response:
     response_body = response.read().decode('utf-8')
     send_post_request('http://0.0.0.0:5000','hr@holbertonschool.com')
