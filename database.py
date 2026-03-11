import os
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from bcrypt import hashpw, gensalt
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

def init_db():
    if db.query(User).first() is None:
        user = input()
        password = input()
        Base.metadata.create_all(engine)
        Admin = User(name=user, hash=hashpw(password.encode(), gensalt()).decode())
        db.add(Admin)
        db.commit()
        print(f"Registered! welcome to Fast API, {user}")
    else:
        pass

