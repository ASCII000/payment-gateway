"""
Router for transactions (Query)
"""

from typing import List
from fastapi import APIRouter, Depends

from ..schemas import (
    BaseResponseSchema,
    PixChargeResponseSchema,
    BoletoChargeResponseSchema,
    CreditCardChargeResponseSchema,
)

from ..services import TransactionService


router = APIRouter()


@router.get("/all")
async def get_all_transactions(
    service: TransactionService = Depends(TransactionService)
) -> List[BaseResponseSchema]:
    """
    Get all transactions
    """
    return await service.get_all_transactions()


@router.get("/pix")
async def get_all_transactions_pix(
    service: TransactionService = Depends(TransactionService)
) -> List[PixChargeResponseSchema]:
    """
    Get all transactions pix
    """
    return await service.get_all_transactions_pix()


@router.get("/pix/{transaction_id}")
async def get_transaction_pix_by_id(
    transaction_id: int,
    service: TransactionService = Depends(TransactionService),
) -> PixChargeResponseSchema:
    """
    Get transaction pix by id
    """
    return await service.get_transaction_pix_by_id(transaction_id)


@router.get("/boleto")
async def get_all_transactions_boleto(
    service: TransactionService = Depends(TransactionService)
) -> List[BoletoChargeResponseSchema]:
    """
    Get all transactions boleto
    """
    return await service.get_all_transactions_boleto()


@router.get("/boleto/{transaction_id}")
async def get_transaction_boleto_by_id(
    transaction_id: int,
    service: TransactionService = Depends(TransactionService),
) -> BoletoChargeResponseSchema:
    """
    Get transaction boleto by id
    """
    return await service.get_transaction_boleto_by_id(transaction_id)


@router.get("/credit")
async def get_all_transactions_credit_card(
    service: TransactionService = Depends(TransactionService)
) -> List[CreditCardChargeResponseSchema]:
    """
    Get all transactions credit card
    """
    return await service.get_all_transactions_credit_card()


@router.get("/credit/{transaction_id}")
async def get_transaction_credit_card_by_id(
    transaction_id: int,
    service: TransactionService = Depends(TransactionService),
) -> CreditCardChargeResponseSchema:
    """
    Get transaction credit card by id
    """
    return await service.get_transaction_credit_card_by_id(transaction_id)
