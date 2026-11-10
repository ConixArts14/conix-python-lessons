from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from app.config import settings
from app.database import engine
from app.models import Base
from app.routers import auth, items

# Initialize database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Modular Production FastAPI App", version="2.0")

# --- 1. Security & CORS Middleware ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    TrustedHostMiddleware, 
    allowed_hosts=["localhost", "127.0.0.1", "testserver"]
)

# --- 2. Register Routers ---
app.include_router(auth.router)
app.include_router(items.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Modular FastAPI Backend with Production Middleware!"}