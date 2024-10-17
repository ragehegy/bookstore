FROM python:3.11
COPY . /project
WORKDIR /project
RUN pip install -r requirements.txt
RUN black .
RUN isort .
CMD ["python", "manage.py", "runserver"]