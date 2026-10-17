# Day 143 - Activity 1: The Adapter Pattern (Bridging Incompatible Interfaces)
from abc import ABC, abstractmethod

# 1. Modern Target Interface that our system expects
class ModernRunnerDashboard(ABC):
    @abstractmethod
    def display_run_summary(self) -> str:
        pass

# 2. Modern Concrete Implementation
class StandardRunner(ModernRunnerDashboard):
    def __init__(self, distance_km: float, pace_min_km: float):
        self.distance_km = distance_km
        self.pace_min_km = pace_min_km

    def display_run_summary(self) -> str:
        return f"🏃 [MODERN RUNNER]: Completed {self.distance_km}km at {self.pace_min_km} min/km pace."

# 3. Legacy (Incompatible) Class from an older system version
class LegacyTracker:
    def get_old_data_format(self):
        # Returns raw legacy data dictionary (using miles instead of km!)
        return {"dist_miles": 3.1, "time_min": 25.0}

# 4. The Adapter Class (Bridges Legacy Tracker to Modern Dashboard Interface)
class LegacyTrackerAdapter(ModernRunnerDashboard):
    def __init__(self, legacy_tracker: LegacyTracker):
        self.legacy_tracker = legacy_tracker

    def display_run_summary(self) -> str:
        # Fetch raw legacy data
        raw_data = self.legacy_tracker.get_old_data_format()
        
        # Translate legacy units (miles to kilometers -> 1 mile = 1.609 km)
        km_distance = raw_data["dist_miles"] * 1.609
        calculated_pace = raw_data["time_min"] / km_distance
        
        return f"🔄 [ADAPTER WRAPPER]: Converted legacy data -> {km_distance:.2f}km at {calculated_pace:.2f} min/km pace."

# 5. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 143 Activity 1 Adapter Pattern...\n")

    # Test 1: Native modern runner object
    modern_run = StandardRunner(5.0, 4.5)
    print(modern_run.display_run_summary())

    # Test 2: Legacy runner wrapped seamlessly inside the Adapter!
    old_system = LegacyTracker()
    adapted_run = LegacyTrackerAdapter(old_system)
    print(adapted_run.display_run_summary())

    # Day 143 - Activity 2: The Facade Pattern (Simplified Unified Interface)

# 1. Complex Subsystem 1: Camera Hardware
class CameraSubsystem:
    def power_on(self):
        print("📸 [CAMERA]: Lens open, sensor initialized, 4K recording ready.")

# 2. Complex Subsystem 2: Audio Recording
class AudioSubsystem:
    def calibrate_mics(self):
        print("🎙️ [AUDIO]: Noise-canceling calibrated, wireless mic connected.")

# 3. Complex Subsystem 3: Cloud Upload & Storage
class CloudStorageSubsystem:
    def upload_raw_footage(self, filename: str):
        print(f"☁️ [CLOUD]: Uploading '{filename}' to secure server...")

# 4. The Facade: Simplifies the complex subsystems into one clean interface!
class VlogProductionFacade:
    def __init__(self):
        self.camera = CameraSubsystem()
        self.audio = AudioSubsystem()
        self.cloud = CloudStorageSubsystem()

    def record_and_publish_vlog(self, title: str):
        print(f"🎬 [FACADE]: Starting automated workflow for '{title}'...")
        self.camera.power_on()
        self.audio.calibrate_mics()
        self.cloud.upload_raw_footage(f"{title}.mp4")
        print(f"🏆 [FACADE]: Vlog '{title}' successfully produced and published!\n")

# 5. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 143 Activity 2 Facade Pattern...\n")

    # Client code interacts ONLY with the Facade, hiding all subsystem complexity!
    vlog_studio = VlogProductionFacade()
    vlog_studio.record_and_publish_vlog("Day_143_Coding_Masterclass")

# Day 143 - Activity 3: The Proxy Pattern (Controlled Access & Security)
from abc import ABC, abstractmethod

# 1. Subject Interface
class DatabaseAccess(ABC):
    @abstractmethod
    def get_campaign_metrics(self) -> str:
        pass

# 2. Real Subject (The heavy/sensitive database)
class RealDatabase(DatabaseAccess):
    def get_campaign_metrics(self) -> str:
        return "📊 [SECURE DB]: Returning confidential email campaign conversion metrics & revenue data."

# 3. The Proxy (Controls access and checks security permissions)
class SecurityProxyDatabase(DatabaseAccess):
    def __init__(self, real_database: RealDatabase, user_role: str):
        self._real_database = real_database
        self._user_role = user_role

    def get_campaign_metrics(self) -> str:
        print(f"🔒 [SECURITY PROXY]: Inspecting permissions for user role: '{self._user_role}'...")
        
        # Security check
        if self._user_role.lower() != "admin":
            print(f"❌ [ACCESS DENIED]: Unauthorized role '{self._user_role}' cannot access confidential metrics!")
            return "Access Restricted: Admins Only."
        
        print(f"✅ [ACCESS GRANTED]: Admin privileges verified. Forwarding request to Real Database...")
        return self._real_database.get_campaign_metrics()

# 4. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 143 Activity 3 Proxy Pattern...\n")

    # The actual database instance
    production_db = RealDatabase()

    print("--- Test 1: Access attempt by a regular guest/user ---")
    guest_proxy = SecurityProxyDatabase(production_db, user_role="Guest")
    print(guest_proxy.get_campaign_metrics())

    print("\n--- Test 2: Access attempt by an Admin ---")
    admin_proxy = SecurityProxyDatabase(production_db, user_role="Admin")
    print(admin_proxy.get_campaign_metrics())

# Day 143 - Activity 4: The Composite Pattern (Tree Hierarchies)
from abc import ABC, abstractmethod
from typing import List

# 1. Component Interface
class TrainingComponent(ABC):
    @abstractmethod
    def get_details(self, indent: int = 0) -> str:
        pass

    @abstractmethod
    def get_distance_km(self) -> float:
        pass

# 2. Leaf (Individual Workout - e.g., a single run session)
class WorkoutSession(TrainingComponent):
    def __init__(self, name: str, distance_km: float):
        self.name = name
        self.distance_km = distance_km

    def get_details(self, indent: int = 0) -> str:
        space = "  " * indent
        return f"{space}🏃 [WORKOUT]: {self.name} ({self.distance_km}km)"

    def get_distance_km(self) -> float:
        return self.distance_km

# 3. Composite (Training Week or Block holding multiple workouts/sub-blocks)
class TrainingBlock(TrainingComponent):
    def __init__(self, block_name: str):
        self.block_name = block_name
        self._children: List[TrainingComponent] = []

    def add(self, component: TrainingComponent):
        self._children.append(component)

    def remove(self, component: TrainingComponent):
        self._children.remove(component)

    def get_details(self, indent: int = 0) -> str:
        space = "  " * indent
        result = f"{space}📁 [BLOCK]: {self.block_name} (Total: {self.get_distance_km():.1f}km)\n"
        for child in self._children:
            result += child.get_details(indent + 1) + "\n"
        return result.strip()

    def get_distance_km(self) -> float:
        # Recursively sums up distances from all children in the tree!
        return sum(child.get_distance_km() for child in self._children)

# 4. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 143 Activity 4 Composite Pattern...\n")

    # Create individual workouts (Leaves)
    run_recovery = WorkoutSession("Recovery Run", 5.0)
    run_tempo = WorkoutSession("Tempo Run", 8.0)
    run_long = WorkoutSession("Long Slow Distance", 12.0)
    run_intervals = WorkoutSession("Track Intervals 5k Prep", 6.5)

    # Create Training Blocks (Composites)
    week_one = TrainingBlock("Race Prep Week 1")
    week_one.add(run_recovery)
    week_one.add(run_tempo)

    week_two = TrainingBlock("Race Prep Week 2")
    week_two.add(run_long)
    week_two.add(run_intervals)

    # Master Training Plan (Composite holding other Composites!)
    master_plan = TrainingBlock("Milo Marathon 5k Training Program")
    master_plan.add(week_one)
    master_plan.add(week_two)

    # Print the entire tree structure and calculate total distance uniformly!
    print(master_plan.get_details())
    print(f"\n🏆 Grand Total Program Distance: {master_plan.get_distance_km():.1f} km")

# Day 143 - Activity 5: The Bridge Pattern (Decoupling Abstraction from Implementation)
from abc import ABC, abstractmethod

# 1. Implementation Interface (The Hardware/Screen Platform)
class DisplayPlatform(ABC):
    @abstractmethod
    def render_display(self, data: str) -> str:
        pass

# 2. Concrete Implementations
class SmartwatchScreen(DisplayPlatform):
    def render_display(self, data: str) -> str:
        return f"⌚ [SMARTWATCH SCREEN]: {data} (Optimized for small wrist display)"

class MobileAppScreen(DisplayPlatform):
    def render_display(self, data: str) -> str:
        return f"📱 [MOBILE APP SCREEN]: {data} (Full interactive dashboard graph)"

# 3. Abstraction (The Workout Plan holding a bridge to a Platform)
class WorkoutPlan(ABC):
    def __init__(self, platform: DisplayPlatform):
        self.platform = platform  # This is the "Bridge"!

    @abstractmethod
    def trigger_workout(self) -> str:
        pass

# 4. Refined Abstractions
class IntervalTraining(WorkoutPlan):
    def __init__(self, platform: DisplayPlatform, intervals: int):
        super().__init__(platform)
        self.intervals = intervals

    def trigger_workout(self) -> str:
        details = f"Running {self.intervals}x 400m Track Intervals"
        return self.platform.render_display(details)

class LongSlowDistance(WorkoutPlan):
    def __init__(self, platform: DisplayPlatform, distance_km: float):
        super().__init__(platform)
        self.distance_km = distance_km

    def trigger_workout(self) -> str:
        details = f"Long Slow Distance Run: {self.distance_km}km"
        return self.platform.render_display(details)

# 5. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 143 Activity 5 Bridge Pattern...\n")

    # Create display hardware platforms
    watch = SmartwatchScreen()
    mobile = MobileAppScreen()

    # Combine workouts and platforms independently using the Bridge!
    interval_on_watch = IntervalTraining(watch, 6)
    print(interval_on_watch.trigger_workout())

    print()
    lsd_on_mobile = LongSlowDistance(mobile, 12.5)
    print(lsd_on_mobile.trigger_workout())