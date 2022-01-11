#!/usr/bin/python3
"""script that takes your Github credentials (username and password) and uses
the Github API to display your id"""

import requests
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    pssword = sys.argv[2]
    url = "https://api.github.com/user"

    req = requests.get(url, auth=(user, pssword))
    req_json_rep = req.json()

    print(req_json_rep.get("id", "None"))
