from app import app

# Post /
@app.post("/users/")
def signUp():
    return "Sign Up"


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
