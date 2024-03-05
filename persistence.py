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

def save_to_file(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to '{filename}'.")

if __name__ == "__main__":
    todos = get_todos()
    if todos:
        save_to_file(todos, "todos.json")
        display_todos(todos)
