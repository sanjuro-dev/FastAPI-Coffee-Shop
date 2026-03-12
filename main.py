from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware
from jose import jwt
from sqlalchemy import select
from database import db, User, Coffee, init_db
from auth import authorization, verify, SECRET_KEY
from schema import CoffeeSchema
from typing import List

# API
security = HTTPBearer()
app = FastAPI()
init_db()

# POST
@app.post("/login")
def login(username: str, password: str):

    query = select(User).where(User.name == username)
    user = db.execute(query).scalar_one_or_none()

    if user is None or not verify(password, user.hash):
        raise HTTPException(status_code=401)

    token = authorization(username)

    return {"token": token}

def authenticate(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload["user"]
    except:
        raise HTTPException(status_code=401)


@app.post("/management", response_model=CoffeeSchema)
def add_coffee(name: str, price:float , user=Depends(authenticate)):
    coffee = Coffee(name=name, price=price)
    db.add(coffee)
    db.commit()
    db.refresh(coffee)
    return coffee

# GET
@app.get("/management", response_model=List[CoffeeSchema])
def check_menu(user=Depends(authenticate)):
    return db.query(Coffee).all()

@app.get("/management/{produto_id}", response_model=CoffeeSchema)
def order_a_coffee(coffee_id:int, user=Depends(authenticate)):

    coffee = db.query(Coffee).filter(Coffee.id == coffee_id).first()
    if coffee is None:
        raise HTTPException(status_code=404)
    return coffee

# DELETE
@app.delete("/management/{coffee_id}")
def trash_coffee(coffee_id: int, user=Depends(authenticate)):

    coffee = db.query(Coffee).filter(Coffee.id == coffee_id).first()

    if not coffee:
        raise HTTPException(status_code=404)

    db.delete(coffee)
    db.commit()

    return {"mensagem": f"trashed {coffee_id}"}
