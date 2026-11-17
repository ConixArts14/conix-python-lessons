from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models import User, Item
from app.schemas import ItemCreate, ItemUpdate, ItemResponse
from app.security import get_current_user

router = APIRouter(prefix="/items", tags=["Items"])