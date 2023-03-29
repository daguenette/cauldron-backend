from app.taxes_allocations.helpers.terminal_output import execute
from fastapi import APIRouter, FastAPI, Depends, Response, status, APIRouter
from app.declaration import routes as declaration_routes
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi.responses import JSONResponse

origins = [
    "http://localhost:5173",
    "localhost:5173"
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Range"]
)

app.include_router(declaration_routes.router)

@app.get('/')
async def read_taxes(response: Response):
    content = {"Hello World": "My API"}
    headers = {"Access-Control-Expose-Headers": "Content-Range", "Content-Range": "taxes 0-24/319"}
    return JSONResponse(content=content, headers=headers)

def start():
    uvicorn.run(app, port=8001, log_level="debug")
    # execute()

if __name__ == "__main__":
    start()