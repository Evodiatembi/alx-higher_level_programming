#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status using the urlib package
"""
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    content = response.read()
    print("body response:"):
        print("\n- type: {}".format(type(content)))
        print("\n- content: {}".format(content))
        print("\n- utf8 content: {}".format(content.decode('utf-8')))

if __name__ == '__main__':
