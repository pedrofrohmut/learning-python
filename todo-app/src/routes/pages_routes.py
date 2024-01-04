from flask import redirect, render_template, session, url_for

from src.app import app

@app.get("/")
@app.get("/pages/home")
def home_page():
    if not session or not session["user_id"]:
        return render_template("signin.html",
                               error_message="You must be signed in to access the todos")
    return render_template("home.html")


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
