from flask import Flask, jsonify, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from helpers import get_users, check_server, check_activity, get_movies, get_playlists, get_playlist_movies, login_required
from plexapi.server import PlexServer

# init flask
app = Flask(__name__)

# use filesystem instead of cookies for sessions
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/connect", methods=["GET", "POST"])
def connect():

    if request.method == "GET":
        return render_template("connect.html.jinja")
    else:
        plex_url = request.form.get("plex-url")
        plex_token = request.form.get("plex-token")

        # check if plex server is available
        plex = check_server(plex_url, plex_token)

        if plex:
            session["plex_token"] = plex_token
            session["plex_url"] = plex_url
            session["plex"] = plex
            return redirect("/")
        else:
            return redirect("/tryagain")


@app.route("/about")
def about():
    return render_template("about.html.jinja")


@app.route('/')
@login_required
def index():
    return render_template("index.html.jinja")


@app.route('/server')
@login_required
def server():
    users = get_users(session["plex"])
    return render_template("server.html.jinja", users=users)


@app.route('/playlists')
@login_required
def playlists():

    plex_playlists = get_playlists(session["plex"])

    playlists = []

    for i, p_list in enumerate(plex_playlists):

        playlists.append({"title": p_list.title,
                          "id": f'playlist-{i}',
                          })

    return render_template("playlists.html.jinja", playlists=playlists)


@app.route('/disconnect')
def disconnect():
    session.clear()
    return redirect("/")


@app.route('/tryagain')
def tryagain():
    return render_template("tryagain.html.jinja")


@app.route('/update_activity', methods=["GET"])
def update_activity():
    # get the username from the form
    user = request.args.get("username")

    # get all active users from plex
    activity = check_activity(session["plex"])

    for playing in activity:
        if str(playing.usernames[0]) == (user):
            active_user = {"user": user,
                           "show": playing.grandparentTitle if playing.type == "episode" else playing.title,
                           "type": playing.type,
                           "title": playing.title}
            return jsonify(active_user)

    return jsonify(False)


@app.route('/search', methods=["GET"])
def search():
    query = request.args.get("query")
    movies = get_movies(session["plex"], query)
    movies = [movie.title for movie in movies]
    return jsonify(movies=movies)


@app.route('/playdata', methods=["GET"])
def playdata():
    playlist = request.args.get("playlist")
    movies = get_playlist_movies(session["plex"], playlist)

    return jsonify(movies)
