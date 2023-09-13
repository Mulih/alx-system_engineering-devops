#!/usr/bin/python3
"""
Python script that, using a REST API, records all tasks from all employees
and writes them to a JSON file.
"""

import json
import requests


def main():
    """
    Fetches data from the REST API and writes it to a JSON file.
    """
    api_url = "https://jsonplaceholder.typicode.com/"
    all_employees_tasks = {}

    for USER_ID in range(1, 11):  # Replace with the range of employee IDs you require
        employee_todo = requests.get(api_url + f"todos?userId={USER_ID}").json()
        employee = requests.get(api_url + f"users/{USER_ID}").json()

        task_list = [{"username": employee["username"], "task": task["title"], "completed": task["completed"]} for task in employee_todo]
        all_employees_tasks[str(USER_ID)] = task_list

    with open("todo_all_employees.json", "w") as f:
        json.dump(all_employees_tasks, f)


if __name__ == "__main__":
    main()
