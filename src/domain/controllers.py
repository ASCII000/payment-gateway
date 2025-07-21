"""
Module for include routers for domains
"""

from typing import TypedDict, List
from enum import Enum

from fastapi import APIRouter

from .manager.routers import router as manager_routers
from .transactions.routers import router as transactions_routers


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
    {"router": manager_routers, "prefix": "/v1/manager", "tags": [Tags.PROVIDERS.value]},
    {"router": transactions_routers, "prefix": "/v1/transactions", "tags": [Tags.TRANSACTIONS.value]},
]
