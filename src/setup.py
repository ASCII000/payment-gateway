# pylint: disable=invalid-name, too-few-public-methods, too-many-instance-attributes

"""
Module for import setup
"""

import os
from typing import TypeVar, Type
import logging

from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from sqlmodel import SQLModel

from dotenv import dotenv_values

from database.tables import *  # pylint: disable=wildcard-import, unused-wildcard-import


T = TypeVar("T")

class Setup:
    """
    Class contains the environment variables
    and database connection
    """

    def __init__(self):
        """
        Attrs:
            API_PORT : porta da api
            API_NAME: nome da api
            API_HOST: host da api
            API_DESCRIPTION: descricao da api
        """

        self.env = dotenv_values(".env")

        self.API_RELOAD = self.get_env("API_RELOAD", False, bool)
        self.API_PORT = self.get_env("API_PORT", 8000, int)
        self.API_NAME = self.get_env("API_NAME", "API", str)
        self.API_HOST = self.get_env("API_HOST", "0.0.0.0", str)
        self.API_DESCRIPTION = self.get_env(
            "API_DESCRIPTION", "API Payment Gateways", str
        )

        self.SQLITE_DB_PATH = self.get_env(
            "SQLITE_DB_PATH", "./db/sqlite.db", str
        )

    def create_sqlite_db_folder(self) -> None:
        """
        Create database folder
        """
        os.makedirs(os.path.dirname(self.SQLITE_DB_PATH), exist_ok=True)

    async def create_relational_db_engine(self) -> AsyncEngine:
        """
        Create database engine with sqlite db path
        """

        # Create the database folder
        self.create_sqlite_db_folder()

        # Setup engine
        db_url = f"sqlite+aiosqlite:///{self.SQLITE_DB_PATH}"
        engine = create_async_engine(db_url)

        # Create tables
        await self.create_tables(engine)

        # Return engine
        return engine

    async def create_tables(self, engine: AsyncEngine) -> None:
        """
        Create tables in database

        Args:
            engine: Database engine
        """

        # Create tables
        async with engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)

    def get_env(
        self,
        value: str,
        default_value: str = None,
        type_value: Type[T] = str,
    ) -> T:
        """
        Get the value of the environment variable
        
        Args:
            value: The name of the environment variable
            default_value: The default value to use if the environment variable is not set
            type_value (Type): The type of the environment variable
        
        Returns:
            (TypeVar): The value of the environment variable
        """

        try:

            # Try to get the value of the environment variable
            result = self.env.get(value, default_value)
            return type_value(result) if result is not None else default_value

        except ValueError as err:

            # If not getter the value of the environment variable
            # return the default value case not default value
            # raise the error
            if default_value is None:
                raise ValueError(
                    "Variavel de ambiente nao compativel com o tipo "
                    f"esperado: {type_value.__name__}"
                ) from err

            logging.warning(
                "Variavel %s nao encontrada usando o valor padrao: %s",
                value, default_value
            )

            return default_value


setup = Setup()
