from pydantic import BaseModel

class ProdutoSchema(BaseModel):
    id: int | None = None
    nome: str
    preco: float

    class Config:
        from_attributes = True