import requests

base_url = "http://localhost:8000"  # Replace with your local Frappe instance URL
import os

api_key = os.getenv("API_KEY", "default_api_key")
api_secret = os.getenv("API_SECRET", "default_api_secret")


headers = {"Authorization": f"token {api_key}:{api_secret}"}

def fetch_movies():
    """Fetch and display all movies."""
    response = requests.get(f"{base_url}/api/method/movie_api.get_movies", headers=headers)
    if response.status_code == 200:
        movies = response.json()["message"]
        for movie in movies:
            print(f"Title: {movie['title']}, Director: {movie['director']}, Released Date: {movie['released_date']}")
    else:
        print(f"Error: {response.text}")

def add_movie(title, director, released_date, poster=None):
    """Add a new movie."""
    data = {
        "title": title,
        "director": director,
        "released_date": released_date,
        "poster": poster  # Can be None
    }
    response = requests.post(
        f"{base_url}/api/method/movie_api.add_movie",
        headers=headers,
        json=data
    )
    if response.status_code == 200:
        print(f"Movie added successfully: {response.json()['message']}")
    else:
        print(f"Error: {response.text}")

def delete_movie(movie_id):
    """Delete a movie by ID."""
    data = {"movie_id": movie_id}
    response = requests.post(
        f"{base_url}/api/method/movie_api.delete_movie",
        headers=headers,
        data=data
    )
    if response.status_code == 200:
        print(response.json()["message"])
    else:
        print(f"Error: {response.text}")
