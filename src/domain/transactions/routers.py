"""
Router for transactions
"""
from fastapi import APIRouter, Depends

from .service import TransactionService
from .schemas import (
    PixChargeRequestSchema, PixChargeResponseSchema
)


router = APIRouter()


@router.post("/create_pix_charge")
async def create_pix_charge(
    charge: PixChargeRequestSchema,
    service: TransactionService = Depends(TransactionService),
) -> PixChargeResponseSchema:
    """
    Create pix charge
    """
    return await service.create_pix_charge(charge)
