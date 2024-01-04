from flask import redirect, render_template, request, session, url_for

from src.app import app, bcrypt
from src.db.data_access.users_data_access import add_user, find_by_email

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

    session["user"] = {
        "id": user.id,
        "name": user.name,
        "email": user.email
    }

    return redirect(url_for("home_page"))


@app.post("/users/signout")
def signout():
    session.pop("user", None)
    return redirect(url_for("signin_page"))
