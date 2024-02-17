import csv

from main import get_db
from models import Users
from datetime import datetime, date

# Write data from csv file to database
with open("data/dataset.csv", "r") as data:
    reader = csv.DictReader(data)
    print("Data processing (Filling Database) ...")

    for element in reader:
        model = Users()
        today = date.today()
        db = next(get_db())

        model.category = element["category"]
        model.firstname = element["firstname"]
        model.lastname = element["lastname"]
        model.email = element["email"]
        model.gender = element["gender"]
        model.birth_date = datetime.strptime(element["birthDate"], "%Y-%m-%d").date()
        model.age = today.year - model.birth_date.year - ((today.month, today.day) < (model.birth_date.month, model.birth_date.day))

        db.add(model)
        db.commit()
