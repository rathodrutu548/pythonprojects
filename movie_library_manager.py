class Movie:
    def __init__(self, title, genre, director, release_year):
        self.title = title
        self.genre = genre
        self.director = director
        self.release_year = release_year

class MovieLibrary:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def search_by_title(self, title):
        result = []
        for movie in self.movies:
            if title.lower() in movie.title.lower():
                result.append(movie)
        return result

    def search_by_genre(self, genre):
        result = []
        for movie in self.movies:
            if genre.lower() in movie.genre.lower():
                result.append(movie)
        return result

    def display_movie_info(self, movie):
        print("Title:", movie.title)
        print("Genre:", movie.genre)
        print("Director:", movie.director)
        print("Release Year:", movie.release_year)
        print()

# Example usage
library = MovieLibrary()

# Add movies to the library
movie1 = Movie("The Shawshank Redemption", "Drama", "Frank Darabont", 1994)
movie2 = Movie("The Godfather", "Crime", "Francis Ford Coppola", 1972)
movie3 = Movie("The Dark Knight", "Action", "Christopher Nolan", 2008)
library.add_movie(movie1)
library.add_movie(movie2)
library.add_movie(movie3)

# Search by title
search_results = library.search_by_title("godfather")
for movie in search_results:
    library.display_movie_info(movie)

# Search by genre
search_results = library.search_by_genre("action")
for movie in search_results:
    library.display_movie_info(movie)
