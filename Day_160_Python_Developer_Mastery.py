from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks
from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session
from pydantic import BaseModel, EmailStr
from typing import List, Optional
import time

# --- 1. Database Setup ---
SQLALCHEMY_DATABASE_URL = "sqlite:///./runner_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- 2. SQLAlchemy Models ---
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    posts = relationship("Post", back_populates="owner")

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    content = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="posts")

# Create database tables automatically
Base.metadata.create_all(bind=engine)

# --- 3. Pydantic Schemas ---
class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    user_id: int

    class Config:
        from_attributes = True

class UserResponse(BaseModel):
    id: int
    username: str
    email: Optional[str] = None
    is_active: bool
    posts: List[PostResponse] = []

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# --- 4. FastAPI App Initialization ---
app = FastAPI(title="Day 160 Async & Background Tasks API", version="1.0")

# --- 5. Simulated Background Task ---
def send_welcome_email(email: str):
    time.sleep(2)  # Simulate a 2-second delay for sending email in the background
    print(f"📧 [Background Task] Welcome email successfully sent to {email}!")

# --- 6. Endpoints ---
@app.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=user.password 
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    # Add sending welcome email to background tasks
    background_tasks.add_task(send_welcome_email, user.email)
    
    return new_user

@app.get("/users/", response_model=List[UserResponse])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(User).offset(skip).limit(limit).all()
    return users

@app.get("/")
def root():
    return {"message": "Welcome to Day 160 Async & Background Tasks API!"}

from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks
from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session
from pydantic import BaseModel, EmailStr
from typing import List, Optional
import time

# --- 1. Database Setup ---
SQLALCHEMY_DATABASE_URL = "sqlite:///./runner_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- 2. SQLAlchemy Models ---
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    posts = relationship("Post", back_populates="owner")

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    content = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="posts")

# Create database tables automatically
Base.metadata.create_all(bind=engine)

# --- 3. Pydantic Schemas ---
class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    user_id: int

    class Config:
        from_attributes = True

class UserResponse(BaseModel):
    id: int
    username: str
    email: Optional[str] = None
    is_active: bool
    posts: List[PostResponse] = []

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# --- 4. FastAPI App Initialization ---
app = FastAPI(title="Day 160 Async & Multiple Background Tasks API", version="1.0")

# --- 5. Background Task Functions ---
def send_welcome_email(email: str):
    time.sleep(2)  # Simulate email dispatch delay
    print(f"📧 [Background Task 1] Welcome email successfully sent to {email}!")

def log_user_signup_activity(username: str):
    time.sleep(1)  # Simulate database logging delay
    print(f"📊 [Background Task 2] Analytics logged: User '{username}' successfully registered!")

# --- 6. Endpoints ---
@app.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=user.password 
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    # Queue multiple background tasks
    background_tasks.add_task(send_welcome_email, user.email)
    background_tasks.add_task(log_user_signup_activity, user.username)
    
    return new_user

@app.get("/users/", response_model=List[UserResponse])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(User).offset(skip).limit(limit).all()
    return users

@app.get("/")
def root():
    return {"message": "Welcome to Day 160 Async & Multiple Background Tasks API!"}