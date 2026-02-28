import os
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

# Definindo o caminho do banco de dados
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_banco = os.path.join(diretorio_atual, "vendinha.db")
SQLALCHEMY_DATABASE_URL = f"sqlite:///{caminho_banco}"

# Inicializa à Engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Definindo os campos das celulas
class Cell(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    preco = Column(Float)

# Inicializa o Declarative Mapping
def init_db():
    Base.metadata.create_all(bind=engine)
