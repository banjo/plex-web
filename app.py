from flask import Flask, jsonify, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from helpers import login_required, check_server, get_users
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


@app.route('/disconnect')
def disconnect():
    session.clear()
    return redirect("/")


@app.route('/tryagain')
def tryagain():
    return render_template("tryagain.html.jinja")


@app.route('/update_activity', methods=["POST"])
def update_activity():
    user = request.form.get("user")
    
