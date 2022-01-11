#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response."""

import requests
import sys

if __name__ == "__main__":

    req = requests.get(sys.argv[1])

    if req.status_code >= 400:
        print("Error code:", req.status_code)
    else:
        print(req.text)
