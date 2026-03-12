import bcrypt, datetime
from jose import jwt
import secrets
from pathlib import Path

ENV_FILE = Path(".env")


def getkey():
    secret = None

    if ENV_FILE.exists():
        with open(ENV_FILE) as f:
            for line in f:
                key, _, value = line.partition("=")
                if key.strip() == "SECRET_KEY":
                    secret = value.strip()
                    break

    if not secret:
        secret = secrets.token_urlsafe(32)
        with open(ENV_FILE, "a") as f:
            f.write(f"\nSECRET_KEY={secret}\n")

    return secret

SECRET_KEY = getkey()

def verify(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed.encode())

def authorization(username):
    payload = {
    "user": username,
    "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(hours=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")
