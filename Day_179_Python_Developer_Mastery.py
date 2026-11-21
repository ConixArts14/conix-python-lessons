import os
from contextlib import contextmanager
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker

from Day_179_Python_Developer_Mastery import app, Base, get_db

TEST_DB_URL = "sqlite:///./test_day179.db"
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
    if os.path.exists("./test_day179.db"):
        try:
            os.remove("./test_day179.db")
        except PermissionError:
            pass


client = TestClient(app)


def test_filter_items_by_owner_and_search_without_n_plus_one():
    u1 = client.post("/users/", json={"username": "conix", "email": "conix@example.com"}).json()["id"]
    u2 = client.post("/users/", json={"username": "pacer", "email": "pacer@example.com"}).json()["id"]

    client.post(f"/items/user/{u1}", json={"title": "5K Uphill Split", "description": "Hill workout"})
    client.post(f"/items/user/{u1}", json={"title": "FastAPI Router Notes", "description": "PATCH endpoint"})
    client.post(f"/items/user/{u2}", json={"title": "5K Tempo Split", "description": "Steady pace"})

    with count_queries(engine) as statements:
        res = client.get(f"/items/?owner_id={u1}&search=Split&limit=10")

    assert res.status_code == 200
    body = res.json()
    assert body["total"] == 1
    assert len(body["items"]) == 1
    assert body["items"][0]["title"] == "5K Uphill Split"
    assert body["items"][0]["owner"]["username"] == "conix"
    assert len(statements) == 2


def test_patch_item_updates_fields_and_handles_missing_id():
    user_id = client.post(
        "/users/", json={"username": "builder", "email": "builder@example.com"}
    ).json()["id"]
    created = client.post(
        f"/items/user/{user_id}",
        json={"title": "Draft Spec", "description": "Initial version"},
    ).json()

    patch_res = client.patch(
        f"/items/{created['id']}",
        json={"title": "Final Spec"},
    )
    assert patch_res.status_code == 200
    updated = patch_res.json()
    assert updated["title"] == "Final Spec"
    assert updated["description"] == "Initial version"
    assert updated["owner"]["id"] == user_id

    missing_res = client.patch("/items/99999", json={"title": "Ghost Item"})
    assert missing_res.status_code == 404
    err = missing_res.json()
    assert err["success"] is False
    assert err["error"]["code"] == 404

from datetime import datetime, timezone
from typing import Literal
from fastapi import FastAPI, APIRouter, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, or_
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker, declarative_base, Session, relationship, joinedload, selectinload

# 1. Database Setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./day179.db"
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
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), index=True, nullable=False)

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


class ItemUpdate(BaseModel):
    title: str | None = None
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
app = FastAPI(title="Day 179 — Relational Filtering & PATCH Updates")


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


# 5. Routers with Relational Filtering, Eager Loading & PATCH Support
users_router = APIRouter(prefix="/users", tags=["Users"])
items_router = APIRouter(prefix="/items", tags=["Items"])


@users_router.post("/", response_model=UserResponse, status_code=201)
def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(
        (User.email == payload.email) | (User.username == payload.username)
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username or email already registered")

    try:
        user = User(username=payload.username, email=payload.email)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to create user")


@users_router.get("/{user_id}", response_model=UserWithItemsResponse)
def get_user_with_items(user_id: int, db: Session = Depends(get_db)):
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

    try:
        db.delete(user)
        db.commit()
        return {"deleted": True, "user_id": user_id}
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to delete user")


@items_router.post("/user/{user_id}", response_model=ItemWithOwnerResponse, status_code=201)
def create_item_for_user(user_id: int, payload: ItemCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")

    try:
        item = Item(title=payload.title, description=payload.description, owner_id=user.id)
        db.add(item)
        db.commit()
        db.refresh(item)
        return item
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to create item")


@items_router.get("/", response_model=PaginatedItemResponse)
def list_items_with_owners(
    skip: int = 0,
    limit: int = 10,
    owner_id: int | None = None,
    search: str | None = None,
    sort_by: Literal["id", "title"] = "id",
    order: Literal["asc", "desc"] = "desc",
    db: Session = Depends(get_db),
):
    query = db.query(Item)

    if owner_id is not None:
        query = query.filter(Item.owner_id == owner_id)

    if search:
        pattern = f"%{search}%"
        query = query.filter(or_(Item.title.ilike(pattern), Item.description.ilike(pattern)))

    total = query.count()

    sort_column = getattr(Item, sort_by)
    query = query.order_by(sort_column.desc() if order == "desc" else sort_column.asc())

    items = query.options(joinedload(Item.owner)).offset(skip).limit(limit).all()

    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "items": items,
    }


@items_router.patch("/{item_id}", response_model=ItemWithOwnerResponse)
def patch_item(item_id: int, payload: ItemUpdate, db: Session = Depends(get_db)):
    item = db.query(Item).options(joinedload(Item.owner)).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")

    updates = payload.model_dump(exclude_unset=True)
    for field, value in updates.items():
        setattr(item, field, value)

    try:
        db.commit()
        db.refresh(item)
        return item
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to update item")


app.include_router(users_router)
app.include_router(items_router)