# FastAPI Coffee Shop

<p align="center"> <img src="logo.png" width="400" style="border-radius:50%;"> </p>


Want some coffee? Lets keep it safe with api.
The API includes authentication with login and password, password hashing using bcrypt, and product queries stored in a database.

The goal of this project is to practice building a backend API with authentication, database access and clean structure using FastAPI and SQLAlchemy.

## Features

- User authentication with login and password
- Password hashing with bcrypt
- JWT authentication
- Product listing endpoint
- SQLAlchemy ORM for database interaction
- Basic HTTP status handling

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- bcrypt
- JWT

## Installation

Clone the repository:

```bash
git clone https://github.com/sanjuro-dev/FastAPI-Coffee-Shop
````

Enter the project folder:

```bash
cd FastAPI-Coffe-Shop
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the API

Start the server with uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Interactive documentation:

```
http://127.0.0.1:8000/docs
```

## Authentication

Users authenticate using login and password.
Passwords are stored hashed using bcrypt.
After login the API returns a JWT token which must be included in protected requests.

## Project Structure

```
FastAPI/
│
├── main.py        # API entry point and routes
├── database.py    # Database connection
├── models.py      # SQLAlchemy models
├── auth.py        # Authentication logic
```

## Notes

The database file is not included in the repository.
When running the project for the first time the database needs to be initialized locally.


Notes

The database file is not included in the repository.
When running the project for the first time the database needs to be initialized locally.
