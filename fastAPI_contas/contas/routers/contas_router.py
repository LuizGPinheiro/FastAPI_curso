from fastapi import APIRouter
from pydantic import BaseModel
from decimal import Decimal
from typing import List

router = APIRouter(prefix="/contas")

class ContasResponse(BaseModel):
    id: int
    description: str
    valor: Decimal
    tipo: str # Pagar, Receber

class ContasRequest(BaseModel):
    id: int
    description: str
    valor: Decimal
    tipo: str # Pagar, Receber

@router.get("/", response_model=List[ContasResponse])
def listar_contas():
    return [
        ContasResponse(
            id=1,
            description="Aluguel",
            valor=1000.50,
            tipo="Pagar",
        ),
        ContasResponse(
            id=2,
            description="Salário",
            valor=5000.50,
            tipo="Receber",
        ),
    ]

@router.post("/", response_model=ContasResponse, status_code=201)
def criar_conta(conta: ContasRequest):
    return ContasResponse(
            id=3,
            description="conta.descricao",
            valor=conta.valor,
            tipo="conta.tipo",
    )