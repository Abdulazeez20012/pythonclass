import datetime

class Movie:
    def __init__(self, title):
        self.title = title
        self.date_added = datetime.datetime.now()
        self.ratings = []

    def add_rating(self, rating):
        if 1 <= rating <= 5:
            self.ratings.append(rating)
        else:
            raise ValueError("Rating must be between 1 and 5")

    def get_average_rating(self):
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)
