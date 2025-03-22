import unittest

from movie_system import  MovieSystem

class TestMovieSystem(unittest.TestCase):
    def test_that_movie_can_be_added(self):
        movie_system = MovieSystem()
        movie_system.add_movie("Koto aye")
        self.assertTrue("Koto Aye", movie_system.movies)

    def test_that_when_add_duplicate_movie_should_raise_value_error(self):
        movie_system = MovieSystem()
        movie_system.add_movie("Koto Aye")
        with self.assertRaises(ValueError):
            movie_system.add_movie("Koto Aye")

    def test_that_can_rate_movie(self):
        movie_system = MovieSystem()
        movie_system.add_movie("olongbo iya agba")
        movie_system.rate_movie("olongbo iya agba", 4)
        self.assertEqual(movie_system.movies["olongbo iya agba"].ratings, [4])

    def test_that_when_rate_nonexistent_movie_raise_exception(self):
        movie_system = MovieSystem()
        with self.assertRaises(ValueError):
            movie_system.rate_movie("Nonexistent", 3)

    def test_that_can_get_movie_rating(self):
        movie_system = MovieSystem()
        movie_system.add_movie("olongbo iya agba")
        movie_system.rate_movie("olongbo iya agba", 5)
        movie_system.rate_movie("olongbo iya agba", 3)
        self.assertEqual(movie_system.get_movie_rating("olongbo iya agba"), 4.0)

    def test_that_get_movie_rating_that_has_no_ratings(self):
        movie_system = MovieSystem()
        movie_system.add_movie("olongbo iya agba")
        self.assertEqual(movie_system.get_movie_rating("olongbo iya agba"), 0)

    def test_get_all_movies_average_rating(self):
        movie_system = MovieSystem()
        movie_system.add_movie("olongbo iya agba")
        movie_system.add_movie("Koto Aye")
        movie_system.rate_movie("Koto Aye", 5)
        movie_system.rate_movie("olongbo iya agba", 3)
        self.assertEqual(movie_system.get_all_movies_average_rating(), 4.0)

    def test_that_can_get_all_movies_average_rating_no_movies(self):
        movie_system = MovieSystem()
        self.assertEqual(movie_system.get_all_movies_average_rating(), 0)


if __name__ == "__main__":
    movie_system = MovieSystem()