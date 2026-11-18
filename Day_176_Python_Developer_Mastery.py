from typing import Literal
from fastapi import FastAPI, APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session

# 1. Database Setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./day176.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 2. Pydantic Schemas
class ItemResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    model_config = {"from_attributes": True}

class PaginatedItemResponse(BaseModel):
    total: int
    skip: int
    limit: int
    items: list[ItemResponse]

# 3. Router & App Initialization
app = FastAPI(title="Day 176 API")
router = APIRouter(prefix="/items", tags=["Items"])

@router.get("/", response_model=PaginatedItemResponse)
def get_my_items(
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

    items = query.offset(skip).limit(limit).all()

    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "items": items
    }

app.include_router(router)

