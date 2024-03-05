# Enhanced Data Manipulation
# Objective:
# Develop a script that includes capabilities for data transformation and advanced retrieval.
# Devise a function to transform the retrieved data in a meaningful way. 
# This could involve summarizing data, such as categorizing posts, calculating average engagement metrics, or
# other innovative transformations that add value.
# Store the transformed data in a manner that distinguishes it from the original data, either by
# using a separate file or a dedicated section within the existing file.
# Implement functions for more complex data queries, such as filtering for specific user
# characteristics, searching for keywords within posts, or identifying the top engaging posts.
# Showcase your ability to handle and query data sets efficiently and practically.


import requests
import json

# The get_posts() function retrieves posts data from the JSONPlaceholder API.
def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve posts. Status code:", response.status_code)
        return None

# The categorize_posts(posts) function categorizes posts based on user ID.
def categorize_posts(posts):
    categorized_posts = {"categories": {}}
    for post in posts:
        userId = post['userId']
        if userId not in categorized_posts["categories"]:
            categorized_posts["categories"][userId] = []
        categorized_posts["categories"][userId].append(post)
    return categorized_posts

# The save_to_file(data, filename) function saves data to a JSON file.
def save_to_file(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to '{filename}'.")

# The filter_posts_by_user(posts, user_id) function filters posts by a specific user ID.
def filter_posts_by_user(posts, user_id):
    filtered_posts = [post for post in posts if post['userId'] == user_id]
    return filtered_posts

# The search_posts_by_keyword(posts, keyword) function searches for posts containing a specific keyword.
def search_posts_by_keyword(posts, keyword):
    keyword = keyword.lower()
    matching_posts = [post for post in posts if keyword in post['title'].lower() or keyword in post['body'].lower()]
    return matching_posts

# Within the __main__ block, examples of using the filtering and searching functions are demonstrated.
if __name__ == "__main__":
    posts = get_posts()
    if posts:
        categorized_posts = categorize_posts(posts)
        save_to_file(categorized_posts, "categorized_posts.json")

        # Example usage of filter_posts_by_user function
        filtered_posts = filter_posts_by_user(posts, 1)
        print("Posts by User ID 1:")
        for post in filtered_posts:
            print(f"Title: {post['title']}")

        # Example usage of search_posts_by_keyword function
        matching_posts = search_posts_by_keyword(posts, "delectus")
        print("\nPosts containing keyword 'delectus':")
        for post in matching_posts:
            print(f"Title: {post['title']}")

 

# Interact with the Script in the console by typing: python task_three.pyramid
# After running the script, you'll see the output in the terminal/console. 

# The script will perform the following actions:
# Retrieve posts data from the JSONPlaceholder API.
# Categorize the posts based on user ID and save the categorized data to a file named categorized_posts.json.
# Filter posts by a specific user ID and display the titles of those posts.
# Search for posts containing a specific keyword and display the titles of matching posts.
