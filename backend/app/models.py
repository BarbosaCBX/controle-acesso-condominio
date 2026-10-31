from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
import uuid

class VisitorCreate(BaseModel):
    nome: str = Field(..., example="João Silva")
    documento: str = Field(..., example="123.456.789-00")
    unidade: str = Field(..., example="Bloco A - Ap 42")

class Visitor(VisitorCreate):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    entrada: datetime = Field(default_factory=datetime.now)
    saida: Optional[datetime] = None
    ativo: bool = True