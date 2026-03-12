import os
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from bcrypt import hashpw, gensalt
path = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(path, "menu.db")
SQLALCHEMY_DATABASE_URL = f"sqlite:///{db_path}"


engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()



class Coffee(Base):
    __tablename__ = "menu"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)


class User(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    hash = Column(String)



db = SessionLocal()

def init_db():
    try:
        db.query(User).first()
    except:
        user = input()
        password = input()
        Base.metadata.create_all(engine)
        Admin = User(name=user, hash=hashpw(password.encode(), gensalt()).decode())
        db.add(Admin)
        db.commit()
        print(f"Registered! welcome to Fast API, {user}")

