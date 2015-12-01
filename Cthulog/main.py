# -*- coding: utf-8 -*-
import datetime
from flask import Flask, render_template, request, url_for, g, redirect, session
from flaskext.auth import Auth, AuthUser, login_required, logout, Permission, Role, permission_required
from flask.ext.pymongo import PyMongo
from Cthulog.opression.Opression import opression_api

app = Flask(__name__)
app.config.from_object("config")
app.secret_key = app.config["APP_SECRET_KEY"]

mongo = PyMongo(app, config_prefix="MONGOLAB")
opression_api(app)

# authentication
auth = Auth(app, login_url_name="login")
# you'll stay logged in unto the heat death of the universe
auth.user_timeout = 0

create_user = Permission("create", "user")
create_division = Permission("create", "division")
create_post = Permission("create", "post")
read_posts = Permission("read", "posts")

roles = {
        "admin": Role("admin", [
            create_user,
            create_division,
            create_post,
            read_posts,
            ]),
        "user": Role("user", [create_post, read_posts]),
        }

def load_role(role_name):
    return roles.get(role_name)
auth.load_role = load_role

# set up one or more admin users nothing fancy. everyone is first fire chief
@app.before_request
def init_users():
    g.users = {}
    for username in app.config["ADMINS"]:
        user = AuthUser(username=username)
        user.set_and_encrypt_password(app.config["ADMINS"][username])
        user.role = "admin"
        g.users[username] = user

# editor function "landing page"
# again, everything pretty much copied from pocoo.org
@app.route("/", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        if username in g.users:
            if g.users[username].authenticate(request.form["password"]):
                session["username"] = username
                return redirect(url_for("browse"))
    return render_template("login.html")

# get thee gone, back to index
@app.route("/logout")
def cthlogout():
    logout()
    return redirect(url_for("login"))

# everything that requires a login here
# note that we don't use the @app.route decorator, thus requiring 
# routing info below the actual endpoint definitions
@permission_required(resource="read", action="posts")
def browse():
    return render_template("browse.html")
app.add_url_rule("/browse", "browse", browse)

@permission_required(resource="create", action="post")
def editor():
    return render_template("editor.html")
app.add_url_rule("/editor", "editor", editor, methods = ["GET", "POST"])

