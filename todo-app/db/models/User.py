from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, relationship

from db import db
from db.models.TimestampMixin import TimestampMixin

class User(db.Model, TimestampMixin):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String, nullable=False)
    email = mapped_column(String, unique=True, nullable=False)
    password_hash = mapped_column(String, nullable=False)
    phone = mapped_column(String)

    goals = relationship("Goal")
