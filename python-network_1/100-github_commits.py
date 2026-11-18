#!/usr/bin/python3
import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])
    response = requests.get(url, params={"per_page": 10})
    for commit in response.json()[:10]:
        author = commit.get("commit").get("author").get("name")
        print("{}: {}".format(commit.get("sha"), author))
