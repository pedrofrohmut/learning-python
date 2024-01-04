from flask import redirect, render_template, request
import bcrypt

from src.app import app
from src.db.data_access.users_data_access import add_user

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

    bytes_password = bytes(password, "UTF-8")
    password_hash = bcrypt.hashpw(bytes_password, bcrypt.gensalt())
    if not bcrypt.checkpw(bytes_password, password_hash):
        return render_template("error.html",
                               error_message="Error to generate a password hash. The hash does not match the password")

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
    return "Sign In"


# POST /verify
@app.post("/users/verify")
def verify():
    return "Verify"


# GET /current
@app.get("/users/current")
def getCurrent():
    return "Current"
