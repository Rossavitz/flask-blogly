"""Blogly application."""

from flask import Flask, render_template, request, redirect
from models import db, connect_db, User

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///blogly"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.app_context().push()

connect_db(app)


@app.route("/")
def home_page():
    return redirect("/users")


@app.route("/users")
def list_users():
    """shows users page"""
    users = User.query.all()
    return render_template("list.html", users=users)


@app.route("/users/new", methods=["GET"])
def show_form():
    """shows add user form"""

    return render_template("addUser.html")


@app.route("/users/new", methods=["POST"])
def add_user():
    first_name = request.form["first"]
    last_name = request.form["last"]
    image_url = request.form["image"]

    new_user = User(
        first_name=first_name, last_name=last_name, image_url=image_url or None
    )
    db.session.add(new_user)
    db.session.commit()

    return redirect("/")


@app.route("/users/<int:user_id>")
def show_user(user_id):
    """show details about a single user"""
    user = User.query.get_or_404(user_id)
    return render_template("details.html", user=user)


@app.route("/users/<int:user_id>/edit", methods=["GET"])
def show_edit_form(user_id):
    """shows edit user form"""
    user = User.query.get_or_404(user_id)
    return render_template("edit.html", user=user)


@app.route("/users/<int:user_id>/edit", methods=["POST"])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    user.first_name = request.form["first"]
    user.last_name = request.form["last"]
    user.image_url = request.form["image"]

    db.session.add(user)
    db.session.commit()

    return redirect("/")


@app.route("/users/<int:user_id>/delete", methods=["POST"])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/")
