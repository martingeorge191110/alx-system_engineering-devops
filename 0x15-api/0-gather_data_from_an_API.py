#!/usr/bin/python3
"""Python script that, using this REST API"""
import requests
from sys import argv


def api_response(api, id):
    user_api = requests.get(f"{api}/users/{id}").json()
    user_tasks_api = requests.get(f"{api}/users/{id}/todos").json()
    user_done_tasks_api = requests.get(
        f"{api}/users/{id}/todos?completed=true").json()
    no_tasks = len(user_tasks_api)
    no_done = len(user_done_tasks_api)

    print(f"Employee {user_api['name']} is done with tasks"
          f"({no_done}/{no_tasks}):")

    for ele in user_done_tasks_api:
        print(f"\t {ele['title']}")


if __name__ == '__main__':

    api_response(
        'https://jsonplaceholder.typicode.com',
        argv[1]
        )
