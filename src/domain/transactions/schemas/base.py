#pylint: disable=no-self-argument

"""
Module contains base schemas for requests and responses
"""
from decimal import Decimal

from pydantic import BaseModel, Field, field_validator
from fastapi.exceptions import RequestValidationError

from utils.validators import validate_cpf_cnpj


class BaseChargeRequestSchema(BaseModel):
    """
    Schema for pix charge request
    """
    nome_cliente: str = Field(..., description="Nome do cliente da cobrança")
    cpf_cnpj: str | None = Field(None, description="CPF ou CNPJ do cliente da cobrança")
    valor: Decimal = Field(..., description="Valor da cobrança", gt=1)

    @field_validator("cpf_cnpj", mode="before")
    def validate_cpf_cnpj(cls, value: str) -> str | None:
        """
        Validate CPF or CNPJ
        """

        if value and not validate_cpf_cnpj(value):
            raise RequestValidationError(
                "CPF ou CNPJ inválido",
            )

        return value


class BaseResponseSchema(BaseModel):
    """
    Schema for pix charge response
    """
    id: int = Field(..., description="ID da cobrança")
    gateway_id: str = Field(..., description="ID da cobrança no provedor de pagamento")
    nome_cliente: str = Field(..., description="Nome do cliente da cobrança")
    valor: Decimal = Field(..., description="Valor da cobrança")
