"""
Module contains dependencies for database
"""

from typing import AsyncGenerator, AsyncContextManager, Callable

from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession


async def get_db_session(request: Request) -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency that yields a database async session.
    
    Notes:
        This method is used to get the database session from the request state
        and commit or rollback the session if an exception is raised
    """

    session_maker: Callable[[], AsyncContextManager[AsyncSession]] = request.app.state.db_session

    async with session_maker() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
