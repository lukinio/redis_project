from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import app_routes
from app.utils import get_logger

logger = get_logger(__name__)
app = FastAPI(title="Docker, FastAPI, redis")

# Handle CORS protection
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(app_routes)
