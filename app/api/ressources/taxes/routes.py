from fastapi import APIRouter, Request, Depends, Response
from app.database.base import get_db
from .crud import (get_taxes, create_taxes)
from .schemas import (Taxes)

router = APIRouter()

@router.get("/taxes_declarations")
async def list_declarations(response: Response, db=Depends(get_db)):
    """
    Get all declarations
    """
    taxes = get_taxes(db)

    # Necessary for react-admin to work
    response.headers["Content-Range"] = f"0-9/{len(taxes)}"
    
    return taxes

@router.post("/taxes_declarations")
async def declaration_create(request: Request, taxes: Taxes, db=Depends(get_db)):
    """
    Create declarations
    """
    return create_taxes(db, taxes)