import bcrypt, datetime, jwt

SECRET_KEY = "sanjuro-dev"

def verify(senha, hashed):
    return bcrypt.checkpw(senha.encode(), hashed)

def authorization(username):
    payload = {
    "user": username,
    "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(hours=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")
