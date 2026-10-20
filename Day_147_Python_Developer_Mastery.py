# Day 147 - Activity 1: Asynchronous Event Loops & Tasks (asyncio)
import asyncio
import time

# 1. Async Coroutine: Simulates fetching live biometric telemetry from a runner's device
async def fetch_runner_telemetry(runner_name: str, delay_seconds: float) -> dict:
    print(f"📡 [ASYNC]: Initiating telemetry connection for {runner_name}...")
    await asyncio.sleep(delay_seconds)  # Non-blocking pause allowing other tasks to run!
    print(f"✅ [ASYNC]: Telemetry received for {runner_name} ({delay_seconds}s delay)")
    return {
        "runner": runner_name,
        "heart_rate": 165,
        "pace_min_km": "4:30"
    }

# 2. Main Async Orchestrator
async def main():
    print("🚀 Initializing Day 147 Activity 1: Async Telemetry Processing...\n")
    start_time = time.perf_counter()

    # Schedule multiple coroutines to run concurrently inside the event loop
    task1 = asyncio.create_task(fetch_runner_telemetry("Conix", 2.0))
    task2 = asyncio.create_task(fetch_runner_telemetry("Eona", 1.5))
    task3 = asyncio.create_task(fetch_runner_telemetry("Coach", 1.0))

    # Await all tasks to complete concurrently
    results = await asyncio.gather(task1, task2, task3)

    elapsed = time.perf_counter() - start_time
    print(f"\n📊 Telemetry Results Collected: {results}")
    print(f"⏱️ Total Execution Time: {elapsed:.2f} seconds (Notice it took ~2s instead of 4.5s sync!)")

# 3. Execution Block
if __name__ == "__main__":
    asyncio.run(main())

# Day 147 - Activity 2: Asynchronous Event Queues (asyncio.Queue)
import asyncio
import random

# 1. Producer: Generates split events and puts them into the queue
async def split_telemetry_producer(queue: asyncio.Queue, count: int):
    for i in range(1, count + 1):
        split_data = {
            "split_id": f"SPLIT-{i:03d}",
            "runner": "Conix",
            "km": i,
            "seconds": round(random.uniform(210.0, 225.0), 1)
        }
        await queue.put(split_data)
        print(f"📥 [PRODUCER]: Sent split event -> Km {split_data['km']} ({split_data['seconds']}s)")
        await asyncio.sleep(0.5)  # Simulate delay between kilometers

# 2. Consumer: Worker that pulls events from the queue and processes them
async def leaderboard_consumer(queue: asyncio.Queue):
    while True:
        split_data = await queue.get()
        print(f"⚙️ [CONSUMER]: Processing leaderboard update for {split_data['runner']} on Km {split_data['km']}...")
        await asyncio.sleep(0.2)  # Simulate processing work
        print(f"✅ [CONSUMER]: Split {split_data['split_id']} successfully recorded!")
        queue.task_done()

# 3. Main Orchestrator
async def main():
    print("🚀 Initializing Day 147 Activity 2: Async Event Queues...\n")

    # Create an unbounded async queue
    queue = asyncio.Queue()

    # Start the consumer task in the background
    consumer_task = asyncio.create_task(leaderboard_consumer(queue))

    # Run the producer to generate 3 split events
    await split_telemetry_producer(queue, count=3)

    # Wait until all items in the queue have been processed
    await queue.join()

    # Cancel background consumer worker
    consumer_task.cancel()
    print("\n🏁 All queued splits have been processed successfully!")

# Execution Block
if __name__ == "__main__":
    asyncio.run(main())

# Day 147 - Activity 3: Asynchronous Event Bus & Pub/Sub Pattern
import asyncio
from dataclasses import dataclass
from typing import Callable, List, Dict, Any

# 1. Immutable Event Data Object
@dataclass(frozen=True)
class RaceCompletedEvent:
    runner_name: str
    total_time: float

# 2. Asynchronous Event Bus (Pub/Sub)
class AsyncEventBus:
    def __init__(self):
        self._subscribers: Dict[str, List[Callable[[Any], Any]]] = {}

    def subscribe(self, event_type: str, handler: Callable[[Any], Any]) -> None:
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []
        self._subscribers[event_type].append(handler)

    async def publish(self, event: Any) -> None:
        event_type = type(event).__name__
        if event_type not in self._subscribers:
            print(f"⚠️ [EVENT BUS]: No subscribers found for {event_type}")
            return

        print(f"⚡ [EVENT BUS]: Broadcasting {event_type} to all microservices...")

        # Execute all async subscriber handlers concurrently!
        handlers = self._subscribers[event_type]
        await asyncio.gather(*(handler(event) for handler in handlers))

# 3. Independent Microservice Event Handlers
async def push_notification_service(event: RaceCompletedEvent):
    await asyncio.sleep(0.4)  # Simulate external SMS network call
    print(f"🔔 [NOTIFICATION SERVICE]: Sent push alert -> {event.runner_name} finished in {event.total_time}s!")

async def leaderboard_service(event: RaceCompletedEvent):
    await asyncio.sleep(0.2)  # Simulate database write
    print(f"📊 [LEADERBOARD SERVICE]: Updated official standings for {event.runner_name}.")

async def analytics_service(event: RaceCompletedEvent):
    await asyncio.sleep(0.3)  # Simulate telemetry logging
    print(f"📈 [ANALYTICS SERVICE]: Logged performance metrics for {event.runner_name}.")

# 4. Main Orchestrator
async def main():
    print("🚀 Initializing Day 147 Activity 3: Async Event Bus...\n")

    # Initialize Event Bus
    bus = AsyncEventBus()

    # Register microservices to listen for RaceCompletedEvent
    bus.subscribe("RaceCompletedEvent", push_notification_service)
    bus.subscribe("RaceCompletedEvent", leaderboard_service)
    bus.subscribe("RaceCompletedEvent", analytics_service)

    # Publish an event
    event = RaceCompletedEvent(runner_name="Conix", total_time=1125.5)
    await bus.publish(event)

    print("\n🏁 All microservice subscribers finished processing concurrently!")

# Execution Block
if __name__ == "__main__":
    asyncio.run(main())

# Day 147 - Activity 4: Asynchronous Worker Pools & Rate Limiting (asyncio.Semaphore)
import asyncio
import random

# 1. Telemetry processor protected by a Semaphore (Rate Limiter)
async def process_telemetry_batch(semaphore: asyncio.Semaphore, batch_id: int, runner_name: str):
    # Acquire the semaphore lock (Only X tasks allowed in here at once)
    async with semaphore:
        print(f"🔒 [SEMAPHORE]: Batch {batch_id} for {runner_name} acquired database access.")

        # Simulate database write / heavy processing delay
        processing_time = round(random.uniform(0.8, 1.5), 2)
        await asyncio.sleep(processing_time)

        print(f"✅ [SEMAPHORE]: Batch {batch_id} for {runner_name} saved in {processing_time}s and released lock.")

# 2. Main Orchestrator
async def main():
    print("🚀 Initializing Day 147 Activity 4: Async Worker Pools & Semaphores...\n")

    # Create a semaphore allowing a maximum of 2 concurrent database writes
    db_semaphore = asyncio.Semaphore(2)

    # Simulate 5 incoming runner telemetry batches arriving simultaneously
    runners = ["Conix", "Eona", "Coach", "Runner-X", "Runner-Y"]

    tasks = [
        process_telemetry_batch(db_semaphore, i + 1, runner)
        for i, runner in enumerate(runners)
    ]

    # Run all tasks concurrently (the semaphore will safely throttle them to max 2 at a time)
    await asyncio.gather(*tasks)

    print("\n🏁 All telemetry batches successfully processed with controlled concurrency!")

# Execution Block
if __name__ == "__main__":
    asyncio.run(main())
# Day 147 - Activity 5: Asynchronous Timeouts & Fault Tolerance (asyncio.wait_for)
import asyncio

# 1. Microservice operation that simulates a fluctuating network delay
async def fetch_external_weather_telemetry(delay: float) -> str:
    print("🌐 [EXTERNAL API]: Connecting to weather telemetry satellite...")
    await asyncio.sleep(delay)
    return "Weather Status: Clear skies, 28°C, Track conditions optimal."

# 2. Resilient Orchestrator with Timeout Protection
async def get_telemetry_with_timeout(delay: float, timeout_limit: float):
    try:
        print(f"⏱️ [MICROSERVICE]: Requesting data with a strict timeout limit of {timeout_limit}s...")

        # Enforce a time limit using asyncio.wait_for
        result = await asyncio.wait_for(
            fetch_external_weather_telemetry(delay),
            timeout=timeout_limit
        )
        print(f"✅ [SUCCESS]: Received -> {result}")

    except asyncio.TimeoutError:
        print(f"⚠️ [FAULT TOLERANCE]: External API timed out after {timeout_limit}s! Falling back to cached local data safely.")

# 3. Main Orchestrator
async def main():
    print("🚀 Initializing Day 147 Activity 5: Async Timeouts & Fault Tolerance...\n")

    # Test Case 1: Fast response (Succeeds within timeout)
    print("--- Test Case 1: Normal Speed Response ---")
    await get_telemetry_with_timeout(delay=1.0, timeout_limit=2.0)

    print("\n" + "="*50 + "\n")

    # Test Case 2: Slow/Hanging response (Triggers Timeout and Fallback)
    print("--- Test Case 2: Hanging Network Response ---")
    await get_telemetry_with_timeout(delay=3.0, timeout_limit=1.5)

# Execution Block
if __name__ == "__main__":
    asyncio.run(main())
