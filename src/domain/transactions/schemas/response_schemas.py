"""
Module contains schemas (RESPONSES) for transactions
"""

from datetime import datetime

from pydantic import Field

from .base import BaseResponseSchema


class PixChargeResponseSchema(BaseResponseSchema):
    """
    Schema for pix charge response
    """
    expira_em: datetime = Field(..., description="Data de expiração da cobrança")
    pix_copia_cola: str = Field(..., description="Pix Copia e Cola")


class BoletoChargeResponseSchema(BaseResponseSchema):
    """
    Schema for boleto charge response
    """
    link_pdf: str = Field(..., description="Link para o boleto em PDF")
    data_vencimento: datetime = Field(..., description="Data de vencimento do boleto")


class CreditCardChargeResponseSchema(BaseResponseSchema):
    """
    Schema for credit card charge response
    """
