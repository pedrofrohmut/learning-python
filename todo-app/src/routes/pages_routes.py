from flask import render_template, session

from src.app import app

@app.get("/")
@app.get("/pages/home")
def home_page():
    goals = [
        { "id": 1, "text": "Goal 1" },
        { "id": 2, "text": "Goal 2" },
        { "id": 3, "text": "Goal 3" },
        { "id": 4, "text": "Goal 4" },
        { "id": 5, "text": "Goal 5" }
    ]
    if not "user" in session:
        return render_template("signin.html",
                               error_message="You must be signed in to access the todos")
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
