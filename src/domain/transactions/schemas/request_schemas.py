"""
Module contains schemas (REQUEST) for transactions
"""

from datetime import datetime

from pydantic import Field

from .base import BaseChargeRequestSchema


class BoletoChargeRequestSchema(BaseChargeRequestSchema):
    """
    Schema for boleto charge request
    """
    data_vencimento: datetime = Field(..., description="Data de vencimento do boleto")


class CreditCardChargeRequestSchema(BaseChargeRequestSchema):
    """
    Schema for credit card charge request
    """
    numero: str = Field(..., description="Numero do cartão de crédito")
    mes: int = Field(..., description="Mês de vencimento do cartão de crédito")
    ano: int = Field(..., description="Ano de vencimento do cartão de crédito")
    cvv: str = Field(..., description="CVV do cartão de crédito")

class PixChargeRequestSchema(BaseChargeRequestSchema):
    """
    Schema for pix charge request
    """
    tempo_aguardo: int = Field(..., description="Tempo de vencimento em segundos")
