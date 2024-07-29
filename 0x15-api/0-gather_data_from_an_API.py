#!/usr/bin/python3
"""Returns information about his/her TODO list progress.
"""

if __name__ == "__main__":
    import requests
    import sys

    url = "https://jsonplaceholder.typicode.com/users/{}"
    user = requests.get(url.format(sys.argv[1])).json()
    url = "https://jsonplaceholder.typicode.com/users/{}/todos"
    todos = requests.get(url.format(sys.argv[1])).json()
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"),
        len([t for t in todos if t.get("completed")]),
        len(todos)))
    for todo in todos:
        print("    {}".format(todo.get("title")))
