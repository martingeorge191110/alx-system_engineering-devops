#!/usr/bin/python3
"""Python script that, using this REST API"""
import json
import requests
from sys import argv


def api_response(api, id):
    user_api = requests.get(f"{api}/users/{id}").json()
    user_tasks_api = requests.get(f"{api}/users/{id}/todos").json()
    json_format = {f"{id}": []}
    username = user_api['username']

    for ele in user_tasks_api:
        json_format[f"{id}"].append(
            {'task': ele['title'],
             'completed': ele['completed'], 'username': username}
        )

    with open(f"{id}.json", "w", encoding="utf-8") as file:
        json.dump(json_format, file, indent=4)


if __name__ == '__main__':

    api_response(
        'https://jsonplaceholder.typicode.com',
        argv[1]
        )
