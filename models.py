# Models
from datetime import date
from enum import Enum

from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from database import Base


# Database User model
class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[str | None] = mapped_column(String(100))
    firstname: Mapped[str | None] = mapped_column(String(100))
    lastname: Mapped[str | None] = mapped_column(String(100))
    email: Mapped[str | None] = mapped_column(String(100))
    gender: Mapped[str | None] = mapped_column(String(100))
    birth_date: Mapped[date | None]
    age: Mapped[int | None]


# Model for Users age filtering
class UserAgeRanges(Enum):
    AR1 = 25, 30, "25-30 years"
    AR2 = 30, 35, "30-35 years"

    def __init__(self, from_age, to_age, label):
        self.from_age = from_age
        self.to_age = to_age
        self.label = label