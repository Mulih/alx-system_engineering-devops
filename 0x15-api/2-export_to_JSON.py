#!/usr/bin/python3
"""
Python script that, using the REST API, exports data in the JSON format.
"""
import json
import requests
import sys

# Endpoints
USERS_URL = "https://jsonplaceholder.typicode.com/users"
TODOS_URL = "https://jsonplaceholder.typicode.com/todos"


def get_employee_status(employee_id):
    """
    Gather employee status from REST API and store it in JSON format.
    """

    # Retrieve user information
    user_response = requests.get(f'{USERS_URL}/{employee_id}')

    # Verify if the request was successful
    if user_response.status_code != 200:
        print('Failed to get user data')
        return
    
    # Retrieve todos for the user
    todos_response = requests.get(TODOS_URL, params={'userId': employee_id})

    if todos_response.status_code != 200:
        print('Failed to get todo data')
        return

    # Parse the responses
    user_data = user_response.json()
    todos_data = todos_response.json()

    # Store user name and ID
    employee_id = user_data['id']
    employee_name = user_data['username']

    # Format data
    tasks_info = [{
        "userId": employee_id,
        "username": employee_name,
        "completed": task["completed"],
        "title": task["title"]
    } for task in todos_data]

    # Write to JSON file
    with open(f'{employee_id}.json', 'w') as jsonfile:
        json.dump(tasks_info, jsonfile)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Please provide the employee id as a command line argument')
        print('Usage: python3 script.py [EMPLOYEE_ID]')
    else:
        # Translate the string argument to integer
        get_employee_status(int(sys.argv[1]))