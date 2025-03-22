import unittest
import datetime
from movie_system import Movie


class TestMovie(unittest.TestCase):
    def test_that_can_create_movie(self):
        movie = Movie("Koto Aye")
        self.assertEqual(movie.title, "Koto Aye")
        self.assertIsInstance(movie.date_added, datetime.datetime)
        self.assertEqual(movie.ratings, [])

    def test_add_valid_rating(self):
        movie = Movie("Koto Aye")
        movie.add_rating(5)
        self.assertEqual(movie.ratings, [5])

    def test_add_invalid_rating_for_movie(self):
        movie = Movie("Koto Aye")
        with self.assertRaises(ValueError):
            movie.add_rating(6)

    def test_that_can_get_average_rating_of_movie(self):
        movie = Movie("Koto aye")
        movie.add_rating(3)
        movie.add_rating(5)
        self.assertEqual(movie.get_average_rating(), 4.0)

    def test_that_can_get_average_rating_movie_of_no_ratings(self):
        movie = Movie("Inception")
        self.assertEqual(movie.get_average_rating(), 0)

