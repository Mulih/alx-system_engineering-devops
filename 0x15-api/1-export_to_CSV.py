#!/usr/bin/python3

import json
import requests
import sys
import csv

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

    # Prepare data for CSV
    data_for_csv = []
    for task in todos_data:
        data_for_csv.append([employee_id, employee_name, task['completed'], task['title']])
    
    # Write data to CSV file
    with open('{}.csv'.format(employee_id), 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(data_for_csv)

    return

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Please provide the employee id as a command line argument")
        print("Usage: python3 script.py [EMPLOYEE_ID]")
    else:
        get_employee_status(sys.argv[1])
