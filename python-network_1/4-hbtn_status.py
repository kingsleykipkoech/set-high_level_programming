#!/usr/bin/python3
"""Fetches status using requests with fallback."""
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    try:
        r = requests.get(url)
    except Exception:
        url = "https://intranet.hbtn.io/status"
        r = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
