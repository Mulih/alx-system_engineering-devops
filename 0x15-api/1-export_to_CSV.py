#!/usr/bin/python3
"""
Check student .CSV output of user information
"""

import csv
import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users?id="
todos_url = "https://jsonplaceholder.typicode.com/todos"


def user_info(id):
    """ Check user information """

    total_tasks = 0
    response = requests.get(todos_url).json()
    for i in response:
        if i['userId'] == id:
            total_tasks += 1

    response = requests.get(users_url + str(id)).json()
    username = response[0]['username']

    flag = 0
    with open(str(id) + ".csv", 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:
            if not row:  # ignore empty lines
                continue
            if str(id) != row[0]:  # assuming User ID is the first field
                print("User ID: Incorrect / ", end='')
                flag = 1
            if username != row[1]:  # assuming Username is the second field
                print("Username: Incorrect")
                flag = 1

    if flag == 0:
        print("User ID and Username: OK")


if __name__ == "__main__":
    user_info(int(sys.argv[1]))