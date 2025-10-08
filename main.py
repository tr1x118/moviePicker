# importing necessary modules

from random_picker import get_random_movie_by_genre


def main():
    # Getting user input for genre

    genre_name = (
        input("Enter a movie genre (e.g., Action, Comedy, Drama): ").strip().title()
    )
    # Fetching a random movie from the specified genre

    movie = get_random_movie_by_genre(genre_name)

    if movie:
        # Displaying movie details

        print(f"\nRandom {genre_name} Movie Recommendation:")
        print(f"Title: {movie['title']}")
        print(f"Overview: {movie['overview'] or 'No overview available.'}")
        print(f"Release Date: {movie['release_date'] or 'Unknown'}")
        print(f"Rating: {movie['vote_average']:.2f}/10")
    else:
        # error message if no movie is found

        print(f"No movies found for genre '{genre_name}'. Please try another genre.")


if __name__ == "__main__":
    main()