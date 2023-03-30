from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from app.api.base import api_router
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()
app.include_router(api_router)

# Middleware setup
origins = [
    "http://localhost:5173",
    "localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Range"]
)

@app.get('/')
async def read_taxes(response: Response):
    content = {"Hello World": "My API"}
    headers = {"Access-Control-Expose-Headers": "Content-Range", "Content-Range": "taxes 0-24/319"}
    return JSONResponse(content=content, headers=headers)


def start():
    uvicorn.run(app, port=8001, log_level="debug")

if __name__ == "__main__":
    start()