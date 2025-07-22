"""
Modules contains tables sqlmodel
"""

from enum import Enum

from sqlmodel import SQLModel, Field
from sqlalchemy import JSON

from utils.main import now_utc_iso



class StateEnum(str, Enum):
    """
    Possible states transactions
    """
    PAGO = "PAGO"
    PENDENTE = "PENDENTE"
    CANCELADO = "CANCELADO"


class Transaction(SQLModel, table=True):
    """
    Table transactions
    """

    __tablename__ = "transacoes"

    id: int | None = Field(default=None, primary_key=True)
    cliente_nome: str = Field(..., description="Nome do cliente da cobrança")
    cliente_cpf_cnpj: str | None = Field(None, description="CPF ou CNPJ do cliente da cobrança")
    estado: StateEnum = Field(..., description="Estado da cobrança")
    criado_em: str = Field(default_factory=now_utc_iso, description="Data de criacao da cobrança")


class TransactionLog(SQLModel, table=True):
    """
    Table transaction log
    """

    __tablename__ = "transacoes_log"

    id: int | None = Field(default=None, primary_key=True)
    transacao_id: int = Field(foreign_key="transacoes.id")
    estado: StateEnum = Field(..., description="Estado da cobrança")
    conteudo_json: dict = Field(
        default_factory=dict,
        sa_type=JSON(),
        description="Conteúdo JSON da cobrança"
    )
    criado_em: str = Field(default_factory=now_utc_iso, description="Data de criação da cobrança")
