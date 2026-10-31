from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from datetime import datetime

from app.models import Visitor, VisitorCreate
from app.database import visitors_db

app = FastAPI(
    title="API Controle de Acesso",
    version="1.0.0",
    description="Backend para gerenciamento de entrada e saída de visitantes"
)

# Habilita CORS para permitir que o Frontend faça chamadas da portaria
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    return {"status": "ok", "service": "controle-acesso-api"}

@app.get("/api/v1/visitors", response_model=List[Visitor])
def list_visitors():
    # Retorna apenas visitantes que ainda estão no condomínio
    return [v for v in visitors_db if v.ativo]

@app.post("/api/v1/visitors", response_model=Visitor, status_code=status.HTTP_201_CREATED)
def register_visitor(visitor_in: VisitorCreate):
    new_visitor = Visitor(**visitor_in.model_dump())
    visitors_db.append(new_visitor)
    return new_visitor

@app.put("/api/v1/visitors/{visitor_id}/checkout", response_model=Visitor)
def visitor_checkout(visitor_id: str):
    for visitor in visitors_db:
        if visitor.id == visitor_id and visitor.ativo:
            visitor.ativo = False
            visitor.saida = datetime.now()
            return visitor
    raise HTTPException(status_code=404, detail="Visitante não encontrado ou já realizou saída")