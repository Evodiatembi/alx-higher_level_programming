#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
import requests


r = requests.get("https://alx-intranet.hbtn.io/status")
print("Body response:")
print("\n- type: {}".format(type(r.text)))
print("\n- content: {}".format(r.text))
