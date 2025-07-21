"""
Module contains commands for transactions
"""

from .transaction_base import BaseTransactionService

from ..schemas import (
    PixChargeRequestSchema,
    PixChargeResponseSchema,
)


class TransactionServiceCommand(BaseTransactionService):
    """
    Class contains methods command
    """

    async def create_pix_charge(self, charge: PixChargeRequestSchema) -> PixChargeResponseSchema:
        """
        Create pix charge

        Args:
            charge (PixChargeRequestSchema): PixChargeRequestSchema

        Returns:
            PixChargeResponseSchema: PixChargeResponseSchema
        """

        return PixChargeResponseSchema(
            nome_cliente="UNKNOWN",
            valor="0.00",
            pix_copia_cola="UNKNOWN",
        )
