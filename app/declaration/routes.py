from fastapi import APIRouter, Request, Depends, Response, encoders
import typing as t

from app.db.session import get_db
from app.db.crud import (get_declarations, create_declaration)
from app.db.schemas import (DeclarionBase)

router = APIRouter()

@router.get("/declarations")
async def list_declarations(response: Response, db=Depends(get_db)):
    """
    Get all declarations
    """
    declarations = get_declarations(db)

    # Necessary for react-admin to work
    response.headers["Content-Range"] = f"0-9/{len(declarations)}"
    
    return declarations

@router.post("/declarations")
async def declaration_create(request: Request, declaration: DeclarionBase, db=Depends(get_db)):
    """
    Create declarations
    """
    return create_declaration(db, declaration)