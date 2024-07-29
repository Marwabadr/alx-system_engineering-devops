#!/usr/bin/python3
import requests
import sys

def fetch_employee_data(employee_id):
    try:
        # Fetch user details
        user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
        user_response.raise_for_status()
        user_data = user_response.json()

        # Fetch todo list for the user
        todos_response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        return user_data, todos_data

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    return None, None

def display_todo_progress(employee_id):
    user_data, todos_data = fetch_employee_data(employee_id)
    if user_data is None or todos_data is None:
        return

    employee_name = user_data.get('name')
    completed_tasks = [task for task in todos_data if task.get('completed')]
    total_tasks = len(todos_data)
    number_of_done_tasks = len(completed_tasks)

    # Display the summary line
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")

    # Display each completed task title
    for task in completed_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            display_todo_progress(employee_id)
        except ValueError:
            print("Please provide a valid integer as employee ID.")

