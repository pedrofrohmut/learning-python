from src.db import db
from src.db.models.Goal import Goal

def add_goal(goal_dto):
    goal = Goal()
    goal.text = goal_dto["text"]
    goal.user_id = goal_dto["user_id"]
    db.session.add(goal)
    db.session.commit()


def find_all_goals(user_id):
    goals = db.session.execute(db.select(Goal).where(Goal.user_id == user_id)).scalars().all()
    return goals


def delete_goal(goal_id):
    goal = db.session.execute(db.select(Goal).where(Goal.id == goal_id)).scalar_one()
    if goal:
        db.session.delete(goal)
        db.session.commit()
