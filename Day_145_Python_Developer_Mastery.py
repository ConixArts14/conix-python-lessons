# Day 145 - Activity 1: The Repository Pattern (Data Access Abstraction)
from abc import ABC, abstractmethod
from typing import List, Optional, Dict

# 1. Domain Entity (The Core Business Data)
class RunnerProfile:
    def __init__(self, runner_id: int, name: str, favorite_event: str):
        self.runner_id = runner_id
        self.name = name
        self.favorite_event = favorite_event

    def __repr__(self) -> str:
        return f"RunnerProfile(id={self.runner_id}, name='{self.name}', event='{self.favorite_event}')"

# 2. Repository Interface
class RunnerRepository(ABC):
    @abstractmethod
    def add(self, runner: RunnerProfile) -> None:
        pass

    @abstractmethod
    def get_by_id(self, runner_id: int) -> Optional[RunnerProfile]:
        pass

    @abstractmethod
    def get_all(self) -> List[RunnerProfile]:
        pass

# 3. Concrete Implementation: In-Memory Repository (Great for Testing)
class InMemoryRunnerRepository(RunnerRepository):
    def __init__(self):
        self._storage: Dict[int, RunnerProfile] = {}

    def add(self, runner: RunnerProfile) -> None:
        self._storage[runner.runner_id] = runner
        print(f"💾 [REPOSITORY]: Saved {runner.name} to storage.")

    def get_by_id(self, runner_id: int) -> Optional[RunnerProfile]:
        return self._storage.get(runner_id)

    def get_all(self) -> List[RunnerProfile]:
        return list(self._storage.values())

# 4. Service Layer / Core App Logic (Uses the Repository abstraction)
class RunnerService:
    def __init__(self, repository: RunnerRepository):
        self.repository = repository  # Decoupled from storage implementation!

    def register_runner(self, runner_id: int, name: str, event: str) -> None:
        profile = RunnerProfile(runner_id, name, event)
        self.repository.add(profile)

    def list_all_athletes(self) -> None:
        print("\n📋 [ALL ATHLETES IN SYSTEM]:")
        for runner in self.repository.get_all():
            print(f"  - {runner}")

# 5. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 145 Activity 1 Repository Pattern...\n")

    # Instantiate the repository and service
    repo = InMemoryRunnerRepository()
    service = RunnerService(repo)

    # Register runners
    service.register_runner(1, "Conix", "5k Speed Run")
    service.register_runner(2, "Eona", "1k Youth Dash")

    # Fetch and list data through the repository
    service.list_all_athletes()

# Day 145 - Activity 2: Dependency Injection Container Pattern (IoC)
from abc import ABC, abstractmethod
from typing import Dict, Callable, Any

# 1. Repository Interface & Concrete Implementation
class RunnerRepository(ABC):
    @abstractmethod
    def get_status(self) -> str:
        pass

class SqlRunnerRepository(RunnerRepository):
    def get_status(self) -> str:
        return "Connected to Enterprise PostgreSQL Database 🗄️"

# 2. Service Layer
class RunnerManagementService:
    def __init__(self, repository: RunnerRepository):
        self.repository = repository

    def get_runner_system_status(self) -> str:
        return f"Runner Service Active -> {self.repository.get_status()}"

# 3. The Dependency Injection Container (IoC Container)
class DIContainer:
    def __init__(self):
        self._services: Dict[str, Callable[[], Any]] = {}

    def register(self, key: str, factory: Callable[[], Any]) -> None:
        self._services[key] = factory
        print(f"🔧 [DI CONTAINER]: Registered dependency '{key}'.")

    def resolve(self, key: str) -> Any:
        if key not in self._services:
            raise KeyError(f"Dependency '{key}' not found in container!")
        # Execute the factory function to build the object and its dependencies
        return self._services[key]()

# 4. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 145 Activity 2 DI Container Pattern...\n")

    # Instantiate the container
    container = DIContainer()

    # Register dependencies with factory lambdas
    container.register("RunnerRepository", lambda: SqlRunnerRepository())
    
    # Register the service, telling the container to resolve its repository dependency automatically!
    container.register(
        "RunnerService", 
        lambda: RunnerManagementService(container.resolve("RunnerRepository"))
    )

    print("\n🔍 Resolving 'RunnerService' from DI Container...")
    service = container.resolve("RunnerService")
    
    # Run method from resolved service
    print(service.get_runner_system_status())

# Day 145 - Activity 3: The Unit of Work Pattern (Atomic Transactions)
from abc import ABC, abstractmethod

# 1. Unit of Work Abstract Base Class (Context Manager Protocol)
class UnitOfWork(ABC):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"❌ [UoW ERROR DETECTED]: {exc_val}")
            self.rollback()
        else:
            self.commit()

    @abstractmethod
    def commit(self) -> None:
        pass

    @abstractmethod
    def rollback(self) -> None:
        pass

# 2. Concrete Unit of Work (Simulating Enterprise Database Transaction Management)
class SqlRunnerUnitOfWork(UnitOfWork):
    def __init__(self):
        self._is_transaction_active = False

    def __enter__(self):
        super().__enter__()
        self._is_transaction_active = True
        print("🔄 [UoW TRANSACTION]: Opening database connection and starting transaction...")
        return self

    def commit(self) -> None:
        if self._is_transaction_active:
            print("💾 [UoW COMMIT]: All operations succeeded. Committing changes to database permanently!")
            self._is_transaction_active = False

    def rollback(self) -> None:
        if self._is_transaction_active:
            print("⏪ [UoW ROLLBACK]: Error occurred! Rolling back transaction to protect data integrity.")
            self._is_transaction_active = False

# 3. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 145 Activity 3 Unit of Work Pattern...\n")

    print("--- SCENARIO 1: Successful Transaction ---")
    with SqlRunnerUnitOfWork() as uow:
        print("  🏃 [BUSINESS LOGIC]: Updating Conix's 5k personal record...")
        print("  📊 [BUSINESS LOGIC]: Saving telemetry split times...")
        # Automatically commits when leaving the 'with' block successfully!

    print("\n--- SCENARIO 2: Failed Transaction with Auto-Rollback ---")
    try:
        with SqlRunnerUnitOfWork() as uow:
            print("  🏃 [BUSINESS LOGIC]: Registering new race event...")
            print("  💥 [SIMULATED ERROR]: Database connection lost mid-transaction!")
            raise ConnectionError("Lost connection to PostgreSQL server.")
    except ConnectionError:
        print("🛡️ [APP CATCH]: Transaction safely aborted and rolled back.")

# Day 145 - Activity 4: The Specification Pattern (Encapsulating Business Query Rules)
from abc import ABC, abstractmethod
from typing import List

# 1. Domain Entity
class Runner:
    def __init__(self, name: str, event: str, best_time_min: float):
        self.name = name
        self.event = event
        self.best_time_min = best_time_min

    def __repr__(self) -> str:
        return f"Runner(name='{self.name}', event='{self.event}', best_time={self.best_time_min}m)"

# 2. Specification Interface
class Specification(ABC):
    @abstractmethod
    def is_satisfied_by(self, runner: Runner) -> bool:
        pass

# 3. Concrete Specification A: Filter by Event
class EventSpecification(Specification):
    def __init__(self, event_name: str):
        self.event_name = event_name

    def is_satisfied_by(self, runner: Runner) -> bool:
        return runner.event.lower() == self.event_name.lower()

# 4. Concrete Specification B: Filter by Speed (Elite runners under a certain time)
class EliteSpeedSpecification(Specification):
    def __init__(self, max_time_min: float):
        self.max_time_min = max_time_min

    def is_satisfied_by(self, runner: Runner) -> bool:
        return runner.best_time_min <= self.max_time_min

# 5. Composite Specification (Combining two rules with AND logic)
class AndSpecification(Specification):
    def __init__(self, spec1: Specification, spec2: Specification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, runner: Runner) -> bool:
        return self.spec1.is_satisfied_by(runner) and self.spec2.is_satisfied_by(runner)

# 6. Repository with Specification Query Support
class RunnerQueryRepository:
    def __init__(self, runners: List[Runner]):
        self.runners = runners

    def query(self, spec: Specification) -> List[Runner]:
        # Filters the list using any passed specification rule!
        return [runner for runner in self.runners if spec.is_satisfied_by(runner)]

# 7. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 145 Activity 4 Specification Pattern...\n")

    # Sample roster
    roster = [
        Runner("Conix", "5k", 18.5),
        Runner("Eona", "1k", 3.8),
        Runner("Alex", "5k", 22.0),
        Runner("Sam", "10k", 41.5)
    ]

    repo = RunnerQueryRepository(roster)

    # Query 1: Find all 5k runners using EventSpecification
    five_k_spec = EventSpecification("5k")
    print("📋 [QUERY 1]: All 5k runners:")
    for r in repo.query(five_k_spec):
        print(f"  - {r}")

    # Query 2: Find elite runners (under 20 minutes) using EliteSpeedSpecification
    elite_spec = EliteSpeedSpecification(20.0)
    print("\n📋 [QUERY 2]: Elite runners (<= 20 mins):")
    for r in repo.query(elite_spec):
        print(f"  - {r}")

    # Query 3: Combine rules! Find 5k runners AND elite speed using AndSpecification
    elite_5k_spec = AndSpecification(EventSpecification("5k"), EliteSpeedSpecification(20.0))
    print("\n📋 [QUERY 3]: Elite 5k runners (Combined Rule):")
    for r in repo.query(elite_5k_spec):
        print(f"  - {r}")

# Day 145 - Activity 5: CQRS Pattern (Command Query Responsibility Segregation)
from abc import ABC, abstractmethod
from typing import List, Dict

# 1. Shared Database State (Simulating data storage)
class SharedDatabase:
    def __init__(self):
        self.runners: List[Dict] = []

# ==========================================
# PART A: THE WRITE SIDE (Commands & Handlers)
# ==========================================
class Command(ABC):
    pass

class RegisterRunnerCommand(Command):
    def __init__(self, name: str, event: str, pace_min: float):
        self.name = name
        self.event = event
        self.pace_min = pace_min

class RegisterRunnerHandler:
    def __init__(self, db: SharedDatabase):
        self.db = db

    def handle(self, command: RegisterRunnerCommand) -> None:
        # Enforce business write rules & mutations here
        print(f"✍️ [CQRS WRITE]: Validating and saving new runner -> {command.name} ({command.event})")
        self.db.runners.append({
            "name": command.name, 
            "event": command.event, 
            "pace": command.pace_min
        })

# ==========================================
# PART B: THE READ SIDE (Queries & Handlers)
# ==========================================
class Query(ABC):
    pass

class GetRunnerLeaderboardQuery(Query):
    pass

class GetRunnerLeaderboardHandler:
    def __init__(self, db: SharedDatabase):
        self.db = db

    def handle(self, query: GetRunnerLeaderboardQuery) -> List[Dict]:
        # Optimized purely for fast reading and sorting without touching write logic
        print("📖 [CQRS READ]: Fetching optimized leaderboard read model...")
        return sorted(self.db.runners, key=lambda x: x["pace"])

# 5. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 145 Activity 5 CQRS Pattern...\n")

    # Shared database instance
    db = SharedDatabase()

    # Instantiate Write and Read handlers
    write_handler = RegisterRunnerHandler(db)
    read_handler = GetRunnerLeaderboardHandler(db)

    # 1. Execute Write Commands (Modifying state)
    write_handler.handle(RegisterRunnerCommand("Alex", "5k", 21.0))
    write_handler.handle(RegisterRunnerCommand("Conix", "5k", 18.5))
    write_handler.handle(RegisterRunnerCommand("Eona", "1k", 3.8))

    print("\n----------------------------------------\n")

    # 2. Execute Read Queries (Fetching optimized view)
    leaderboard = read_handler.handle(GetRunnerLeaderboardQuery())

    print("\n🏆 [OPTIMIZED LEADERBOARD RESULTS]:")
    for rank, runner in enumerate(leaderboard, 1):
        print(f"  {rank}. {runner['name']} ({runner['event']}) -> {runner['pace']} min pace")