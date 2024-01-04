from flask import render_template, session

from src.app import app
from src.db.data_access.goals_data_access import find_all_goals

@app.get("/")
@app.get("/pages/home")
def home_page():
    if not "user" in session:
        return render_template("signin.html",
                               error_message="You must be signed in to access the todos")

    goals = find_all_goals(session["user"]["id"])

    print("Goals: ", goals)

    return render_template("home.html", goals=goals)


@app.get("/about")
@app.get("/pages/about")
def about_page():
    return render_template("about.html")


@app.get("/signup")
@app.get("/pages/signup")
def signup_page():
    return render_template("signup.html")


@app.get("/signin")
@app.get("/pages/signin")
def signin_page():
    return render_template("signin.html")

@app.get("/error")
@app.get("/pages/error")
def error_page():
    return render_template("error.html")
