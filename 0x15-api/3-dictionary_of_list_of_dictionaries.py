#!/usr/bin/python3
"""Returns information about his/her TODO list progress.
"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(url).json()
    url = "https://jsonplaceholder.typicode.com/todos"
    todos = requests.get(url).json()
    with open("todo_all_employees.json", "w") as json_file:
        data = {user.get("id"): [{'task': todo.get('title'),
                                  'completed': todo.get('completed'),
                                  'username': user.get('username')
                                  } for todo in todos
                                 if user.get("id") == todo.get('userId')]
                for user in users}
        json.dump(data, json_file)
