# Day 153 - Activity 1: Database Setup with SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Define the SQLite database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./runner_app.db"

# 2. Create the SQLAlchemy Engine
# (check_same_thread=False is needed only for SQLite in multi-threaded FastAPI apps)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 3. Create a SessionLocal class for database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Create a Base class for ORM models to inherit from
Base = declarative_base()

# Dependency helper to manage DB sessions in FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Day 153 - Activity 2: Pydantic Schemas for Request & Response Validation
from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    is_active: bool

    class Config:
        from_attributes = True  # Allows Pydantic to read data from SQLAlchemy ORM models

# Day 153 - Activity 2: FastAPI Endpoints with SQLAlchemy ORM
import bcrypt
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from database import engine, get_db, Base
import models
import schemas

# Create database tables automatically if they don't exist yet
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Runner Microservice - Database & ORM API")

@app.post("/users/", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """Register a new user, hash their password, and save them to SQLite via SQLAlchemy."""
    # 1. Check if the username already exists in the database
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )
    
    # 2. Hash the password using bcrypt (carrying over our Day 152 security standard!)
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    # 3. Create the SQLAlchemy User model instance
    new_user = models.User(
        username=user.username,
        hashed_password=hashed_password
    )
    
    # 4. Add to session, commit the transaction, and refresh the instance
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

@app.get("/users/", response_model=list[schemas.UserResponse])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Retrieve a list of all registered users from the database."""
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users

# Day 153 - Activity 3: Automated Testing for Database Endpoints
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base, get_db
from main_db import app

# 1. Use an in-memory SQLite database for testing isolation
SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_TEST_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 2. Override the get_db dependency for tests
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# 3. Create fresh tables in the in-memory test database
Base.metadata.create_all(bind=engine)

client = TestClient(app)

def test_create_user_success():
    """Test creating a new user in the database."""
    response = client.post(
        "/users/",
        json={"username": "testrunner@mastery.com", "password": "TestPassword123!"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "testrunner@mastery.com"
    assert "id" in data
    assert data["is_active"] is True

def test_create_duplicate_user_fails():
    """Test that attempting to register a duplicate username returns HTTP 400."""
    user_payload = {"username": "duplicate@mastery.com", "password": "Password123!"}
    
    # First registration
    client.post("/users/", json=user_payload)
    
    # Second registration with the same username
    response = client.post("/users/", json=user_payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "Username already registered"

def test_read_users():
    """Test retrieving all users from the database."""
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)