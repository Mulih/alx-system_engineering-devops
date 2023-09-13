#!/usr/bin/python3

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

    # Prepare data for JSON
    tasks = []
    for task in todos_data:
        tasks.append({
            "task": task['title'],
            "completed": task['completed'],
            "username": employee_name
        })
    
    data_for_json = {employee_id: tasks}

    # Write to JSON file
    with open('{}.json'.format(employee_id), 'w') as json_file:
        json.dump(data_for_json, json_file)

    return

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Please provide the employee id as a command line argument")
        print("Usage: python3 script.py [EMPLOYEE_ID]")
    else:
        get_employee_status(sys.argv[1])
