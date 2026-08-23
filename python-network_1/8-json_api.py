#!/usr/bin/python3
"""Sends a POST request to search_user with a letter parameter."""
import requests
import sys

if __name__ == "__main__":
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]
    url = "http://0.0.0.0:5000/search_user"
    r = requests.post(url, data={'q': q})
    try:
        data = r.json()
        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
