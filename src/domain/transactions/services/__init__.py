"""
Module contains base class and import (CQRS) for transactions
"""
from .transaction_command import TransactionServiceCommand
from .transaction_query import TransactionServiceQuery


class TransactionService(TransactionServiceCommand, TransactionServiceQuery):
    """
    Class contains methods for transactions
    """
