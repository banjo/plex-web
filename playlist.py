import requests
from bs4 import BeautifulSoup
import sys
from plexapi.server import PlexServer

URL_PAGE = "?&mode=detail&page="
HEADERS = {"Accept-Language": "en-US,en;q=0.5"}


def add_playlist_to_plex(url, token, link, name, section, users):

    movies = scrape(link)
    playlist, failed_movies = add_playlist(movies, url, token, name)

    if len(users) > 0:
        copy_to_users(playlist, users)

    return failed_movies


def scrape(website):

    # create lists that takes all data from every loop
    movie_final = []
    year_final = []

    k = 1
    while True:

        html = requests.get(website + URL_PAGE + str(k), headers=HEADERS)
        soup = BeautifulSoup(html.content, "lxml")

        # find popular movies and years, and convert to list
        movies = soup.select(
            '#main > div > div.lister.list.detail.sub-list > div.lister-list > div > div.lister-item-content > h3 > a')
        years = soup.select(
            "#main > div > div.lister.list.detail.sub-list > div.lister-list > div > div.lister-item-content > h3 > span.lister-item-year.text-muted.unbold"
        )

        # break if there are not movies left
        if len(movies) == 0:
            break

        # get all movie titles and years
        movies_string = [movie.get_text() for movie in movies]
        years_int = [year.get_text().replace("(", "") for year in years]
        years_int = [year.replace(")", "") for year in years_int]
        years_int = [year.replace("I ", "") for year in years_int]

        # append all movies that are scraped
        movie_final = movie_final + movies_string.copy()
        year_final = year_final + years_int.copy()

        # loop
        k += 1

    # create dict for each movie
    movie_list = {}
    for i, movie in enumerate(movie_final):
        movie_list[movie] = {"title": movie, "year": year_final[i]}

    return movie_list


def add_playlist(name_list, url, token, name):
    movie_list = []
    failed_movies = []

    for movie in name_list:

        # create the movie dict item
        movie = name_list[movie]

        # get movie if it exists
        temp = get_movie(movie, url, token)

        # loop if it can't find the movie
        if temp is False:
            failed_movies.append(movie["title"])
            continue

        # add to list if it can find it
        movie_list.append(temp)

    # create playlist
    playlist = PlexServer(url, token).createPlaylist(name, movie_list)

    return playlist, failed_movies


def get_movie(movie, url, token):
    results = PlexServer(url, token).search(movie["title"])

    # return movie if it exists
    for plex_movie in results:

        if plex_movie.type == "movie" and str(plex_movie.year) in str(movie["year"]):
            return plex_movie

    return False


def copy_to_users(playlist, users):
    for user in users:
        try:
            playlist.copyToUser(user)
        except:
            raise NameError(f"{user} does not have access to the library.")