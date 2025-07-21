"""
Module contains base for transactions
"""

from fastapi import Depends

from database.repositories.transactions import TransactionsRepository


class BaseTransactionService:
    """
    Class base for transactions
    """
    def __init__(
            self, repositorie: TransactionsRepository = Depends(TransactionsRepository)
    ):
        """
        Args:
            repositorie (TransactionsRepository): TransactionsRepository
        """
        self.repositorie = repositorie
