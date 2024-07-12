from fastapi import APIRouter, Query, HTTPException
from fastapi_pagination import Page, paginate
from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError
from typing import List

router = APIRouter()

class Atleta(BaseModel):
    nome: str
    centro_treinamento: str
    categoria: str

@router.get("/atletas", response_model=Page[Atleta])
async def get_atletas_paginados(limit: int = Query(default=10, description="Número máximo de itens por página"),
                                offset: int = Query(default=0, description="Número de itens a serem pulados")):
    # Implemente a lógica para buscar atletas com paginação
    atletas = [...]  # Substitua com sua lógica para buscar dados paginados
    return paginate(atletas, limit=limit, offset=offset)

@router.post("/criar_atleta")
async def criar_atleta():
    try:
        # Lógica para criar o atleta no banco de dados usando SQLAlchemy
        # Simulando uma exceção de integridade para demonstração
        raise IntegrityError("Já existe um atleta cadastrado com o cpf: 12345678900")
    except IntegrityError as e:
        raise HTTPException(status_code=303, detail=f"Já existe um atleta cadastrado com o cpf: 12345678900")
