import requests
from dotenv import load_dotenv
import os
import random

load_dotenv()
API_KEY = os.getenv("TMBD_API_KEY")

if not API_KEY:
    raise ValueError(
        "TMBD_API_KEY not found in .env file. Please set it:\n"
        "1. Get a free key at https://www.themoviedb.org/settings/api\n"
        "2. Copy .env.example to .env and add: TMBD_API_KEY=your_key"
    )

def get_genre_list():
    url = "https://api.themoviedb.org/3/genre/movie/list"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    params = {"language": "en"}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        return {genre['name']: genre['id'] for genre in data.get('genres', [])}
    except requests.RequestException as e:
        print(f"Error fetching genre list: {e}")
        return {}

def search_movies_by_genre(genre_name, limit=50):
    genres = get_genre_list()
    genre_id = genres.get(genre_name)
    if not genre_id:
        print(f"Genre '{genre_name}' not found. Available genres: {', '.join(genres.keys())}")
        return []

    url = "https://api.themoviedb.org/3/discover/movie"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    params = {
        "with_genres": genre_id,
        "sort_by": "popularity.desc",
        "language": "en",
        "page": 1
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get('results', [])[:limit]
    except requests.RequestException as e:
        print(f"Error fetching movies for genre '{genre_name}': {e}")
        return []

def get_random_movie_by_genre(genre_name):
    movies = search_movies_by_genre(genre_name)
    if not movies:
        return None
    return random.choice(movies)

def main():
    genre_name = input("Enter a movie genre (e.g., Action, Comedy, Drama): ").strip().title()
    movie = get_random_movie_by_genre(genre_name)

    if movie:
        print(f"\nRandom {genre_name} Movie Recommendation:")
        print(f"Title: {movie['title']}")
        print(f"Overview: {movie['overview'] or 'No overview available.'}")
        print(f"Release Date: {movie['release_date'] or 'Unknown'}")
        print(f"Rating: {movie['vote_average']:.2f}/10")
    else:
        print(f"No movies found for genre '{genre_name}'. Please try another genre.")

if __name__ == "__main__":
    main()