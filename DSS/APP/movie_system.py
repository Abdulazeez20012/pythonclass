from DSS.APP.movie import Movie

class MovieSystem:
    def __init__(self):
        self.movies = {}

    def add_movie(self, title):
        if title in self.movies:
            raise ValueError("Movie already exists.")
        self.movies[title] = []

    def rate_movie(self, title, rating):
        if title not in self.movies:
            raise ValueError("Movie not found.")
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")
        self.movies[title].append(rating)

    def get_movie_rating(self, title):
        if title not in self.movies or not self.movies[title]:
            raise ValueError("No ratings available for this movie.")
        ratings = self.movies[title]
        return sum(ratings) / len(ratings)

    def get_all_movies_average_rating(self):
        total = 0
        count = 0
        for ratings in self.movies.values():
            total += sum(ratings)
            count += len(ratings)
        return total / count if count > 0 else 0

    def view_all_movies_in_app(self):
        return list(self.movies.keys())
