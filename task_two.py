# Data Storage
# Objective:
# Store the retrieved data locally, simulating basic data persistence without the need for a full-fledged database.


import requests
import json

def get_todos():
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve todos. Status code:", response.status_code)
        return None

def display_todos(todos):
    if todos:
        print("===== Todos =====")
        for todo in todos:
            print(f"ID: {todo['id']}")
            print(f"User ID: {todo['userId']}")
            print(f"Title: {todo['title']}")
            print(f"Completed: {'Yes' if todo['completed'] else 'No'}")
            print()
    else:
        print("No todos to display.")


# The save_to_file(data, filename) function takes data and a filename as input and saves the data to a JSON file 
# with the specified filename.
def save_to_file(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to '{filename}'.")


# In the __main__ block, after retrieving the todos data using get_todos(), the script checks if the data is not None.
#  If todos data is retrieved successfully, it calls save_to_file(todos, "todos.json") to save the data to a file named "todos.json". 
# Then, it proceeds to display the todos data using display_todos(todos).
if __name__ == "__main__":
    todos = get_todos()
    if todos:
        save_to_file(todos, "todos.json")
        display_todos(todos)

 
# In the console type: python task_two.py it will then save the database to a new file called todos.json