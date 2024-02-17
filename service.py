# Specific logic
import csv
from datetime import datetime

from sqlalchemy import or_, true, false
from sqlalchemy.orm import Session

from models import UserAgeRanges as age_ranges, Users


# Function for filtering users from database.
def filter_data(db: Session, category: str, gender: str, date_of_birth: str, age: int, age_range: str):
    # Converting date of birth
    birth_date = None
    if date_of_birth:
        birth_date = format_birth_date(date_of_birth)

    # Generating age range
    from_age = None
    to_age = None
    if age_range:
        from_age, to_age = generate_age_range(age_range)

    # Query
    user_to_return = (
        db.query(Users)
        .filter(
            or_(Users.category == category, true() if category is None else false()),
            or_(Users.gender == gender, true() if gender is None else false()),
            or_(Users.birth_date == birth_date, true() if date_of_birth is None else false()),
            or_(Users.age == age, true() if age is None else false()),
            or_(Users.age.between(from_age, to_age), true() if age_range is None else false()),
        )
        .all()
    )

    return user_to_return


# Converting date of birth
def format_birth_date(date_of_birth: str):
    return datetime.strptime(date_of_birth, "%Y-%m-%d").date()


# Generating age range
def generate_age_range(age_range: str):
    for element in age_ranges:
        if age_range == element.label:
            from_age = element.from_age
            to_age = element.to_age
    return (from_age, to_age)


# Function for writing results into csv file
def generate_csv_file(data: list, file_name: str):
    with open(file_name, "w") as f:
        writer = csv.DictWriter(f, ["category", "firstname", "lastname", "email", "gender", "birth_date"], extrasaction="ignore")
        writer.writeheader()
        for element in data:
            writer.writerow({"category": element.category, "firstname": element.firstname, "lastname": element.lastname, "email": element.email, "gender": element.gender, "birth_date": element.birth_date})
