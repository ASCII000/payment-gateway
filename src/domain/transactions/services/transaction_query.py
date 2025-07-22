"""
Module contains queries for transactions
"""

from datetime import datetime
from typing import List

from .transaction_base import BaseTransactionService

from ..schemas import (
    BaseResponseSchema,
    PixChargeResponseSchema,
    BoletoChargeResponseSchema,
    CreditCardChargeResponseSchema,
)


class TransactionServiceQuery(BaseTransactionService):
    """
    Class contains methods query
    """

    async def get_all_transactions(self) -> List[BaseResponseSchema]:
        """
        Get all transactions

        Returns:
            list[BaseResponseSchema]: list[BaseResponseSchema]
        """
        return []

    async def get_transaction_by_id(self, transaction_id: int) -> BaseResponseSchema:
        """
        Get transaction by id

        Args:
            transaction_id (int): transaction_id

        Returns:
            BaseResponseSchema: BaseResponseSchema
        """
        return BaseResponseSchema(
            gateway_id="UNKNOWN",
            id=transaction_id,
            nome_cliente="UNKNOWN",
            valor="0.00",
        )

    async def get_all_transactions_pix(self) -> List[PixChargeResponseSchema]:
        """
        Get all transactions pix

        Returns:
            list[PixChargeResponseSchema]: list[PixChargeResponseSchema]
        """
        return []

    async def get_all_transactions_boleto(self) -> List[BoletoChargeResponseSchema]:
        """
        Get all transactions boleto

        Returns:
            list[BoletoChargeResponseSchema]: list[BoletoChargeResponseSchema]
        """
        return []

    async def get_all_transactions_credit_card(self) -> List[CreditCardChargeResponseSchema]:
        """
        Get all transactions credit card

        Returns:
            list[CreditCardChargeResponseSchema]: list[CreditCardChargeResponseSchema]
        """
        return []

    async def get_transaction_pix_by_id(self, transaction_id: int) -> PixChargeResponseSchema:
        """
        Get transaction pix by id

        Args:
            transaction_id (int): transaction_id

        Returns:
            PixChargeResponseSchema: PixChargeResponseSchema
        """
        return PixChargeResponseSchema(
            gateway_id="UNKNOWN",
            id=transaction_id,
            nome_cliente="UNKNOWN",
            valor="0.00",
            pix_copia_cola="UNKNOWN",
            expira_em=datetime.now(),
        )

    async def get_transaction_boleto_by_id(self, transaction_id: int) -> BoletoChargeResponseSchema:
        """
        Get transaction boleto by id

        Args:
            transaction_id (int): transaction_id

        Returns:
            BoletoChargeResponseSchema: BoletoChargeResponseSchema
        """
        return BoletoChargeResponseSchema(
            gateway_id="UNKNOWN",
            id=transaction_id,
            nome_cliente="UNKNOWN",
            valor="0.00",
            data_vencimento=datetime.now(),
            link_pdf="UNKNOWN",
        )

    async def get_transaction_credit_card_by_id(
        self,
        transaction_id: int
    ) -> CreditCardChargeResponseSchema:
        """
        Get transaction credit card by id

        Args:
            transaction_id (int): transaction_id

        Returns:
            CreditCardChargeResponseSchema: CreditCardChargeResponseSchema
        """
        return CreditCardChargeResponseSchema(
            gateway_id="UNKNOWN",
            id=transaction_id,
            nome_cliente="UNKNOWN",
            valor="0.00",
        )
