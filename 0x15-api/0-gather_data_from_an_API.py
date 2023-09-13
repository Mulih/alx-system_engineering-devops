#!/usr/bin/python3
"""
This is a module docstring
This module using this REST API, for a given employee ID, 
returns information about his/her TODO list progress.
"""
import json
import requests
import sys

def get_employee_status(employee_id):

    # Using the requests module to make the http GET request
    user_response = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))
    todos_response = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id))

    # Check the status code of the response to make sure the GET request was successful
    if user_response.status_code != 200:
        print("Failed to get the user data")
        return
    
    if todos_response.status_code != 200:
        print("Failed to get the todo data")
        return

    # Parse the response text into Python Dictionary
    user_data = user_response.json()
    todos_data = todos_response.json()

    # Getting the employee's name
    employee_name = user_data['name']

    # Filter the todos data for tasks that are completed
    completed_task = [task for task in todos_data if task['completed'] ]

    # Printing the details
    print(f"Employee {employee_name} is done with tasks({len(completed_task)}/{len(todos_data)}):")

    for task in completed_task:
        print("\t", task['title'])

    return

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Please provide the employee id as a command line argument")
        print("Usage: python3 script.py [EMPLOYEE_ID]")
    else:
        get_employee_status(sys.argv[1])
