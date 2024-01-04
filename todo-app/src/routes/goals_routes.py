from flask import redirect, request, session, url_for
from src.db.data_access.goals_data_access import add_goal, delete_goal
from src.app import app

@app.post("/goals")
def add():
    if not "user" in session:
        return redirect(url_for("signin"))

    add_goal({
        "text": request.form["text"],
        "user_id": session["user"]["id"]
    })

    return redirect(url_for("home_page"))


@app.post("/goals/<id>/delete")
def delete(id):
    if not "user" in session:
        return redirect(url_for("signin"))

    delete_goal(id)

    return redirect(url_for("home_page"))
