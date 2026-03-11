import bcrypt
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
import datetime
import os
from sqlalchemy import create_engine, Column, Integer, String, Float, select
from sqlalchemy.orm import declarative_base, sessionmaker

# Database
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_banco = os.path.join(diretorio_atual, "dados.db")
SQLALCHEMY_DATABASE_URL = f"sqlite:///{caminho_banco}"


engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()



class Product(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    preco = Column(Float)


class User(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    hash = Column(String)


db = SessionLocal()

# Token
SECRET_KEY = "sanjuro-dev"
security = HTTPBearer()

def verify(senha, hashed):
    return bcrypt.checkpw(senha.encode(), hashed)

def authorization(username):
    payload = {
    "user": username,
    "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(hours=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

# API
app = FastAPI()

@app.post("/login")
def login(username: str, senha: str):

    query = select(User).where(User.name == username)
    user = db.execute(query).scalar_one_or_none()

    if user is None or not verify(senha, user.hash):
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

@app.get("/produtos")
def listar_produtos(user=Depends(authenticate)):
    return