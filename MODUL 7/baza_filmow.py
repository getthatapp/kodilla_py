import random
from datetime import datetime


class Movie:
    def __init__(self, title, release_year, genre, views=0):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.view = views

    def play(self):
        self.views += 1

    def __str__(self):
        return f'{self.title} ({self.release_year})'


class Series(Movie):
    def __init__(self, title, release_year, genre, episode, season, views=0):
        super().__init__(title, release_year, genre, views)
        self.episode = episode
        self.season = season

    def __str__(self):
        return f'{self.title} S{str(self.season).zfill(2)}E{str(self.episode).zfill(2)}'


library = []


def get_movies():
    return sorted([item for item in library if isinstance(item, Movie) and not isinstance(item, Series)],
                  key=lambda x: x.title)


def get_series():
    return sorted([item for item in library if isinstance(item, Series)], key=lambda x: x.title)


def search(title):
    for item in library:
        if item.title.lower() == title.lower():
            return item
    return None


def generate_views():
    item = random.choice(library)
    item.views += random.randint(1, 100)
    return item


def generate_views_n_times(n):
    for _ in range(n):
        generate_views()