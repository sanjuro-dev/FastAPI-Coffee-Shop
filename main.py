

# API
from fastapi import FastAPI, Depends, HTTPException

# Banco de dados
from sqlalchemy.orm import Session
from sqlalchemy import select, delete
from database import  Cell, init_db, SessionLocal

# Inicializa a API e o banco de dados
init_db()
app = FastAPI()

def get_db():
    db = SessionLocal() # Sessao aberta
    try:
        yield db
    finally:
        db.close()

# Classe Depends = define a rotina de acesso ao banco como get_db()

#   Adição de produtos
@app.post("/produtos")
def adicionar_item(nome: str, preco: float, db: Session = Depends(get_db)):
    item = Cell(nome=nome, preco=preco)
    db.add(item)
    db.commit()
    db.refresh(item)
    return {"mensagem": "Criado", "produto": item}
#   Vizualização do banco
@app.get("/produtos")
def mostrar_banco(db: Session = Depends(get_db)):
    return db.execute(select(Cell)).scalars().all()

#   Pesquisa no banco
@app.get("/produtos/{nome}")
def buscar_item(nome: str, db: Session = Depends(get_db)):
    item = db.execute(select(Cell).where(Cell.nome == nome)).scalar()
    if not item:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return item

#   Remoção de itens no banco
@app.delete("/produtos/{nome}")
def remover_item(nome: str, db: Session = Depends(get_db)):
    result = db.execute(delete(Cell).where(Cell.nome == nome))
    db.commit()
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Nada para deletar")
    return {"mensagem": f"{nome} deletado!"}
