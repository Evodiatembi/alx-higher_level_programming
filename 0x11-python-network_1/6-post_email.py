#!/usr/bin/python3
"""takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter, 
and finally displays the body of the response.
"""
import sys
import requests


r = requests.post('http://0.0.0.0:5000', 'hr@holbertonschool.com')
print(r.text)
