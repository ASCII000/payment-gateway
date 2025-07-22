"""
Router for transactions (Command)
"""

from fastapi import APIRouter, Depends

from ..services import TransactionService
from ..schemas import (
    PixChargeRequestSchema, PixChargeResponseSchema,
    CreditCardChargeRequestSchema, CreditCardChargeResponseSchema,
    BoletoChargeRequestSchema, BoletoChargeResponseSchema,
)


router = APIRouter()


@router.post("/pix")
async def create_pix_charge(
    charge: PixChargeRequestSchema,
    service: TransactionService = Depends(TransactionService),
) -> PixChargeResponseSchema:
    """
    Create pix charge
    """
    return await service.create_pix_charge(charge)


@router.post("/boleto")
async def create_boleto_charge(
    charge: BoletoChargeRequestSchema,
    service: TransactionService = Depends(TransactionService),
) -> BoletoChargeResponseSchema:
    """
    Create boleto charge
    """
    return await service.create_boleto_charge(charge)


@router.post("/credit")
async def create_credit_card_charge(
    charge: CreditCardChargeRequestSchema,
    service: TransactionService = Depends(TransactionService),
) -> CreditCardChargeResponseSchema:
    """
    Create credit card charge
    """
    return await service.create_credit_card_charge(charge)
