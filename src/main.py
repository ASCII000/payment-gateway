"""
Module to run the application and start
the necessary processes for it to work
"""

from fastapi import FastAPI

import uvicorn

from setup import setup
from domain.controllers import routers
from dependencies.lifespan import lifespan


app = FastAPI(
    lifespan=lifespan,
    title=setup.API_NAME,
    description=setup.API_DESCRIPTION,
)

for router in routers:
    app.include_router(
        router["router"],
        prefix=router["prefix"],
        tags=router["tags"],
    )


if __name__=="__main__":
    uvicorn.run(
        "main:app",
        host=setup.API_HOST,
        port=setup.API_PORT,
        reload=setup.API_RELOAD,
    )
