from flask import redirect, render_template, request, session
from functools import wraps
from plexapi.server import PlexServer


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/1.0/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("plex_token") is None:
            return redirect("/connect")
        return f(*args, **kwargs)
    return decorated_function


def get_users(plex):
    return [user.title for user in plex.myPlexAccount().users() if user.friend]


def check_server(url, token):
    try:
        plex = PlexServer(url, token)
        return plex
    except:
        return False


def check_activity(plex):
    return [client for client in plex.sessions()]


def get_movies(plex, query):
    return plex.search(query)


def get_playlists(plex):
    return plex.playlists()
