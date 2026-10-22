# Day 149 - Activity 1: Async SQLAlchemy ORM Models & Database Engines
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer

# 1. Setup Async Database Engine (Using SQLite in-memory for lightning-fast async testing)
DATABASE_URL = "sqlite+aiosqlite:///:memory:"
engine = create_async_engine(DATABASE_URL, echo=False, future=True)

# 2. Setup Async Session Factory
async_session_maker = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

# 3. Base Class for ORM Models
class Base(DeclarativeBase):
    pass

# 4. Define Persistent Runner ORM Model
class RunnerORM(Base):
    __tablename__ = "runners"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    runner_id: Mapped[int] = mapped_column(Integer, unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    target_5k_pace: Mapped[str] = mapped_column(String(10), nullable=False)

    def __repr__(self) -> str:
        return f"<RunnerORM(id={self.runner_id}, name='{self.name}', pace='{self.target_5k_pace}')>"

# 5. Async Function to Initialize Database Tables & Test Insertion
async def init_db_and_test():
    print("🚀 Initializing Day 149 Activity 1: Async SQLAlchemy ORM...\n")
    
    # Create database tables asynchronously
    async with engine.begin() as conn:
        print("🛠️ [DATABASE]: Creating database tables from ORM models...")
        await conn.run_sync(Base.metadata.create_all)
    print("✅ [DATABASE]: Tables created successfully!\n")

    # Open an async session and insert a runner
    async with async_session_maker() as session:
        print("📥 [SESSION]: Inserting new runner into SQLite database...")
        new_runner = RunnerORM(
            runner_id=101,
            name="Conix",
            email="conix@example.com",
            target_5k_pace="04:15"
        )
        session.add(new_runner)
        await session.commit()
        print(f"✅ [SUCCESS]: Saved {new_runner} to database!")

        # Query the database asynchronously
        print("\n🔍 [QUERY]: Fetching runner from database...")
        result = await session.get(RunnerORM, 1) # Note: primary key ID is 1
        print(f"📊 Retrieved from DB: {result}")

    # Dispose of engine connection pool
    await engine.dispose()

# Execution Block
if __name__ == "__main__":
    asyncio.run(init_db_and_test())

# Day 149 - Activity 2: FastAPI + Async SQLAlchemy CRUD & Session Dependency
import asyncio
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field
from typing import List
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, select

# 1. Database Engine & Session Setup
DATABASE_URL = "sqlite+aiosqlite:///:memory:"
engine = create_async_engine(DATABASE_URL, echo=False, future=True)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

class RunnerORM(Base):
    __tablename__ = "runners"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    runner_id: Mapped[int] = mapped_column(Integer, unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    target_5k_pace: Mapped[str] = mapped_column(String(10), nullable=False)

# 2. FastAPI App Initialization
app = FastAPI(title="Persistent Runner Microservice", version="2.0.0")

# 3. Database Session Dependency Generator
async def get_db():
    async with async_session_maker() as session:
        yield session

# 4. Pydantic Schemas
class RunnerCreateSchema(BaseModel):
    runner_id: int = Field(..., gt=0)
    name: str = Field(..., min_length=2, max_length=50)
    email: str
    target_5k_pace: str = Field(..., pattern=r"^\d{1,2}:\d{2}$")

class RunnerResponseSchema(RunnerCreateSchema):
    id: int
    class Config:
        from_attributes = True

# 5. Asynchronous POST Endpoint: Save Runner to Database
@app.post("/api/v1/runners", status_code=status.HTTP_201_CREATED, response_model=RunnerResponseSchema)
async def create_runner(runner_data: RunnerCreateSchema, db: AsyncSession = Depends(get_db)):
    print(f"📥 [API POST]: Registering {runner_data.name} into persistent database...")
    
    # Check if runner_id already exists using an async select query
    stmt = select(RunnerORM).where(RunnerORM.runner_id == runner_data.runner_id)
    result = await db.execute(stmt)
    existing_runner = result.scalar_one_or_none()
    
    if existing_runner:
        raise HTTPException(status_code=400, detail="Runner ID already registered in database.")
    
    # Create and commit new ORM record
    new_runner = RunnerORM(**runner_data.model_dump())
    db.add(new_runner)
    await db.commit()
    await db.refresh(new_runner)
    
    print(f"✅ [SUCCESS]: Saved {new_runner.name} with primary key ID {new_runner.id}!")
    return new_runner

# 6. Asynchronous GET Endpoint: Fetch All Runners from Database
@app.get("/api/v1/runners", response_model=List[RunnerResponseSchema])
async def get_all_runners(db: AsyncSession = Depends(get_db)):
    print("📡 [API GET]: Fetching all runners from persistent database...")
    stmt = select(RunnerORM)
    result = await db.execute(stmt)
    runners = result.scalars().all()
    return runners

# 7. Script Execution Test / Direct Verification
async def test_activity_2():
    print("🚀 Testing Day 149 Activity 2: FastAPI + Async SQLAlchemy CRUD...\n")
    
    # Create database tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    # Simulate an async session request
    async with async_session_maker() as session:
        # Create a test runner schema payload
        payload = RunnerCreateSchema(
            runner_id=101,
            name="Conix",
            email="conix@example.com",
            target_5k_pace="04:15"
        )
        
        # Test inserting via our endpoint function logic
        db_runner = RunnerORM(**payload.model_dump())
        session.add(db_runner)
        await session.commit()
        print(f"💾 [TEST DB]: Inserted test runner {db_runner}")
        
        # Test querying via SQLAlchemy select statement
        stmt = select(RunnerORM)
        result = await session.execute(stmt)
        all_db_runners = result.scalars().all()
        print(f"📊 [TEST DB QUERY RESULT]: {all_db_runners}")

if __name__ == "__main__":
    asyncio.run(test_activity_2())

# Day 149 - Activity 3: Async SQLAlchemy Relationships (One-to-Many) & Eager Loading
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, selectinload
from sqlalchemy import String, Integer, ForeignKey, Float, select
from typing import List

# 1. Database Engine Setup
DATABASE_URL = "sqlite+aiosqlite:///:memory:"
engine = create_async_engine(DATABASE_URL, echo=False, future=True)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

# 2. Parent Model: RunnerORM
class RunnerORM(Base):
    __tablename__ = "runners"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    
    # One-to-Many Relationship: One runner has many workouts
    workouts: Mapped[List["WorkoutLogORM"]] = relationship(back_populates="runner", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<RunnerORM(id={self.id}, name='{self.name}')>"

# 3. Child Model: WorkoutLogORM
class WorkoutLogORM(Base):
    __tablename__ = "workout_logs"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    runner_id: Mapped[int] = mapped_column(Integer, ForeignKey("runners.id"), nullable=False)
    distance_km: Mapped[float] = mapped_column(Float, nullable=False)
    workout_type: Mapped[str] = mapped_column(String(30), nullable=False)

    # Many-to-One Back reference
    runner: Mapped["RunnerORM"] = relationship(back_populates="workouts")

    def __repr__(self) -> str:
        return f"<WorkoutLogORM(type='{self.workout_type}', distance={self.distance_km}km)>"

# 4. Script Execution Test / Direct Verification
async def test_activity_3():
    print("🚀 Testing Day 149 Activity 3: Async SQLAlchemy Relationships...\n")
    
    # Create tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    async with async_session_maker() as session:
        print("📥 [RELATIONSHIP]: Creating a runner with multiple workout logs...")
        
        # Create a new runner object with nested workouts
        conix_runner = RunnerORM(name="Conix")
        conix_runner.workouts = [
            WorkoutLogORM(distance_km=5.2, workout_type="Intervals"),
            WorkoutLogORM(distance_km=10.0, workout_type="Long Slow Distance"),
            WorkoutLogORM(distance_km=6.5, workout_type="Tempo Run")
        ]
        
        session.add(conix_runner)
        await session.commit()
        print("✅ [SUCCESS]: Runner and workouts saved with relational foreign keys!\n")
        
        # Query using selectinload to eagerly fetch related workouts asynchronously
        print("🔍 [QUERY]: Fetching runner and eagerly loading related workouts...")
        stmt = (
            select(RunnerORM)
            .options(selectinload(RunnerORM.workouts))
            .where(RunnerORM.name == "Conix")
        )
        result = await session.execute(stmt)
        fetched_runner = result.scalar_one()
        
        print(f"\n📊 Retrieved Runner: {fetched_runner.name}")
        print("🏃‍♂️ Associated Training Sessions:")
        for workout in fetched_runner.workouts:
            print(f"   -> {workout}")

if __name__ == "__main__":
    asyncio.run(test_activity_3())