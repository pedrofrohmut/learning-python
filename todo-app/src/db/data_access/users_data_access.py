from src.db import db
from src.db.models.User import User

def add_user(user_dto):
    user = User()
    user.name = user_dto["name"]
    user.email = user_dto["email"]
    user.phone = user_dto["phone"]
    user.password_hash = user_dto["password_hash"]
    db.session.add(user)
    db.session.commit()


def find_by_email(email):
    user = db.session.execute(db.select(User).where(User.email == email)).scalar_one()
    if user:
        return user
    else:
        return None
