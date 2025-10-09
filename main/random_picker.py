# Importing necessary modules

import moviePicker.main.Genre_list as Genre_list, random


def get_random_movie_by_genre(genre_name):

    # Getting a list of movies for the specified genre

    movies = Genre_list.search_movies_by_genre(genre_name)

    # If no movies found, return None

    if not movies:
        return None
    # Returning a random movie from the list

    return random.choice(movies)

