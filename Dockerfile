FROM tiangolo/uvicorn-gunicorn:python3.11

WORKDIR /test-task

COPY . /test-task

RUN pip install -r requirements.txt
RUN python3 read_csv.py
