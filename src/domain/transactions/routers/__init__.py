"""
Module for initialize routers
"""

from fastapi import APIRouter

from .routers_command import router as transactions_routers_command
from .routers_query import router as transactions_routers_query


router = APIRouter()
router.include_router(transactions_routers_command, prefix="/charge")
router.include_router(transactions_routers_query, prefix="/query")

__all__ = ["router"]
