# Test Task API

## Veronika Prokopchuk

## Overview

1. [Startup with Docker](#startup-docker)
2. [Startup without Docker](#startup-without-docker)
3. [Using the project](#usage)

## Startup with Docker <a name="startup-docker"></a>

0. Clone this repository
1. Build and run Docker image:
   Note: Building image will take 360.0s

```
cd VeronikaProkopchuk_TestTask
docker compose up --build
```

2. Check it in docs: http://127.0.0.1:8000/docs

## Startup without Docker <a name="startup-without-docker"></a>

0. Clone this repository
1. Install python 11
2. Create virtual enviroment and install dependencies:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Fill the database:

```
python3 read_csv.py
```

4. Launch dev server:

```
uvicorn main:app --reload
```

5. Check it in docs: http://127.0.0.1:8000/docs

## Using the project <a name="usage"></a>

1. Project includes one endpoint: /users
2. Endpoint includes filters by values:
   • category;
   • gender;
   • date_of_birth (in format "%Y-%m-%d");
   • age;
   • age_range (for example, 25 - 30 years).
3. Response: downloadable csv file with list of users (with applied filters)
4. By default endpoint generates result with no filters used (all users returned)
5. Files and directories included in the project:
   • data: directory with dataset.csv file inside;
   • database.py: file for sqlite database;
   • main.py: main file with endpoint inside;
   • models.py: file for database and other models;
   • read_csv.py: file for reading dataset.csv and writing data into sqlite database;
   • schemas.py: file for pydantic models;
   • service.py: file with specific logic functions.
