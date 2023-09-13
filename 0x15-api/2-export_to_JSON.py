"""
This is a module docstring
This module retrieves employee data from an API and saves it to a JSON file.
"""

import json
import requests
import sys

def get_employee_status(employee_id):
    # Existing code of the function...

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    if not employee_id.isdigit():
        print("Error: employee_id must be a number")
        sys.exit(1)

    get_employee_status(employee_id)