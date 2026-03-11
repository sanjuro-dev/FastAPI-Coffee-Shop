from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
from sqlalchemy import select
from database import db, User, Product, init_db
from auth import authorization, verify, SECRET_KEY
from schema import ProductSchema
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


@app.post("/produtos", response_model=ProductSchema)
def adicionar_produto(name: str, price:float , user=Depends(authenticate)):
    produto = Product(name=name, price=price)
    db.add(produto)
    db.commit()
    db.refresh(produto)
    return produto

# GET
@app.get("/produtos", response_model=List[ProductSchema])
def listar_produtos(user=Depends(authenticate)):
    return db.query(Product).all()

@app.get("/produtos/{produto_id}", response_model=ProductSchema)
def buscar_produto(product_id:int, user=Depends(authenticate)):

    produto = db.query(Product).filter(Product.id == product_id).first()
    if produto is None:
        raise HTTPException(status_code=404)
    return produto

# DELETE
@app.delete("/produtos/{produto_id}")
def deletar_produto(product_id: int, user=Depends(authenticate)):

    produto = db.query(Product).filter(Product.id == product_id).first()

    if not produto:
        raise HTTPException(status_code=404)

    db.delete(produto)
    db.commit()

    return {"mensagem": "produto removido"}
