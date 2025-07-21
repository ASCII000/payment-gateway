"""
Module contains repositories for transactions
"""

from fastapi import Depends

from dependencies.database import get_db_session


class TransactionsRepository:
    """
    Class contains methods for transactions
    """

    def __init__(self, db_session = Depends(get_db_session)) -> None:
        self.db_session = db_session
