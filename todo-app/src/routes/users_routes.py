from flask import render_template, request

from src.app import app, bcrypt
from src.db.data_access.users_data_access import add_user, find_by_email

# Post /
@app.post("/users/")
def signUp():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    password = request.form["password"]
    confirm_password = request.form["confirm_password"]

    if password != confirm_password:
        return render_template("signup.html",
                               password_error="Password and confirm password don't match",
                               name=name,
                               email=email,
                               phone=phone)

    password_hash = bcrypt.generate_password_hash(password).decode("utf-8")
    if not bcrypt.check_password_hash(password_hash, password):
        return render_template("error.html",
                               error_message="Error to generate a password hash. "
                                             "The hash does not match the password")

    add_user({
        "name": name,
        "email": email,
        "phone": phone,
        "password_hash": password_hash
    })

    return render_template("signin.html",
                           success_message="User added. You can now sign in.")


# POST /signin
@app.post("/users/signin")
def signIn():
    email = request.form["email"]
    password = request.form["password"]

    user = find_by_email(email)
    if not user:
        return render_template("signin.html",
                               error_message="User not fond with this e-mail")

    if not bcrypt.check_password_hash(user.password_hash, password):
        return render_template("signin.html",
                               error_message="User e-mail and password do not match",
                               email=email)

    return render_template("home.html")


# POST /verify
@app.post("/users/verify")
def verify():
    return "Verify"


# GET /current
@app.get("/users/current")
def getCurrent():
    return "Current"
