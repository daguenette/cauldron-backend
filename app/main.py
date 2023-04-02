"""
Description: The main application entry point, where you define and configure the FastAPI app instance.
"""

## -- 3rd Party Imports -- ##

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

## -- Project Imports -- ##

from app.api.base import api_router
from app.config import settings

## -- Init FastAPI & Include Router -- ##

app = FastAPI()
app.include_router(api_router)

## -- Add Middleware -- ##

origins = [
    settings.ORIGIN_URL1,
    settings.ORIGIN_URL2
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Range"]
)

## -- Start Server -- ##

def start():
    uvicorn.run(app, port=int(settings.API_PORT), log_level="debug")