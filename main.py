import os
import pathlib

from fastapi import FastAPI, Depends, Query, status
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from database import engine, get_db
from models import Base, UserAgeRanges as age_ranges
from service import generate_csv_file, filter_data

# Instantiate app
app = FastAPI()

Base.metadata.create_all(bind=engine)


# Main endpoint
@app.get("/users", status_code=status.HTTP_200_OK)
def users(
    db: Session = Depends(get_db),
    category: str | None = None,
    gender: str = Query(None, enum=["male", "female"]),
    date_of_birth: str | None = None,
    age: int | None = None,
    age_range: str = Query(None, enum=[f"{age_ranges.AR1.label}", f"{age_ranges.AR2.label}"]),
):
    # Applying filters
    users_to_return = filter_data(db, category, gender, date_of_birth, age, age_range)

    # Generating csv file with results
    generate_csv_file(users_to_return, "results.csv")

    # Returning csv file with results (available for download in docs)
    absolute_path = pathlib.Path().absolute()
    file_path = os.path.join(absolute_path, "results.csv")
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="text/csv", filename="results.csv")
