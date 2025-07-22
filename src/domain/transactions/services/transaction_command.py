"""
Module contains commands for transactions
"""

from datetime import datetime

from .transaction_base import BaseTransactionService

from ..schemas import (
    PixChargeResponseSchema, PixChargeRequestSchema,
    BoletoChargeRequestSchema, BoletoChargeResponseSchema,
    CreditCardChargeRequestSchema, CreditCardChargeResponseSchema
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

    async def create_boleto_charge(
        self,
        charge: BoletoChargeRequestSchema,
    ) -> BoletoChargeResponseSchema:
        """
        Create boleto charge

        Args:
            charge (BoletoChargeRequestSchema): BoletoChargeRequestSchema

        Returns:
            BoletoChargeResponseSchema: BoletoChargeResponseSchema
        """

        return BoletoChargeResponseSchema(
            nome_cliente="UNKNOWN",
            valor="0.00",
            data_vencimento=datetime.now(),
            link_pdf="UNKNOWN",
        )

    async def create_credit_card_charge(
        self,
        charge: CreditCardChargeRequestSchema,
    ) -> CreditCardChargeResponseSchema:
        """
        Create credit card charge

        Args:
            charge (CreditCardChargeRequestSchema): CreditCardChargeRequestSchema

        Returns:
            CreditCardChargeResponseSchema: CreditCardChargeResponseSchema
        """

        return CreditCardChargeResponseSchema(
            nome_cliente="UNKNOWN",
            valor="0.00",
        )
