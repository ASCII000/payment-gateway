"""
Module for include routers for domains
"""

from typing import TypedDict, List
from enum import Enum

from fastapi import APIRouter

from .providers.routers import router as providers_router
from .transactions.routers import router as transactions_router


class Tags(Enum):
    """
    Tags for use in routers
    """
    PROVIDERS = "PROVEDORES"
    TRANSACTIONS = "TRANSAÇÕES"


class Routers(TypedDict):
    """
    Routers for domains
    """
    router: APIRouter
    prefix: str
    tags: List[str]


routers: List[Routers] = [
    {"router": providers_router, "prefix": "/v1/providers", "tags": [Tags.PROVIDERS.value]},
    {"router": transactions_router, "prefix": "/v1/transactions", "tags": [Tags.TRANSACTIONS.value]},
]
