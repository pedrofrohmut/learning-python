from app import app

# POST addGoal /
@app.post("/goals/")
def add():
    return "Add goal"


# GET findAll /
@app.get("/goals/")
def findAll():
    return "Find all"


# PUT updateGoal /:id
@app.put("/goals/<id>")
def update(id):
    return "Update goal " + id


# DELETE deleteGoal /:id
@app.delete("/goals/<id>")
def delete(id):
    return "Delete goal " + id
