from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None

from fastapi import FastAPI
from app.routers import auth

app = FastAPI(title="Secure FastAPI Backend")

# Include authentication router
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI Backend with Authentication!"}