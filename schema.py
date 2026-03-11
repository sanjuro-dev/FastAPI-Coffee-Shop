from pydantic import BaseModel

class ProdutoSchema(BaseModel):
    id: int | None = None
    name: str
    price: float

    class Config:
        from_attributes = True