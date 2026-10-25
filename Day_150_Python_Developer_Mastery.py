# 7. Script Execution Test / Direct Verification
async def test_capstone():
    print("🚀 Testing Day 150 Capstone: Full-Stack Microservice Integration...\n")

    # Create database tables first!
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with async_session_maker() as session:
        # Test direct insertion
        test_runner = RunnerORM(runner_id=999, name="Conix Milestone", email="conix150@example.com", target_5k_pace="04:00")
        session.add(test_runner)
        await session.commit()

        # Test query
        stmt = select(RunnerORM).where(RunnerORM.runner_id == 999)
        res = await session.execute(stmt)
        print(f"📊 [VERIFICATION QUERY]: {res.scalar_one()}")

# Day 150 - Milestone Capstone: Full-Stack Async FastAPI & SQLAlchemy Microservice
import asyncio
from typing import List
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, select

# 1. Database Engine & Session Setup
DATABASE_URL = "sqlite+aiosqlite:///runner_telemetry.db"
engine = create_async_engine(DATABASE_URL, echo=False, future=True)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

# 2. SQLAlchemy ORM Model
class RunnerORM(Base):
    __tablename__ = "runners"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    runner_id: Mapped[int] = mapped_column(Integer, unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    target_5k_pace: Mapped[str] = mapped_column(String(10), nullable=False)

# 3. FastAPI Lifespan Handler (Creates database tables on app startup!)
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🔌 [LIFESPAN]: Starting up Runner Telemetry Service...")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ [LIFESPAN]: Database tables verified and ready!")
    yield
    print("🛑 [LIFESPAN]: Shutting down database connections...")
    await engine.dispose()
    print("🔒 [LIFESPAN]: Shutdown complete.")

# Initialize FastAPI App
app = FastAPI(
    title="Runner Telemetry Production Microservice",
    version="3.0.0",
    lifespan=lifespan
)

# 4. Session Dependency Injection
async def get_db():
    async with async_session_maker() as session:
        yield session

# 5. Pydantic Request & Response Schemas
class RunnerCreateSchema(BaseModel):
    runner_id: int = Field(..., gt=0)
    name: str = Field(..., min_length=2, max_length=50)
    email: str
    target_5k_pace: str = Field(..., pattern=r"^\d{1,2}:\d{2}$")

class RunnerResponseSchema(RunnerCreateSchema):
    id: int
    class Config:
        from_attributes = True

# 6. Live API Endpoints
@app.post("/api/v1/runners", status_code=status.HTTP_201_CREATED, response_model=RunnerResponseSchema)
async def register_runner(runner_data: RunnerCreateSchema, db: AsyncSession = Depends(get_db)):
    print(f"📥 [API POST]: Registering runner '{runner_data.name}' into SQLite DB...")

    # Check if runner already exists
    stmt = select(RunnerORM).where(RunnerORM.runner_id == runner_data.runner_id)
    result = await db.execute(stmt)
    if result.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Runner ID already registered.")

    # Save to SQLite database
    new_runner = RunnerORM(**runner_data.model_dump())
    db.add(new_runner)
    await db.commit()
    await db.refresh(new_runner)

    print(f"✅ [SUCCESS]: Saved {new_runner.name} with DB Primary Key #{new_runner.id}!")
    return new_runner

@app.get("/api/v1/runners", response_model=List[RunnerResponseSchema])
async def get_runners(db: AsyncSession = Depends(get_db)):
    print("📡 [API GET]: Querying all runners from persistent database...")
    stmt = select(RunnerORM)
    result = await db.execute(stmt)
    return result.scalars().all()

# Day 150 - Milestone Capstone: Relational Full-Stack Async FastAPI & SQLAlchemy Microservice
import asyncio
from typing import List
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, selectinload
from sqlalchemy import String, Integer, Float, ForeignKey, select

# 1. Database Engine & Session Setup
DATABASE_URL = "sqlite+aiosqlite:///runner_telemetry_relational.db"
engine = create_async_engine(DATABASE_URL, echo=False, future=True)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

# 2. Parent Model: RunnerORM
class RunnerORM(Base):
    __tablename__ = "runners"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    runner_id: Mapped[int] = mapped_column(Integer, unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    target_5k_pace: Mapped[str] = mapped_column(String(10), nullable=False)

    # One-to-Many Relationship
    workouts: Mapped[List["WorkoutLogORM"]] = relationship(back_populates="runner", cascade="all, delete-orphan")

# 3. Child Model: WorkoutLogORM
class WorkoutLogORM(Base):
    __tablename__ = "workout_logs"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    runner_db_id: Mapped[int] = mapped_column(Integer, ForeignKey("runners.id"), nullable=False)
    distance_km: Mapped[float] = mapped_column(Float, nullable=False)
    workout_type: Mapped[str] = mapped_column(String(30), nullable=False)

    # Many-to-One Back reference
    runner: Mapped["RunnerORM"] = relationship(back_populates="workouts")

# 4. FastAPI Lifespan Handler
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🔌 [LIFESPAN]: Starting up Relational Telemetry Service...")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ [LIFESPAN]: Database tables created successfully!")
    yield
    print("🛑 [LIFESPAN]: Shutting down database...")
    await engine.dispose()

app = FastAPI(title="Relational Runner Telemetry Microservice", version="3.5.0", lifespan=lifespan)

# 5. Session Dependency
async def get_db():
    async with async_session_maker() as session:
        yield session

# 6. Pydantic Schemas (Including Nested Response Schemas)
class RunnerCreateSchema(BaseModel):
    runner_id: int = Field(..., gt=0)
    name: str = Field(..., min_length=2, max_length=50)
    email: str
    target_5k_pace: str = Field(..., pattern=r"^\d{1,2}:\d{2}$")

class WorkoutCreateSchema(BaseModel):
    distance_km: float = Field(..., gt=0)
    workout_type: str = Field(..., min_length=2, max_length=30)

class WorkoutResponseSchema(WorkoutCreateSchema):
    id: int
    class Config:
        from_attributes = True

class RunnerWithWorkoutsResponseSchema(RunnerCreateSchema):
    id: int
    workouts: List[WorkoutResponseSchema] = []
    class Config:
        from_attributes = True

# 7. API Endpoints
@app.post("/api/v1/runners", status_code=status.HTTP_201_CREATED, response_model=RunnerCreateSchema)
async def register_runner(runner_data: RunnerCreateSchema, db: AsyncSession = Depends(get_db)):
    stmt = select(RunnerORM).where(RunnerORM.runner_id == runner_data.runner_id)
    result = await db.execute(stmt)
    if result.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Runner ID already registered.")

    new_runner = RunnerORM(**runner_data.model_dump())
    db.add(new_runner)
    await db.commit()
    return new_runner

@app.post("/api/v1/runners/{runner_id}/workouts", status_code=status.HTTP_201_CREATED, response_model=WorkoutResponseSchema)
async def add_workout_to_runner(runner_id: int, workout_data: WorkoutCreateSchema, db: AsyncSession = Depends(get_db)):
    # Find the parent runner by runner_id
    stmt = select(RunnerORM).where(RunnerORM.runner_id == runner_id)
    result = await db.execute(stmt)
    runner = result.scalar_one_or_none()

    if not runner:
        raise HTTPException(status_code=404, detail="Runner not found.")

    # Create child workout linked to parent's primary key ID
    new_workout = WorkoutLogORM(
        runner_db_id=runner.id,
        distance_km=workout_data.distance_km,
        workout_type=workout_data.workout_type
    )
    db.add(new_workout)
    await db.commit()
    await db.refresh(new_workout)
    return new_workout

@app.get("/api/v1/runners/with-workouts", response_model=List[RunnerWithWorkoutsResponseSchema])
async def get_runners_with_workouts(db: AsyncSession = Depends(get_db)):
    # Query all runners and eagerly load their workouts asynchronously using selectinload
    stmt = select(RunnerORM).options(selectinload(RunnerORM.workouts))
    result = await db.execute(stmt)
    return result.scalars().all()

    