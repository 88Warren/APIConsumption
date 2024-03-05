import requests
import json

def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve posts. Status code:", response.status_code)
        return None

def categorize_posts(posts):
    categorized_posts = {"categories": {}}
    for post in posts:
        userId = post['userId']
        if userId not in categorized_posts["categories"]:
            categorized_posts["categories"][userId] = []
        categorized_posts["categories"][userId].append(post)
    return categorized_posts

def save_to_file(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to '{filename}'.")

def filter_posts_by_user(posts, user_id):
    filtered_posts = [post for post in posts if post['userId'] == user_id]
    return filtered_posts

def search_posts_by_keyword(posts, keyword):
    keyword = keyword.lower()
    matching_posts = [post for post in posts if keyword in post['title'].lower() or keyword in post['body'].lower()]
    return matching_posts

def identify_top_engaging_posts(posts):
    sorted_posts = sorted(posts, reverse=True)
    return sorted_posts[:5]

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
