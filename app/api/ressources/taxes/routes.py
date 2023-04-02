"""
Description: The file containing FastAPI routes for taxes resource.
"""

## -- 3rd Party Imports -- ##

from fastapi import APIRouter, Request, Depends, Response

## -- Project Imports -- ##

from app.database.base import get_db
from .crud import (get_all_taxes, create_taxes)
from .schemas import (Taxes)

## -- Init APIRouter -- ##

router = APIRouter()

## -- Taxes Routes -- ##

# GET /taxes_declarations
@router.get("/taxes_declarations")
async def list_taxes_declarations(response: Response, db=Depends(get_db)):
    """
    Get all declarations
    """
    taxes = get_all_taxes(db)

    # Necessary for react-admin to work
    response.headers["Content-Range"] = f"0-9/{len(taxes)}"
    
    return taxes

# POST /taxes_declarations
@router.post("/taxes_declarations")
async def create_taxes_declaration(request: Request, taxes: Taxes, db=Depends(get_db)):
    """
    Create declarations
    """
    return create_taxes(db, taxes)