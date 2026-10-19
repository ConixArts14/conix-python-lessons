# Day 146 - Activity 1: Value Objects (DDD Tactical Patterns)
from dataclasses import dataclass

# 1. Value Object: Immutable and defined entirely by its values, not an ID!
@dataclass(frozen=True)
class Pace:
    minutes: int
    seconds: int

    def __post_init__(self):
        # Validate data integrity upon creation
        if self.seconds < 0 or self.seconds >= 60:
            raise ValueError("Seconds must be between 0 and 59.")
        if self.minutes < 0:
            raise ValueError("Minutes cannot be negative.")

    def to_seconds_per_km(self) -> float:
        return (self.minutes * 60) + self.seconds

    def __str__(self) -> str:
        return f"{self.minutes}:{self.seconds:02d} min/km"

# 2. Value Object: Distance in Kilometers
@dataclass(frozen=True)
class DistanceKm:
    value: float

    def __post_init__(self):
        if self.value <= 0:
            raise ValueError("Distance must be greater than zero.")

    def __str__(self) -> str:
        return f"{self.value} km"

# 3. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 146 Activity 1: Value Objects...\n")

    # Create value objects
    pace1 = Pace(4, 45)
    pace2 = Pace(4, 45)
    distance = DistanceKm(5.0)

    print(f"🏃 Runner Pace: {pace1}")
    print(f"📏 Race Distance: {distance}")
    print(f"⏱️ Total seconds per km: {pace1.to_seconds_per_km()}s")

    # Value objects equality check (True because attributes match!)
    print(f"⚖️ Are both paces equal? {pace1 == pace2}")

    # Trying to modify a frozen value object raises a FrozenInstanceError!
    try:
        print("🔒 Attempting to mutate immutable pace...")
        # pace1.minutes = 5  # Uncommenting this throws an error!
        print("✅ Immutability successfully preserved!")
    except Exception as e:
        print(f"Error: {e}")

# Day 146 - Activity 2: Entities (DDD Tactical Patterns)
from dataclasses import dataclass

# 1. Reusing our Value Object from Activity 1
@dataclass(frozen=True)
class Pace:
    minutes: int
    seconds: int

    def __str__(self) -> str:
        return f"{self.minutes}:{self.seconds:02d} min/km"

# 2. Entity: Has a unique identity (runner_id) and mutable state/behavior
class RunnerEntity:
    def __init__(self, runner_id: str, name: str, pace: Pace):
        self.runner_id = runner_id  # Unique Identity (Never changes)
        self._name = name           # Mutable attribute
        self._pace = pace           # Mutable value object

    @property
    def name(self) -> str:
        return self._name

    @property
    def pace(self) -> Pace:
        return self._pace

    # Business behavior / method modifying entity state safely
    def update_pace(self, new_pace: Pace) -> None:
        print(f"🔄 [ENTITY]: Updating pace for runner {self.runner_id} from {self._pace} to {new_pace}")
        self._pace = new_pace

    def change_name(self, new_name: str) -> None:
        if not new_name.strip():
            raise ValueError("Runner name cannot be empty.")
        print(f"📝 [ENTITY]: Changing name for ID {self.runner_id} to '{new_name}'")
        self._name = new_name

    # Entities are compared by their unique ID, not their attributes!
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, RunnerEntity):
            return False
        return self.runner_id == other.runner_id

    def __repr__(self) -> str:
        return f"RunnerEntity(id='{self.runner_id}', name='{self._name}', pace={self._pace})"

# 3. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 146 Activity 2: Entities...\n")

    # Instantiate two distinct runners
    runner_1 = RunnerEntity(runner_id="RUN-001", name="Conix", pace=Pace(4, 45))
    runner_2 = RunnerEntity(runner_id="RUN-001", name="Conix Updated", pace=Pace(4, 30))

    print(f"🏃 Initial Runner: {runner_1}")

    # Modify entity state
    runner_1.update_pace(Pace(4, 30))
    runner_1.change_name("Conix Pro")

    print(f"🏃 Modified Runner: {runner_1}")

    # Entity Equality Check (True because runner_id 'RUN-001' matches, even though name/pace changed!)
    print(f"\n⚖️ Are both runner instances the same entity (by ID)? {runner_1 == runner_2}")

# Day 146 - Activity 3: Aggregate Roots (DDD Tactical Patterns)
from dataclasses import dataclass
from typing import List

# 1. Value Object for individual split telemetry
@dataclass(frozen=True)
class SplitTime:
    kilometer: int
    seconds: float

    def __str__(self) -> str:
        return f"Km {self.kilometer}: {self.seconds}s"

# 2. Aggregate Root: Manages consistency across the entire race session cluster
class RaceSessionAggregate:
    def __init__(self, session_id: str, runner_name: str):
        self.session_id = session_id
        self.runner_name = runner_name
        self._splits: List[SplitTime] = []
        self._is_completed = False

    @property
    def is_completed(self) -> bool:
        return self._is_completed

    @property
    def splits(self) -> List[SplitTime]:
        # Return a copy to protect internal list encapsulation
        return list(self._splits)

    # Business Rule Enforcement (Gatekeeper Method)
    def record_split(self, kilometer: int, seconds: float) -> None:
        if self._is_completed:
            raise ValueError("❌ [BUSINESS RULE ERROR]: Cannot add splits to a completed race session!")
        if seconds <= 0:
            raise ValueError("❌ [BUSINESS RULE ERROR]: Split time must be greater than zero.")

        split = SplitTime(kilometer, seconds)
        self._splits.append(split)
        print(f"⏱️ [AGGREGATE ROOT]: Recorded split -> {split}")

    def complete_session(self) -> None:
        self._is_completed = True
        print(f"🏁 [AGGREGATE ROOT]: Race session {self.session_id} for {self.runner_name} is now complete.")

    def __repr__(self) -> str:
        return f"RaceSession(id='{self.session_id}', runner='{self.runner_name}', splits_recorded={len(self._splits)}, completed={self._is_completed})"

# 3. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 146 Activity 3: Aggregate Root...\n")

    # Create the Aggregate Root
    race_session = RaceSessionAggregate(session_id="SESS-5K-01", runner_name="Conix")

    # Record splits through the aggregate root
    race_session.record_split(1, 215.5)
    race_session.record_split(2, 218.0)

    print(f"\n📋 Session Status: {race_session}")

    # Complete the session
    race_session.complete_session()

    # Attempting to add a split after completion triggers our Business Rule guard!
    try:
        print("\n🔒 Attempting to record split after race completion...")
        race_session.record_split(3, 220.0)
    except ValueError as e:
        print(e)

# Day 146 - Activity 4: Domain Services (DDD Tactical Patterns)
from dataclasses import dataclass
from typing import List

# 1. Reusing our Aggregate Root from Activity 3
@dataclass(frozen=True)
class SplitTime:
    kilometer: int
    seconds: float

class RaceSessionAggregate:
    def __init__(self, session_id: str, runner_name: str):
        self.session_id = session_id
        self.runner_name = runner_name
        self._splits: List[SplitTime] = []

    def record_split(self, kilometer: int, seconds: float) -> None:
        self._splits.append(SplitTime(kilometer, seconds))

    def calculate_total_time(self) -> float:
        # Sums all split times across the aggregate
        return sum(split.seconds for split in self._splits)

# 2. Domain Service: Stateless business logic spanning multiple aggregates
class RaceEvaluationService:
    @staticmethod
    def determine_winner(sessions: List[RaceSessionAggregate]) -> RaceSessionAggregate:
        if not sessions:
            raise ValueError("No race sessions provided for evaluation.")

        print("⚙️ [DOMAIN SERVICE]: Calculating race rankings across multiple aggregate roots...")

        # Sort sessions by their total calculated time (lowest total time wins)
        sorted_sessions = sorted(sessions, key=lambda s: s.calculate_total_time())
        return sorted_sessions[0]

# 3. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 146 Activity 4: Domain Services...\n")

    # Create race sessions for different runners (Aggregates)
    session_conix = RaceSessionAggregate("SESS-01", "Conix")
    session_conix.record_split(1, 210.0)
    session_conix.record_split(2, 215.0)  # Total: 425.0s

    session_eona = RaceSessionAggregate("SESS-02", "Eona")
    session_eona.record_split(1, 205.0)
    session_eona.record_split(2, 210.0)  # Total: 415.0s (Faster!)

    # Pass multiple aggregates into the stateless Domain Service
    all_sessions = [session_conix, session_eona]
    winner = RaceEvaluationService.determine_winner(all_sessions)

    print(f"\n🏆 [OFFICIAL RESULTS]: The winner is {winner.runner_name} with a total time of {winner.calculate_total_time()} seconds!")

# Day 146 - Activity 5: Domain Events (DDD Tactical Patterns)
from dataclasses import dataclass
from typing import List, Callable, Any

# 1. Domain Event: Represents a business fact that already occurred in the past
@dataclass(frozen=True)
class RunnerFinishedEvent:
    runner_name: str
    total_time_sec: float
    timestamp: str

# 2. Aggregate Root that raises and stores Domain Events
class EventDrivenRaceAggregate:
    def __init__(self, runner_name: str):
        self.runner_name = runner_name
        self.domain_events: List[Any] = []
        self._is_finished = False

    def finish_race(self, total_time: float) -> None:
        if self._is_finished:
            return
        self._is_finished = True

        print(f"🏁 [AGGREGATE ROOT]: {self.runner_name} crossed the finish line!")

        # Create and record the domain event
        event = RunnerFinishedEvent(
            runner_name=self.runner_name,
            total_time_sec=total_time,
            timestamp="2026-10-19 18:00:00"
        )
        self.domain_events.append(event)

# 3. Domain Event Dispatcher
class RaceEventDispatcher:
    def __init__(self):
        self._handlers: List[Callable[[Any], None]] = []

    def register(self, handler: Callable[[Any], None]) -> None:
        self._handlers.append(handler)

    def dispatch(self, events: List[Any]) -> None:
        for event in events:
            print(f"\n⚡ [EVENT DISPATCHER]: Publishing event -> {type(event).__name__}")
            for handler in self._handlers:
                handler(event)

# 4. Independent Event Handlers (Side effects like notifications and leaderboards)
def send_celebration_notification(event: RunnerFinishedEvent) -> None:
    print(f"🔔 [NOTIFICATION SERVICE]: Sending push notification -> Great job {event.runner_name}! Time: {event.total_time_sec}s")

def update_leaderboard_handler(event: RunnerFinishedEvent) -> None:
    print(f"📊 [LEADERBOARD SERVICE]: Updating official standings with {event.runner_name}'s finish time.")

# 5. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 146 Activity 5: Domain Events...\n")

    # Setup dispatcher and register decoupled handlers
    dispatcher = RaceEventDispatcher()
    dispatcher.register(send_celebration_notification)
    dispatcher.register(update_leaderboard_handler)

    # Trigger aggregate activity
    race_session = EventDrivenRaceAggregate("Conix")
    race_session.finish_race(1125.0)

    # Dispatch any events raised by the aggregate root
    dispatcher.dispatch(race_session.domain_events)