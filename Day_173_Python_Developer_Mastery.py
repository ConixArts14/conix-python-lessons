from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    # Relationship to user-owned items
    items = relationship("Item", back_populates="owner", cascade="all, delete-orphan")

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, index=True, nullable=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Relationship back to User
    owner = relationship("User", back_populates="items")


from fastapi import FastAPI
from app.routers import auth, items

app = FastAPI(title="Secure FastAPI Backend")

# Include routers
app.include_router(auth.router)
app.include_router(items.router)

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI Backend with Authentication!"}