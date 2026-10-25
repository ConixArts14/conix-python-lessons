# Day 151 - Activity 2: Automated Testing for Success & Error Handling
import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, select
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field
from typing import List

# 1. Test Database Setup
TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"
test_engine = create_async_engine(TEST_DATABASE_URL, echo=False, future=True)
test_async_session_maker = async_sessionmaker(test_engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

class RunnerORM(Base):
    __tablename__ = "runners"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    runner_id: Mapped[int] = mapped_column(Integer, unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    target_5k_pace: Mapped[str] = mapped_column(String(10), nullable=False)

# 2. FastAPI App Instance with Duplicate Validation
app = FastAPI(title="Testable Runner Microservice")

async def override_get_db():
    async with test_async_session_maker() as session:
        yield session

class RunnerCreateSchema(BaseModel):
    runner_id: int = Field(..., gt=0)
    name: str = Field(..., min_length=2, max_length=50)
    email: str
    target_5k_pace: str = Field(..., pattern=r"^\d{1,2}:\d{2}$")

class RunnerResponseSchema(RunnerCreateSchema):
    id: int
    class Config:
        from_attributes = True

@app.post("/api/v1/runners", status_code=status.HTTP_201_CREATED, response_model=RunnerResponseSchema)
async def register_runner(runner_data: RunnerCreateSchema, db: AsyncSession = Depends(override_get_db)):
    # Check for duplicate runner_id
    stmt = select(RunnerORM).where(RunnerORM.runner_id == runner_data.runner_id)
    result = await db.execute(stmt)
    if result.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Runner ID already registered.")
    
    new_runner = RunnerORM(**runner_data.model_dump())
    db.add(new_runner)
    await db.commit()
    await db.refresh(new_runner)
    return new_runner

# 3. Pytest Fixture (Fresh DB per test)
@pytest_asyncio.fixture
async def async_client():
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        yield client
        
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

# 4. Test Case 1: Successful Creation
@pytest.mark.asyncio
async def test_create_runner(async_client):
    payload = {
        "runner_id": 777,
        "name": "Conix Tester",
        "email": "conix@test.com",
        "target_5k_pace": "04:10"
    }
    response = await async_client.post("/api/v1/runners", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["runner_id"] == 777
    print("✅ [TEST 1 PASSED]: Runner successfully created!")

# 5. Test Case 2: Duplicate ID Error Handling
@pytest.mark.asyncio
async def test_create_duplicate_runner(async_client):
    payload = {
        "runner_id": 888,
        "name": "Conix Duplicate",
        "email": "duplicate@test.com",
        "target_5k_pace": "04:00"
    }
    
    # First request should succeed (201 Created)
    response1 = await async_client.post("/api/v1/runners", json=payload)
    assert response1.status_code == 201
    
    # Second request with the exact same runner_id should fail (400 Bad Request)
    response2 = await async_client.post("/api/v1/runners", json=payload)
    assert response2.status_code == 400
    assert response2.json()["detail"] == "Runner ID already registered."
    print("✅ [TEST 2 PASSED]: Duplicate runner correctly caught and blocked with HTTP 400!")

# Day 151 - Activity 3: Parameterized Testing & Endpoint Suites
import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, select
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field
from typing import List

# 1. Test Database Setup
TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"
test_engine = create_async_engine(TEST_DATABASE_URL, echo=False, future=True)
test_async_session_maker = async_sessionmaker(test_engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

class RunnerORM(Base):
    __tablename__ = "runners"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    runner_id: Mapped[int] = mapped_column(Integer, unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    target_5k_pace: Mapped[str] = mapped_column(String(10), nullable=False)

# 2. FastAPI App Instance
app = FastAPI(title="Testable Runner Microservice")

async def override_get_db():
    async with test_async_session_maker() as session:
        yield session

class RunnerCreateSchema(BaseModel):
    runner_id: int = Field(..., gt=0)
    name: str = Field(..., min_length=2, max_length=50)
    email: str
    target_5k_pace: str = Field(..., pattern=r"^\d{1,2}:\d{2}$")

class RunnerResponseSchema(RunnerCreateSchema):
    id: int
    class Config:
        from_attributes = True

@app.post("/api/v1/runners", status_code=status.HTTP_201_CREATED, response_model=RunnerResponseSchema)
async def register_runner(runner_data: RunnerCreateSchema, db: AsyncSession = Depends(override_get_db)):
    stmt = select(RunnerORM).where(RunnerORM.runner_id == runner_data.runner_id)
    result = await db.execute(stmt)
    if result.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Runner ID already registered.")
    
    new_runner = RunnerORM(**runner_data.model_dump())
    db.add(new_runner)
    await db.commit()
    await db.refresh(new_runner)
    return new_runner

@app.get("/api/v1/runners", response_model=List[RunnerResponseSchema])
async def get_runners(db: AsyncSession = Depends(override_get_db)):
    stmt = select(RunnerORM)
    result = await db.execute(stmt)
    return result.scalars().all()

# 3. Pytest Fixture (Fresh In-Memory DB per test)
@pytest_asyncio.fixture
async def async_client():
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        yield client
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

# 4. Test Case 1: Successful Creation
@pytest.mark.asyncio
async def test_create_runner(async_client):
    payload = {"runner_id": 777, "name": "Conix Tester", "email": "conix@test.com", "target_5k_pace": "04:10"}
    response = await async_client.post("/api/v1/runners", json=payload)
    assert response.status_code == 201

# 5. Test Case 2: Duplicate ID Error Handling
@pytest.mark.asyncio
async def test_create_duplicate_runner(async_client):
    payload = {"runner_id": 888, "name": "Conix Duplicate", "email": "duplicate@test.com", "target_5k_pace": "04:00"}
    res1 = await async_client.post("/api/v1/runners", json=payload)
    assert res1.status_code == 201
    res2 = await async_client.post("/api/v1/runners", json=payload)
    assert res2.status_code == 400

# 6. Test Case 3: GET All Runners Endpoint
@pytest.mark.asyncio
async def test_get_runners(async_client):
    payload = {"runner_id": 101, "name": "Runner One", "email": "one@test.com", "target_5k_pace": "03:50"}
    await async_client.post("/api/v1/runners", json=payload)
    
    response = await async_client.get("/api/v1/runners")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["name"] == "Runner One"
    print("✅ [TEST 3 PASSED]: GET list endpoint successfully retrieved runners!")

# 7. Test Case 4: Parameterized Pace Validation Test
@pytest.mark.asyncio
@pytest.mark.parametrize(
    "pace,expected_status",
    [
        ("03:45", 201), # Valid format MM:SS
        ("4:30", 201),  # Valid single-digit minute format
        ("0470", 422),  # Invalid format (missing colon)
        ("fast", 422),  # Invalid string format
    ],
)
async def test_pace_validation(async_client, pace, expected_status):
    payload = {"runner_id": 999, "name": "Pace Test", "email": "pace@test.com", "target_5k_pace": pace}
    response = await async_client.post("/api/v1/runners", json=payload)
    assert response.status_code == expected_status
    print(f"✅ [PARAMETRIZED TEST PASSED]: Pace '{pace}' returned expected HTTP status {expected_status}!")