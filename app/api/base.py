"""
Description: The file containing the base API router, which other routers should be added to.
"""

## -- 3rd Party Imports -- ## 

from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse

## -- Project Imports -- ##

from app.api.ressources.taxes.routes import router as taxes_routes

## -- Add API Router & Resource Routes -- ##

api_router = APIRouter()

# Register resource routers here
api_router.include_router(taxes_routes, tags=["Taxes"])

## -- Base Routes -- ##

@api_router.get('/')
async def read_taxes(response: Response):
    content = {"Hello World": "My API"}
    headers = {"Access-Control-Expose-Headers": "Content-Range", "Content-Range": "taxes 0-24/319"}
    return JSONResponse(content=content, headers=headers)