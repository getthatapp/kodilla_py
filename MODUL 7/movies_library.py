import random
from datetime import datetime


class Movie:
    def __init__(self, title, release_year, genre, views=0):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.views = views

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
    movies = []
    for item in library:
        if isinstance(item, Movie) and not isinstance(item, Series):
            movies.append(item)
    movies.sort(key=lambda x: x.title)
    return movies


def get_series():
    series = []
    for item in library:
        if isinstance(item, Series):
            series.append(item)
    series.sort(key=lambda x: x.title)
    return series


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


def top_titles(top_n=3, content_type=None):
    if content_type == "movies":
        content_list = get_movies()
    elif content_type == "series":
        content_list = get_series()
    else:
        content_list = library

    sorted_list = sorted(content_list, key=lambda x: x.views, reverse=True)
    return sorted_list[:top_n]


def add_full_season(title, release_year, genre, season, num_episodes):
    for episode in range(1, num_episodes + 1):
        library.append(Series(title, release_year, genre, episode, season))


def count_episodes(series_title):
    count = 0
    for item in library:
        if isinstance(item, Series) and item.title.lower() == series_title.lower():
            count += 1
    return count


if __name__ == "__main__":
    library.append(Movie("Pulp Fiction", 1994, "crime"))
    library.append(Movie("The Shawshank Redemption", 1994, "drama"))
    library.append(Series("The Simpsons", 1989, "animation", 1, 1))
    library.append(Series("The Simpsons", 1989, "animation", 2, 1))
    library.append(Series("Breaking Bad", 2008, "drama", 1, 1))

    add_full_season("The Simpsons", 1999, "animation", 2, 22)

    print("Biblioteka filmów")
    generate_views_n_times(10)
    date = datetime.now().strftime("%d.%m.%Y")
    print(f"Najpopularniejsze filmy i seriale dnia {date}:")
    top_3 = top_titles()
    for item in top_3:
        print(f"{item} - liczba odtworzeń: {item.views}")
