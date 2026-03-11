import bcrypt, datetime
from jose import jwt

SECRET_KEY = "sanjuro-dev"

def verify(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed.encode())

def authorization(username):
    payload = {
    "user": username,
    "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(hours=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")
