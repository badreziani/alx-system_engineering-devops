#!/usr/bin/python3
"""Exports data in the CSV format.
"""

if __name__ == "__main__":
    import csv
    import requests
    import sys

    url = "https://jsonplaceholder.typicode.com/users/{}"
    user = requests.get(url.format(sys.argv[1])).json()
    url = "https://jsonplaceholder.typicode.com/users/{}/todos"
    todos = requests.get(url.format(sys.argv[1])).json()
    csv_file = "{}.csv".format(sys.argv[1])
    with open(csv_file, 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=",", quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([sys.argv[1],
                             user.get("username"),
                             todo.get('completed'),
                             todo.get('title')])
