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


def get_users():
    plex = PlexServer(session["plex_url"], session["plex_token"])
    account = plex.myPlexAccount()
    users = [user.title for user in account.users()]


def check_server(url, token):
    try:
        plex = PlexServer(url, token)
        return True
    except:
        return False
