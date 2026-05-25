from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from backend.database import engine
from backend.database import Base

from backend import models
from backend.api import router



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {
        "message": "Currency Agent Backend + PostgreSQL Connected"
    }
    
    
@app.get("/add")
def add(a, b):
    return a + b
print(add(2,4))