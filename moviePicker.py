import requests
import random

movies = {}


def get_movies():
    url = (
        "https://api.themoviedb.org/3/discover/movie?include_adult=true&include_video=false"
        "&language=en-US&page=1&sort_by=popularity.desc"
    )

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9."
        "eyJhdWQiOiI5YTNhMjE4ZDlhOTMwNWZkZWVhMmY4OWY2MjJlNWQ2NyIsIm5iZiI6MTc1OTc1ODE4Ny44MTEsInN1YiI6IjY4ZTNjNzZiZGQ2OGZjZmQ0NmY4MWRjNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ"
        ".B3Zxhm4855tZAVU_VFYy3SZhPFimyLj0Lx1ORS5D7YE",
    }

    response = requests.get(url, headers=headers)
    content = response.json()

    for movie in content["results"]:
        movies[movie["title"]] = movie["release_date"][:4]
    return movies


def pick_movie(movies):
    movie = random.choice(list(movies.items()))
    return movie


def main():
    movies = get_movies()
    movie, year = pick_movie(movies)
    print(f"Random movie: {movie} ({year})")


if __name__ == "__main__":
    main()