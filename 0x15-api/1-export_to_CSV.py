#!/usr/bin/python3
"""
Python script that, using REST API, exports data in the CSV format.
"""
import csv
import requests
import sys

# Endpoints
USERS_URL = 'https://jsonplaceholder.typicode.com/users'
TODOS_URL = 'https://jsonplaceholder.typicode.com/todos'


def get_employee_status(employee_id):
    """
    Gather employee status from REST API and store it in CSV format.
    """

    # Retrieve user information
    user_response = requests.get(USERS_URL, params={'id': employee_id})

    # Verify if the request was successful
    if user_response.status_code != 200:
        print('Failed to get the user data')
        return

    # Retrieve todos for the user
    todos_response = requests.get(TODOS_URL, params={'userId': employee_id})

    if todos_response.status_code != 200:
        print('Failed to get the todo data')
        return

    # Parse the response data
    user_data = user_response.json()
    todos_data = todos_response.json()

    # Store user name
    employee_name = user_data[0]['username']

    with open(f'{employee_id}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in todos_data:
            writer.writerow([str(employee_id), employee_name,
                            task['completed'], task['title']])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Please provide the employee id as a command line argument')
        print('Usage: python3 script.py [EMPLOYEE_ID]')
    else:
        # Translate the string argument to integer
        get_employee_status(int(sys.argv[1]))