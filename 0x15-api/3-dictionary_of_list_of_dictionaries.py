#!/usr/bin/python3
"""Python script that, using this REST API"""
import json
import requests


def api_response(api):
    users_api = requests.get(f"{api}/users").json()
    all_users = {}

    for ele in users_api:
        id = ele['id']
        username = ele['username']
        tasks_api = f"{api}users/{id}/todos"
        all_tasks = requests.get(tasks_api).json()

        all_users[id] = []
        for task in all_tasks:
            all_users[id].append({
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            })

    with open("todo_all_employees.json", "w", encoding="utf-8") as file:
        json.dump(all_users, file)


if __name__ == '__main__':

    api_response(
        'https://jsonplaceholder.typicode.com'
        )
