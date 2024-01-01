from flask import Flask, render_template

from src import say_hello

app = Flask(__name__)

@app.get("/")
def hello_route():
    name = "John Doe"
    say_hello(name)
    return render_template("hello.html", name=name)

# Routes

# Goals:
#       addGoal (post /), findAllGoals (get /), updateGoal (put /:id), deleteGoal (delete /:id)

# Users:
#       signUpUser (post /), signInUser (post /signin), verifyUser (post /verify), getCurrent(get /current)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
