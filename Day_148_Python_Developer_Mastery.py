# Day 148 - Activity 1: Defining Async Endpoints & Pydantic Schemas
import asyncio
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, EmailStr

# Initialize FastAPI App
app = FastAPI(title="Runner Telemetry Microservice", version="1.0.0")

# 1. Pydantic Schema for Input Data Validation
class RunnerRegistrationSchema(BaseModel):
    runner_id: int = Field(..., gt=0, description="Unique positive integer ID for the runner")
    name: str = Field(..., min_length=2, max_length=50, example="Conix")
    email: str = Field(..., example="conix@example.com")
    target_5k_pace: str = Field(..., pattern=r"^\d{1,2}:\d{2}$", example="04:15")

# Simulated In-Memory Database
RUNNER_DATABASE = {}

# 2. Asynchronous POST Endpoint
@app.post("/api/v1/runners", status_code=201)
async def register_runner(runner_data: RunnerRegistrationSchema):
    print(f"📥 Received registration request for {runner_data.name}...")
    
    # Check if runner already exists
    if runner_data.runner_id in RUNNER_DATABASE:
        raise HTTPException(status_code=400, detail="Runner ID already registered.")

    # Simulate non-blocking async database insertion delay
    await asyncio.sleep(0.3)
    
    # Store validated data
    RUNNER_DATABASE[runner_data.runner_id] = runner_data.model_dump()
    
    print(f"✅ [SUCCESS]: Runner {runner_data.name} saved to database!")
    return {
        "status": "success",
        "message": f"Runner {runner_data.name} registered successfully!",
        "data": runner_data
    }

# Script Execution Test / Direct Runner Verification
async def test_activity_1():
    print("🚀 Testing Day 148 Activity 1: FastAPI & Pydantic Validation...\n")
    
    # Test valid registration
    valid_payload = RunnerRegistrationSchema(
        runner_id=101,
        name="Conix",
        email="conix@example.com",
        target_5k_pace="04:15"
    )
    response = await register_runner(valid_payload)
    print(f"\n📊 Response Object: {response}")

if __name__ == "__main__":
    asyncio.run(test_activity_1())

# Day 148 - Activity 2: Async GET Endpoints & Dependency Injection (Depends)
import asyncio
from fastapi import FastAPI, HTTPException, Depends, Query
from pydantic import BaseModel, Field
from typing import List, Optional

# Initialize FastAPI App
app = FastAPI(title="Runner Telemetry Microservice", version="1.0.0")

# 1. Pydantic Schemas
class RunnerRegistrationSchema(BaseModel):
    runner_id: int = Field(..., gt=0, description="Unique positive integer ID")
    name: str = Field(..., min_length=2, max_length=50)
    email: str = Field(...)
    target_5k_pace: str = Field(..., pattern=r"^\d{1,2}:\d{2}$")

class RunnerResponseSchema(RunnerRegistrationSchema):
    status: str = "active"

# Simulated In-Memory Database
RUNNER_DATABASE = {
    101: {"runner_id": 101, "name": "Conix", "email": "conix@example.com", "target_5k_pace": "04:15", "status": "active"},
    102: {"runner_id": 102, "name": "Eona", "email": "eona@example.com", "target_5k_pace": "04:45", "status": "active"}
}

# 2. Dependency: Simulated Database/Service Provider
def get_runner_repository():
    # In real apps, this yields a database session or repository instance
    return RUNNER_DATABASE

# 3. Asynchronous POST Endpoint (Registration)
@app.post("/api/v1/runners", status_code=201)
async def register_runner(runner_data: RunnerRegistrationSchema, db = Depends(get_runner_repository)):
    print(f"📥 Received registration request for {runner_data.name}...")
    if runner_data.runner_id in db:
        raise HTTPException(status_code=400, detail="Runner ID already registered.")

    await asyncio.sleep(0.2)  # Simulate async DB write
    db[runner_data.runner_id] = runner_data.model_dump()
    
    print(f"✅ [SUCCESS]: Runner {runner_data.name} saved via Dependency Injection!")
    return {"status": "success", "data": runner_data}

# 4. Asynchronous GET Endpoint: Retrieve All Runners with Optional Filtering
@app.get("/api/v1/runners", response_model=List[RunnerResponseSchema])
async def get_all_runners(
    pace_filter: Optional[str] = Query(None, description="Filter runners faster than or equal to a pace"),
    db = Depends(get_runner_repository)
):
    print("📡 [GET]: Fetching runner list from repository...")
    await asyncio.sleep(0.1)  # Simulate async DB read
    
    runners = list(db.values())
    
    # Optional query filter logic
    if pace_filter:
        runners = [r for r in runners if r["target_5k_pace"] <= pace_filter]
        
    return runners

# 5. Asynchronous GET Endpoint: Retrieve Single Runner by Path ID
@app.get("/api/v1/runners/{runner_id}", response_model=RunnerResponseSchema)
async def get_runner_by_id(runner_id: int, db = Depends(get_runner_repository)):
    print(f"📡 [GET]: Looking up runner ID {runner_id}...")
    await asyncio.sleep(0.1)
    
    if runner_id not in db:
        raise HTTPException(status_code=404, detail="Runner not found.")
        
    return db[runner_id]

# Script Execution Test / Direct Verification
async def test_activity_2():
    print("🚀 Testing Day 148 Activity 2: Async GET Endpoints & Dependency Injection...\n")
    
    # Simulate testing the dependency-injected repository directly
    repo = get_runner_repository()
    
    # Test fetching all runners
    all_runners = await get_all_runners(db=repo)
    print(f"📊 All Registered Runners: {all_runners}")
    
    # Test fetching a single runner by ID path parameter
    runner = await get_runner_by_id(runner_id=101, db=repo)
    print(f"👤 Found Runner ID 101: {runner}")

if __name__ == "__main__":
    asyncio.run(test_activity_2())

# Day 148 - Activity 3: Asynchronous Background Tasks (BackgroundTasks)
import asyncio
from fastapi import FastAPI, HTTPException, Depends, BackgroundTasks
from pydantic import BaseModel, Field

# Initialize FastAPI App
app = FastAPI(title="Runner Telemetry Microservice", version="1.0.0")

# 1. Pydantic Schema
class RunnerRegistrationSchema(BaseModel):
    runner_id: int = Field(..., gt=0, description="Unique positive integer ID")
    name: str = Field(..., min_length=2, max_length=50)
    email: str = Field(...)
    target_5k_pace: str = Field(..., pattern=r"^\d{1,2}:\d{2}$")

# Simulated In-Memory Database
RUNNER_DATABASE = {}

# 2. Background Task Function (Runs after response is sent to client)
async def send_welcome_email_and_sync_telemetry(runner_name: str, email: str):
    print(f"📧 [BACKGROUND WORKER]: Preparing welcome email for {runner_name} ({email})...")
    await asyncio.sleep(1.5)  # Simulate external SMTP server / cloud API call delay
    print(f"✅ [BACKGROUND WORKER]: Welcome email sent and cloud telemetry synced for {runner_name}!")

# 3. Asynchronous POST Endpoint with Background Tasks
@app.post("/api/v1/runners-with-bg", status_code=201)
async def register_runner_background(
    runner_data: RunnerRegistrationSchema,
    background_tasks: BackgroundTasks
):
    print(f"📥 Received registration request for {runner_data.name}...")
    
    if runner_data.runner_id in RUNNER_DATABASE:
        raise HTTPException(status_code=400, detail="Runner ID already registered.")

    # Save to database (Fast operation)
    RUNNER_DATABASE[runner_data.runner_id] = runner_data.model_dump()
    
    # Queue the background task to run right after the response returns
    background_tasks.add_task(
        send_welcome_email_and_sync_telemetry,
        runner_name=runner_data.name,
        email=runner_data.email
    )
    
    print(f"⚡ [API RESPONSE]: Sent back to client immediately! Background task queued.")
    return {
        "status": "success",
        "message": f"Runner {runner_data.name} registered successfully! Welcome email queued.",
        "data": runner_data
    }

# 4. Script Execution Test / Direct Verification
class MockBackgroundTasks:
    """Helper class to simulate FastAPI's BackgroundTasks execution in direct script tests."""
    def __init__(self):
        self.tasks = []
    def add_task(self, func, *args, **kwargs):
        self.tasks.append((func, args, kwargs))

async def test_activity_3():
    print("🚀 Testing Day 148 Activity 3: FastAPI Background Tasks...\n")
    
    bg_tasks = MockBackgroundTasks()
    payload = RunnerRegistrationSchema(
        runner_id=103,
        name="Eona",
        email="eona@example.com",
        target_5k_pace="04:40"
    )
    
    # Execute the endpoint
    response = await register_runner_background(payload, bg_tasks)
    print(f"\n📊 Immediate API Response: {response}")
    
    print("\n⏳ Simulating FastAPI server triggering queued background tasks...")
    for func, args, kwargs in bg_tasks.tasks:
        await func(*args, **kwargs)

if __name__ == "__main__":
    asyncio.run(test_activity_3())



# Day 148 - Activity 4: FastAPI Lifespan Events & Startup/Shutdown
import asyncio
from fastapi import FastAPI
from contextlib import asynccontextmanager

# Simulated Database Connection Pool
db_pool = {}

# 1. Lifespan Context Manager for Startup & Shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- STARTUP PHASE ---
    print("🔌 [LIFESPAN]: Initializing database connection pool and loading configuration...")
    await asyncio.sleep(0.5)  # Simulate async connection delay
    db_pool["status"] = "Connected"
    db_pool["active_connections"] = 42
    print("✅ [LIFESPAN]: Database connection pool ready! Application is live.")
    
    yield  # Yield control back to FastAPI while it handles HTTP requests
    
    # --- SHUTDOWN PHASE ---
    print("\n🛑 [LIFESPAN]: Shutting down application gracefully...")
    await asyncio.sleep(0.3)  # Simulate closing connections
    db_pool.clear()
    print("🔒 [LIFESPAN]: Database connections closed safely. Goodbye!")

# 2. Initialize FastAPI App with the Lifespan Handler
app = FastAPI(title="Runner Telemetry Microservice", version="1.0.0", lifespan=lifespan)

# 3. Health Check Endpoint
@app.get("/api/v1/health")
async def health_check():
    return {
        "status": "healthy",
        "database": db_pool.get("status", "Disconnected"),
        "connections": db_pool.get("active_connections", 0)
    }

# 4. Script Execution Test / Direct Verification
async def test_activity_4():
    print("🚀 Testing Day 148 Activity 4: FastAPI Lifespan Events...\n")
    
    # Test the lifespan context manager directly in our script test
    async with lifespan(app):
        print(f"📊 Active App State during run: Database Pool -> {db_pool}")

if __name__ == "__main__":
    asyncio.run(test_activity_4())