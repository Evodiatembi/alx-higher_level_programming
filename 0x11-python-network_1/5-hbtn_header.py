#!/usr/bin/python3
"""
takes in a URL, 
sends a request to the URL and displays the value of the variable X-Request-Id in the response header
"""
import sys

import requests

    r = requests.get('https://alx-intranet.hbtn.io')
    print(r.headers.get("X-Request-Id"))
