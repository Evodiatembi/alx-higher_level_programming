#!/usr/bin/python3
"""
takes in a URL,
sends a request to the URL and displays the value
of the X-Request-Id variable found in the header of the response.
"""
import sys
import urllib.request

request = urllib.request.Request('https://alx-intranet.hbtn.io')
with urllib.request.urlopen(request) as response:
     x_request_id = response.getheader('X-Request-Id')
     
