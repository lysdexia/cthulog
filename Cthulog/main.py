# -*- coding: utf-8 -*-
import datetime
from flask import Flask, render_template, request, url_for, g, redirect, session
from flaskext.auth import Auth, AuthUser, login_required, logout
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config")

# authentication
auth = Auth(app, login_url_name="login")
# you'll stay logged in unto the heat death of the universe
auth.user_timeout = 0

# initialze ye olde db
db = SQLAlchemy(app)

# set up our one class
class Cthulog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stamp = db.Column(
            db.DateTime(timezone=True),
            default=datetime.datetime.utcnow()
            )
    author = db.Column(db.String)
    title = db.Column(db.String)
    content = db.Column(db.Text)
    
    def __init__(self, title, content):
        self.author = session["username"]
        self.title = title
        self.content = content

    def __repr__(self):
        return "<Cthulog %r>"%self.title

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
    posts = Cthulog.query.all()
    print(posts)
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
                session["username"] = username
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
    log = Cthulog("cow pie guy", "deep in the heart of texas")
    db.session.add(log)
    return render_template("new.html")
app.add_url_rule("/new", "new", new, methods = ["GET", "POST"])

@login_required()
def init_db():
    print("initializing db")
    try:
        db.create_all()
    except Exception as error:
        print(error)
    return redirect(url_for("index"))
app.add_url_rule("/init-db", "init_db", init_db)


app.secret_key = app.config["APP_SECRET_KEY"]
