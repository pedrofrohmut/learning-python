from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import mapped_column

from db.models.TimestampMixin import TimestampMixin
from db import db


class Goal(db.Model, TimestampMixin):
    __tablename__ = "goals"

    id = mapped_column(Integer, primary_key=True)
    text = mapped_column(String, nullable=False)

    user_id = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
