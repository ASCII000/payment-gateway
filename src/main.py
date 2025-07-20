"""
Module to run the application and start the necessary processes
for it to work
"""

from fastapi import FastAPI

import uvicorn

from setup import setup


app = FastAPI(
    title=setup.API_NAME,
    description=setup.API_DESCRIPTION,
)


if __name__=="__main__":
    uvicorn.run(
        "main:app",
        host=setup.API_HOST,
        port=setup.API_PORT,
        reload=setup.API_RELOAD,
    )
