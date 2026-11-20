from datetime import datetime, timezone
from typing import Literal
from fastapi import FastAPI, APIRouter, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, Session, relationship, joinedload, selectinload

# 1. Database Setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./day178.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# 2. Relational SQLAlchemy Models (One-to-Many with Cascading Deletes)
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)

    items = relationship("Item", back_populates="owner", cascade="all, delete-orphan")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("User", back_populates="items")


Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 3. Pydantic v2 Schemas
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


# 4. App & Global Exception Handlers
app = FastAPI(title="Day 178 — Eager Loading & Query Optimization")


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": {
                "code": exc.status_code,
                "message": exc.detail,
                "path": request.url.path,
                "timestamp": datetime.now(timezone.utc).isoformat(),
            },
        },
    )


@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": {
                "code": 500,
                "message": "An unexpected internal server error occurred.",
                "path": request.url.path,
                "timestamp": datetime.now(timezone.utc).isoformat(),
            },
        },
    )


# 5. Routers with Eager Loading
users_router = APIRouter(prefix="/users", tags=["Users"])
items_router = APIRouter(prefix="/items", tags=["Items"])


@users_router.post("/", response_model=UserResponse, status_code=201)
def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(
        (User.email == payload.email) | (User.username == payload.username)
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username or email already registered")

    user = User(username=payload.username, email=payload.email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@users_router.get("/{user_id}", response_model=UserWithItemsResponse)
def get_user_with_items(user_id: int, db: Session = Depends(get_db)):
    # selectinload fetches all related items in a clean follow-up IN query (avoids N+1)
    user = (
        db.query(User)
        .options(selectinload(User.items))
        .filter(User.id == user_id)
        .first()
    )
    if not user:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    return user


@users_router.delete("/{user_id}", status_code=200)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")

    db.delete(user)
    db.commit()
    return {"deleted": True, "user_id": user_id}


@items_router.post("/user/{user_id}", response_model=ItemWithOwnerResponse, status_code=201)
def create_item_for_user(user_id: int, payload: ItemCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")

    item = Item(title=payload.title, description=payload.description, owner_id=user.id)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@items_router.get("/", response_model=PaginatedItemResponse)
def list_items_with_owners(
    skip: int = 0,
    limit: int = 10,
    search: str | None = None,
    sort_by: Literal["id", "title"] = "id",
    order: Literal["asc", "desc"] = "desc",
    db: Session = Depends(get_db),
):
    query = db.query(Item)

    if search:
        query = query.filter(Item.title.ilike(f"%{search}%"))

    total = query.count()

    sort_column = getattr(Item, sort_by)
    query = query.order_by(sort_column.desc() if order == "desc" else sort_column.asc())

    # joinedload loads each Item's owner via SQL JOIN in the same query (prevents N+1)
    items = query.options(joinedload(Item.owner)).offset(skip).limit(limit).all()

    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "items": items,
    }


app.include_router(users_router)
app.include_router(items_router)

import os
from contextlib import contextmanager
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker

from Day_178_Python_Developer_Mastery import app, Base, get_db

TEST_DB_URL = "sqlite:///./test_day178.db"
engine = create_engine(TEST_DB_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@contextmanager
def count_queries(target_engine):
    """Count SQL statements executed on target_engine within this block."""
    executed_statements: list[str] = []

    def before_cursor_execute(conn, cursor, statement, parameters, context, executemany):
        executed_statements.append(statement)

    event.listen(target_engine, "before_cursor_execute", before_cursor_execute)
    try:
        yield executed_statements
    finally:
        event.remove(target_engine, "before_cursor_execute", before_cursor_execute)


@pytest.fixture(autouse=True)
def reset_database():
    app.dependency_overrides[get_db] = override_get_db
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)
    engine.dispose()
    if os.path.exists("./test_day178.db"):
        try:
            os.remove("./test_day178.db")
        except PermissionError:
            pass


client = TestClient(app)


def test_list_items_avoids_n_plus_one_queries():
    # Create two users and 6 items across them
    u1 = client.post("/users/", json={"username": "alpha", "email": "alpha@example.com"}).json()["id"]
    u2 = client.post("/users/", json={"username": "beta", "email": "beta@example.com"}).json()["id"]

    for i in range(4):
        client.post(f"/items/user/{u1}", json={"title": f"Alpha Task {i}"})
    for i in range(2):
        client.post(f"/items/user/{u2}", json={"title": f"Beta Task {i}"})

    with count_queries(engine) as statements:
        res = client.get("/items/?limit=10")

    assert res.status_code == 200
    payload = res.json()
    assert payload["total"] == 6
    assert len(payload["items"]) == 6
    assert all("owner" in item and "username" in item["owner"] for item in payload["items"])

    # Expect only 2 queries: 1 COUNT(*) + 1 SELECT ... FROM items LEFT OUTER JOIN users
    assert len(statements) == 2


def test_user_detail_uses_selectinload_without_n_plus_one():
    user_id = client.post(
        "/users/", json={"username": "sprinter", "email": "sprinter@example.com"}
    ).json()["id"]

    for i in range(5):
        client.post(f"/items/user/{user_id}", json={"title": f"Interval {i}"})

    with count_queries(engine) as statements:
        res = client.get(f"/users/{user_id}")

    assert res.status_code == 200
    body = res.json()
    assert body["username"] == "sprinter"
    assert len(body["items"]) == 5

    # Expect only 2 queries: 1 SELECT users + 1 SELECT items WHERE items.owner_id IN (...)
    assert len(statements) == 2