# importing necessary libraries

import requests, os
from dotenv import load_dotenv


# Load API key from .env file

load_dotenv()
API_KEY = os.getenv("TMBD_API_KEY")

# Check if API key is available

if not API_KEY:
    raise ValueError(
        "TMBD_API_KEY not found in .env file. Please set it:\n"
        "1. Get a free key at https://www.themoviedb.org/settings/api\n"
        "2. Copy .env.example to .env and add: TMBD_API_KEY=your_key"
    )


def get_genre_list():
    # setting up the API request

    url = "https://api.themoviedb.org/3/genre/movie/list"
    headers = {"accept": "application/json", "Authorization": f"Bearer {API_KEY}"}
    params = {"language": "en"}

    try:
        # sendig the request and getting the response

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        return {genre["name"]: genre["id"] for genre in data.get("genres", [])}
    # handling potential errors

    except requests.RequestException as e:
        print(f"Error fetching genre list: {e}")
        return {}


def search_movies_by_genre(genre_name, limit=50):
    # Fetch movies by genre

    genres = get_genre_list()
    genre_id = genres.get(genre_name)

    # If genre not found, return empty list

    if not genre_id:
        print(
            f"Genre '{genre_name}' not found. Available genres: {', '.join(genres.keys())}"
        )
        return []
    # setting up the API request

    url = "https://api.themoviedb.org/3/discover/movie"
    headers = {"accept": "application/json", "Authorization": f"Bearer {API_KEY}"}
    params = {
        "with_genres": genre_id,
        "sort_by": "popularity.desc",
        "language": "en",
        "page": 1,
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get("results", [])[:limit]
    except requests.RequestException as e:
        print(f"Error fetching movies for genre '{genre_name}': {e}")
        return []
