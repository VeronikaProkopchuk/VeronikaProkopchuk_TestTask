# Pydantic models.
from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


class User(BaseModel):
    category: str = Field(min_length=1)
    firstname: str = Field(min_length=1)
    lastname: str = Field(min_length=1)
    email: str = Field(min_length=1)
    gender: str = Field(min_length=1)
    birth_date: Optional[date] = None