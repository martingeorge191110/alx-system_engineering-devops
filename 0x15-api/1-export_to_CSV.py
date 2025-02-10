#!/usr/bin/python3
"""Python script that, using this REST API"""
import csv
import requests
from sys import argv


def api_response(api, id):
    user_api = requests.get(f"{api}/users/{id}").json()
    user_tasks_api = requests.get(f"{api}/users/{id}/todos").json()
    csv_format = []
    username = user_api['username']

    for ele in user_tasks_api:
        csv_format.append([id, username,
                           ele['completed'], ele['title']
                           ])

    with open(f"{id}.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file, quoting=1)

        for e in csv_format:
            writer.writerow(e)


if __name__ == '__main__':

    api_response(
        'https://jsonplaceholder.typicode.com',
        argv[1]
        )
