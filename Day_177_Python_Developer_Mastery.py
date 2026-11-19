from datetime import datetime, timezone
from typing import Literal
from fastapi import FastAPI, APIRouter, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, Session, relationship

# 1. Database Setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./day177.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 2. Relational SQLAlchemy Models (One-to-Many with Cascading Deletes)
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)

    # One User -> Many Items (automatically deletes child items if user is deleted)
    items = relationship("Item", back_populates="owner", cascade="all, delete-orphan")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    # Many Items -> One User
    owner = relationship("User", back_populates="items")


Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class UserCreate(BaseModel):
    username: str
    email: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    model_config = {"from_attributes": True}


class ItemCreate(BaseModel):
    title: str
    description: str | None = None


class ItemResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    owner_id: int
    model_config = {"from_attributes": True}


class ItemWithOwnerResponse(ItemResponse):
    owner: UserResponse


class UserWithItemsResponse(UserResponse):
    items: list[ItemResponse] = []


class PaginatedItemResponse(BaseModel):
    total: int
    skip: int
    limit: int
    items: list[ItemWithOwnerResponse]