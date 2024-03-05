# API Consumption and Data Display
# Objective:
# Write a script to interact with an API, specifically to retrieve data and display it in a user-friendly
# format in the console.
# You will be using the JSONPlaceholder API for this task. This API provides a wide range of
# endpoints simulating typical blog data, such as users, posts, comments, etc.


# This line imports the requests module, which is a popular HTTP library in Python used for making requests to web servers.
import requests

# This function get_todos() is defined to retrieve todos data from the JSONPlaceholder API. 
# It sends a GET request to the specified URL (https://jsonplaceholder.typicode.com/todos). 
# If the response status code is 200 (OK), it returns the JSON data using response.json(). 
# Otherwise, it prints an error message and returns None.
def get_todos():
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve todos. Status code:", response.status_code)
        return None


# This function display_todos(todos) is defined to display the todos data in a user-friendly way in the console. 
# It takes the todos data retrieved from the API as input. 
# If todos is not empty (i.e., there are todos), it iterates over each todo and prints its ID, user ID, title, and completion status. 
# If todos is empty, it prints "No todos to display."
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


# This block of code is executed when the script is run directly (not imported as a module). 
# It calls the get_todos() function to retrieve todos data from the API and assigns it to the variable todos. 
# Then, it calls the display_todos(todos) function to display the todos data in the console.
# Overall, this Python script retrieves todos data from the JSONPlaceholder API, processes it to ensure it's valid JSON, and then displays it in a user-friendly way in the console. 
# It demonstrates how to make HTTP requests, handle responses, and work with JSON data in Python.
if __name__ == "__main__":
    todos = get_todos()
    display_todos(todos)


# In the console type: python task_one.py to display the data in the console. 