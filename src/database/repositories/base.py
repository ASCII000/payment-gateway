"""
Module contains base for repositories
"""

from fastapi import Depends

from dependencies.database import get_db_session


class BaseRepository:
    """
    Class base for repositories
    """

    def __init__(self, db_session = Depends(get_db_session)) -> None:
        self.session = db_session
