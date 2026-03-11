FastAPI Coffee Shop

want some coffee?
The API includes authentication with login and password, password hashing using bcrypt, and product queries stored in a database.

The goal of this project is to practice building a backend API with authentication, database access and clean structure using FastAPI and SQLAlchemy.

Features

User authentication with login and password

Password hashing with bcrypt

JWT authentication

Product listing endpoint

SQLAlchemy ORM for database interaction

Basic HTTP status handling

Tech Stack

Python

FastAPI

SQLAlchemy

bcrypt

JWT

Installation

Clone the repository:

git clone https://github.com/sanjuro-dev/FastAPI.git

Enter the project folder:

cd FastAPI

Create a virtual environment:

python -m venv venv

Activate it:

Windows
venv\Scripts\activate

Linux / Mac
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Running the API

Start the server with uvicorn:

uvicorn main:app --reload

The API will be available at:

http://127.0.0.1:8000

Interactive documentation:

http://127.0.0.1:8000/docs

Authentication

Users authenticate using login and password.
Passwords are stored hashed using bcrypt.
After login the API returns a JWT token which must be included in protected requests.

Project Structure

main.py
API entry point and route definitions

database.py
Database connection and session configuration

models.py
SQLAlchemy models

auth.py
Authentication logic (hashing, token creation, verification)

Notes

The database file is not included in the repository.
When running the project for the first time the database needs to be initialized locally.
