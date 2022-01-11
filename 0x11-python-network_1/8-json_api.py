#!/usr/bin/python3
"""script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""

import requests
import sys

if __name__ == "__main__":

    if len(sys.argv) > 0:
        q = sys.argv[1]
    else:
        q = ""

    try:
        url = "http://0.0.0.0:5000/search_user"
        payload = {"q": q}
        req = requests.post(url, payload).json()

        if len(req) > 0:
            print("{[]} {}".format(req.get("id"), req.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
