from flask import redirect, render_template, request, session
from functools import wraps
from plexapi.server import PlexServer


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("plex_token") is None:
            return redirect("/connect")
        return f(*args, **kwargs)
    return decorated_function


def get_users(url, token):
    return [user.title for user in PlexServer(url, token).myPlexAccount().users() if user.friend]


def check_server(url, token):
    try:
        plex = PlexServer(url, token)
        return True
    except:
        return False


def check_activity(url, token):
    return [client for client in PlexServer(url, token).sessions()]


def get_movies(url, token, query):
    return PlexServer(url, token).search(query)


def get_playlists(url, token):
    return PlexServer(url, token).playlists()


def get_playlist_movies(url, token, playlist):
    movies = PlexServer(url, token).playlist(playlist)

    movie_list = []

    for movie in movies.items():
        movie_list.append({"title": movie.title,
                           "guid": movie.guid[26:],
                           "year": movie.year,
                           "rating": movie.audienceRating})

    return movie_list


def get_sections(url, token):
    return [section.title for section in PlexServer(url, token).library.sections() if section.type == "movie"]
