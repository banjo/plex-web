from flask import Flask, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from helpers import login_required, check_server, get_users

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

        if check_server(plex_url, plex_token):
            session["plex_token"] = plex_token
            session["plex_url"] = plex_url
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
    get_users()

    return render_template("server.html.jinja")


@app.route('/disconnect')
def disconnect():
    session.clear()
    return redirect("/")


@app.route('/tryagain')
def tryagain():
    return render_template("tryagain.html.jinja")
