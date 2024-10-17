# Bookstore

A virtual bookstore where users can read and review books.

## Get started

- Clone the repo to your machine:

    `$ git clone https://github.com/ragehegy/bookstore && cd bookstore`

- Setup your virtual environment using python:
 
   `$ python -m venv venv`

- Make sure pip is installed 
    
    `$ pip --version`

- Install project dependencies:
    
    `$ pip install -r requirements.txt`

- Create `.env` file and add the following sample variables:

    ```
    
    SECRET_KEY = <YOUR_SECRET_KEY>

    DEBUG = TRUE

    ```
- Load sample data into app db models:

    `$ python manage.py loaddata fixtures.json`
    
- To run app:

    `$ python manage.py runserver`
    
- To run tests:

    `$ python manage.py test`
    
# API Documentation:

Visit `http://127.0.0.1:8000/api/schema/swagger-ui/` for full API docs.

## Other API docs urls:

Download the API specs yaml format:
`http://127.0.0.1:8000/api/schema/` 
Redocly UI:
`http://127.0.0.1:8000/api/schema/redoc`

# How to authenticate:

- After registering a new user (`/auth/register`), Send a POST request to the login end point with your username and password fields in the request body.
    ```
    curl --location 'http://127.0.0.1:8000/auth/login' \
    --header 'Content-Type: application/json' \
    --data '{
        "username": <username>,
        "password": <password>
    }'
    ```
- Response sample:
   ```
   {
    "status_code": 200,
    "data": {
        "id": "dbddac87-080c-4150-976a-90d59bcf0211",
        "username": "testrageh",
        "tokens": {
            "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
            "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0..."
            }
        }
    }
   ```
- Use the access token in the authorization header in your requests to authorize the user against endpoints that have POST method.

## Github Actions:

Application goes through a github actions pipelines to validate it's build and test automatically before being able to create a PR and merge from dev branch into main.

*check `.github/workflows/django.yml` for full pipeline overview.*