# Day 144 - Activity 1: The Strategy Pattern (Swappable Algorithms)
from abc import ABC, abstractmethod

# 1. The Strategy Interface
class PaceStrategy(ABC):
    @abstractmethod
    def calculate_target_pace(self, distance_km: float) -> str:
        pass

# 2. Concrete Strategy A: Sprint Pace
class SprintStrategy(PaceStrategy):
    def calculate_target_pace(self, distance_km: float) -> str:
        return f"⚡ [SPRINT STRATEGY]: Pushing max speed! Target pace: 3.5 min/km for {distance_km}km."

# 3. Concrete Strategy B: Endurance Pace
class EnduranceStrategy(PaceStrategy):
    def calculate_target_pace(self, distance_km: float) -> str:
        return f"🔋 [ENDURANCE STRATEGY]: Maintaining steady rhythm. Target pace: 5.2 min/km for {distance_km}km."

# 4. Concrete Strategy C: Recovery Pace
class RecoveryStrategy(PaceStrategy):
    def calculate_target_pace(self, distance_km: float) -> str:
        return f"🫁 [RECOVERY STRATEGY]: Easy breathing jog. Target pace: 6.5 min/km for {distance_km}km."

# 5. The Context Class (Uses a strategy and allows swapping it on the fly!)
class RunnerContext:
    def __init__(self, strategy: PaceStrategy):
        self._strategy = strategy  # Holds the current strategy

    def set_strategy(self, strategy: PaceStrategy):
        print("🔄 [STRATEGY SWITCH]: Changing runner strategy...")
        self._strategy = strategy

    def execute_workout(self, distance_km: float) -> str:
        return self._strategy.calculate_target_pace(distance_km)

# 6. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 144 Activity 1 Strategy Pattern...\n")

    # Start with Endurance Strategy
    runner = RunnerContext(EnduranceStrategy())
    print(runner.execute_workout(10.0))

    # Dynamically switch to Sprint Strategy mid-program!
    runner.set_strategy(SprintStrategy())
    print(runner.execute_workout(3.0))

    # Switch to Recovery Strategy
    runner.set_strategy(RecoveryStrategy())
    print(runner.execute_workout(5.0))

# Day 144 - Activity 2: The Observer Pattern (Publish-Subscribe Event System)
from abc import ABC, abstractmethod
from typing import List

# 1. Observer Interface
class RaceObserver(ABC):
    @abstractmethod
    def update(self, message: str) -> None:
        pass

# 2. Concrete Observer A: Coach Notification System
class CoachAlert(RaceObserver):
    def update(self, message: str) -> None:
        print(f"📱 [COACH NOTIFICATION]: Received alert -> {message}")

# 3. Concrete Observer B: Vlog Camera Auto-Trigger
class VlogCameraTrigger(RaceObserver):
    def update(self, message: str) -> None:
        print(f"🎥 [CAMERA SYSTEM]: Auto-triggering recording snippet -> {message}")

# 4. Subject (The Publisher / Race Tracker)
class RaceTrackerSubject:
    def __init__(self):
        self._observers: List[RaceObserver] = []
        self._current_checkpoint: str = "Start Line"

    def attach(self, observer: RaceObserver) -> None:
        self._observers.append(observer)
        print(f"➕ [OBSERVER ATTACHED]: New listener subscribed.")

    def detach(self, observer: RaceObserver) -> None:
        self._observers.remove(observer)
        print(f"➖ [OBSERVER DETACHED]: Listener unsubscribed.")

    def notify(self, message: str) -> None:
        print(f"\n📢 [BROADCASTING EVENT]: {message}")
        for observer in self._observers:
            observer.update(message)

    def reach_checkpoint(self, checkpoint_name: str) -> None:
        self._current_checkpoint = checkpoint_name
        self.notify(f"Runner reached checkpoint: {checkpoint_name}!")

# 5. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 144 Activity 2 Observer Pattern...\n")

    # Create the Subject (Race Tracker)
    race = RaceTrackerSubject()

    # Create Observers (Coach and Camera)
    coach = CoachAlert()
    camera = VlogCameraTrigger()

    # Subscribe observers to the race tracker
    race.attach(coach)
    race.attach(camera)

    # Trigger checkpoints (watch all subscribers get notified automatically!)
    race.reach_checkpoint("1km Marker")
    
    print("\n--- Mid-race change: Camera battery dies, detaching camera observer ---")
    race.detach(camera)

    race.reach_checkpoint("5km Finish Line 🏆")

# Day 144 - Activity 3: The Command Pattern (Encapsulating Requests & Actions)
from abc import ABC, abstractmethod
from typing import List

# 1. Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

# 2. Receiver (The underlying equipment / system)
class VlogStudioEquipment:
    def start_camera_recording(self) -> None:
        print("🎥 [EQUIPMENT]: 4K camera rolling and recording active.")

    def calibrate_wireless_mic(self) -> None:
        print("🎙️ [EQUIPMENT]: Wireless microphone noise cancellation calibrated.")

    def upload_to_cloud(self) -> None:
        print("☁️ [EQUIPMENT]: Raw footage uploaded to cloud server successfully.")

# 3. Concrete Commands
class StartRecordingCommand(Command):
    def __init__(self, equipment: VlogStudioEquipment):
        self._equipment = equipment

    def execute(self) -> None:
        print("🔘 [COMMAND]: Executing Start Recording...")
        self._equipment.start_camera_recording()

class CalibrateMicCommand(Command):
    def __init__(self, equipment: VlogStudioEquipment):
        self._equipment = equipment

    def execute(self) -> None:
        print("🔘 [COMMAND]: Executing Microphone Calibration...")
        self._equipment.calibrate_wireless_mic()

class UploadFootageCommand(Command):
    def __init__(self, equipment: VlogStudioEquipment):
        self._equipment = equipment

    def execute(self) -> None:
        print("🔘 [COMMAND]: Executing Cloud Upload...")
        self._equipment.upload_to_cloud()

# 4. Invoker (The Automation Controller that queues and runs commands)
class VlogStudioInvoker:
    def __init__(self):
        self._command_queue: List[Command] = []

    def add_command(self, command: Command) -> None:
        self._command_queue.append(command)

    def run_automation_sequence(self) -> None:
        print("🚀 [INVOKER]: Running automated vlog production sequence...")
        for cmd in self._command_queue:
            cmd.execute()
        self._command_queue.clear()

# 5. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 144 Activity 3 Command Pattern...\n")

    # Receiver
    studio_gear = VlogStudioEquipment()

    # Concrete Commands
    rec_cmd = StartRecordingCommand(studio_gear)
    mic_cmd = CalibrateMicCommand(studio_gear)
    upload_cmd = UploadFootageCommand(studio_gear)

    # Invoker
    remote = VlogStudioInvoker()
    remote.add_command(mic_cmd)
    remote.add_command(rec_cmd)
    remote.add_command(upload_cmd)

    # Execute all queued commands in sequence!
    remote.run_automation_sequence()

# Day 144 - Activity 4: The State Pattern (Managing State-Dependent Behavior)
from abc import ABC, abstractmethod

# 1. State Interface
class WorkoutState(ABC):
    @abstractmethod
    def handle_action(self) -> str:
        pass

# 2. Concrete State A: Warmup
class WarmupState(WorkoutState):
    def handle_action(self) -> str:
        return "🔥 [STATE: WARMUP]: Dynamic stretches and light jogging. Heart rate building up gently."

# 3. Concrete State B: Active Running
class ActiveRunningState(WorkoutState):
    def handle_action(self) -> str:
        return "🏃 [STATE: ACTIVE RUNNING]: Pushing pace! Intervals and tempo strides in full swing."

# 4. Concrete State C: Cooldown
class CooldownState(WorkoutState):
    def handle_action(self) -> str:
        return "🧊 [STATE: COOLDOWN]: Slow walking and deep breathing to lower heart rate safely."

# 5. Context Class (Maintains current state and delegates behavior)
class RunningWorkoutContext:
    def __init__(self, state: WorkoutState):
        self._state = state

    def transition_to(self, state: WorkoutState):
        print(f"\n🔄 [STATE TRANSITION]: Shifting workout phase...")
        self._state = state

    def perform_workout_step(self) -> str:
        return self._state.handle_action()

# 6. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 144 Activity 4 State Pattern...\n")

    # Start workout in Warmup state
    workout = RunningWorkoutContext(WarmupState())
    print(workout.perform_workout_step())

    # Transition to Active Running state mid-workout
    workout.transition_to(ActiveRunningState())
    print(workout.perform_workout_step())

    # Transition to Cooldown state
    workout.transition_to(CooldownState())
    print(workout.perform_workout_step())

# Day 144 - Activity 5: The Template Method Pattern (Algorithm Skeleton)
from abc import ABC, abstractmethod

# 1. Abstract Class defining the Template Method skeleton
class WorkoutRoutineTemplate(ABC):
    
    # The Template Method: Defines the rigid step-by-step skeleton of the workout!
    def execute_routine(self) -> str:
        step1 = self.warmup()
        step2 = self.core_workout()  # Varies depending on the subclass!
        step3 = self.cooldown()
        return f"\n📋 [WORKOUT ROUTINE EXECUTED]:\n  1. {step1}\n  2. {step2}\n  3. {step3}"

    # Concrete step shared by all routines
    def warmup(self) -> str:
        return "Warmup: 5 minutes of dynamic leg swings and light jogging."

    # Abstract step that MUST be implemented by subclasses
    @abstractmethod
    def core_workout(self) -> str:
        pass

    # Concrete step shared by all routines
    def cooldown(self) -> str:
        return "Cooldown: 5 minutes of static stretching and deep breathing."

# 2. Concrete Subclass A: Interval Training Routine
class IntervalRoutine(WorkoutRoutineTemplate):
    def __init__(self, reps: int):
        self.reps = reps

    def core_workout(self) -> str:
        return f"Core Workout: Run {self.reps}x 400m hard track intervals with 1-minute rest!"

# 3. Concrete Subclass B: Long Slow Distance (LSD) Routine
class LongSlowDistanceRoutine(WorkoutRoutineTemplate):
    def __init__(self, distance_km: float):
        self.distance_km = distance_km

    def core_workout(self) -> str:
        return f"Core Workout: Maintain steady aerobic pace for {self.distance_km}km continuous distance."

# 4. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 144 Activity 5 Template Method Pattern...\n")

    # Run Interval Routine
    interval_session = IntervalRoutine(8)
    print(interval_session.execute_routine())

    # Run Long Distance Routine
    lsd_session = LongSlowDistanceRoutine(12.0)
    print(lsd_session.execute_routine())