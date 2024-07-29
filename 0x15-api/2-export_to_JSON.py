#!/usr/bin/python3
"""Exports data in the CSV format.
"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    url = "https://jsonplaceholder.typicode.com/users/{}"
    user = requests.get(url.format(sys.argv[1])).json()
    url = "https://jsonplaceholder.typicode.com/users/{}/todos"
    todos = requests.get(url.format(sys.argv[1])).json()
    csv_file = "{}.csv".format(sys.argv[1])
    data = {}
    uid = sys.argv[1]
    with open("{}.json".format(uid), "w") as json_file:
        json.dump({uid: [{
            'task': todo.get('title'),
            'completed': todo.get('completed'),
            'username': user.get('username')
            } for todo in todos]}, json_file)
