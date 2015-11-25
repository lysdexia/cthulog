# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, url_for, g, redirect, session
from flaskext.auth import Auth, AuthUser, login_required, logout

app = Flask(__name__)
app.config.from_object("config")

# authentication
auth = Auth(app, login_url_name="login")
# you'll stay logged in unto the heat death of the universe
auth.user_timeout = 0

# set up one or more users - they all edit the same blog, so don't expect
# anything fancy. everyone is first fire chief
@app.before_request
def init_users():
    g.users = {}
    for username in app.config["EDITORS"]:
        user = AuthUser(username=username)
        user.set_and_encrypt_password(app.config["EDITORS"][username])
        g.users[username] = user

# "regular" front-end for nsixtymedia.com
@app.route("/")
def index():
    return render_template("index.html")

# must be logged in to edit or create entries

# editor function "landing page"
# again, everything pretty much copied from pocoo.org
@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        if username in g.users:
            if g.users[username].authenticate(request.form["password"]):
                return redirect(url_for("index"))
            return render_template("login.html")
    return render_template("login.html")

# get thee gone, back to index
@app.route("/logout")
def cthlogout():
    logout()
    return redirect(url_for("index"))

# everything that requires a login here
# note that we don't use the @app.route decorator, thus requiring 
# routing info below the actual endpoint definitions
@login_required()
def browse():
    return render_template("browse.html")
app.add_url_rule("/browse", "browse", browse)

@login_required()
def editor():
    return render_template("editor.html")
app.add_url_rule("/editor", "editor", editor, methods = ["GET", "POST"])

@login_required()
def new():
    return render_template("new.html")
app.add_url_rule("/new", "new", new, methods = ["GET", "POST"])

app.secret_key = app.config["APP_SECRET_KEY"]