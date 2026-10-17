# Day 142 - Activity 1: The Decorator Pattern (Dynamic Behavior Extension)
from abc import ABC, abstractmethod

# 1. Component Interface
class Coffee(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> float:
        pass

# 2. Concrete Component (Base Object)
class BasicCoffee(Coffee):
    def get_description(self) -> str:
        return "☕ Basic Black Coffee"

    def get_cost(self) -> float:
        return 2.00  # Base price $2.00

# 3. Base Decorator Class
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee  # Storing the wrapped coffee object

    def get_description(self) -> str:
        return self._coffee.get_description()

    def get_cost(self) -> float:
        return self._coffee.get_cost()

# 4. Concrete Decorators
class MilkDecorator(CoffeeDecorator):
    def get_description(self) -> str:
        return f"{self._coffee.get_description()} + 🥛 Whole Milk"

    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.50

class CaramelDecorator(CoffeeDecorator):
    def get_description(self) -> str:
        return f"{self._coffee.get_description()} + 🍯 Caramel Syrup"

    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.75

# 5. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 142 Activity 1 Decorator Pattern...\n")

    # Order 1: Basic Coffee
    my_coffee = BasicCoffee()
    print(f"Order 1: {my_coffee.get_description()} -> Price: ${my_coffee.get_cost():.2f}")

    # Order 2: Basic Coffee + Milk
    milk_coffee = MilkDecorator(my_coffee)
    print(f"Order 2: {milk_coffee.get_description()} -> Price: ${milk_coffee.get_cost():.2f}")

    # Order 3: Basic Coffee + Milk + Caramel Syrup (Layered Decorators!)
    caramel_milk_coffee = CaramelDecorator(milk_coffee)
    print(f"Order 3: {caramel_milk_coffee.get_description()} -> Price: ${caramel_milk_coffee.get_cost():.2f}")

# Day 142 - Activity 2: Python Native Function Decorators (@ Syntax)
import time
from functools import wraps

# 1. Custom Decorator Function
def log_activity(func):
    @wraps(func)  # Preserves the original function's name and docstring
    def wrapper(*args, **kwargs):
        print(f"🟢 [LOG]: Starting execution of '{func.__name__}'...")
        start_time = time.time()
        
        # Execute the actual function
        result = func(*args, **kwargs)
        
        end_time = time.time()
        duration = end_time - start_time
        print(f"🔴 [LOG]: Finished '{func.__name__}' in {duration:.4f} seconds.\n")
        return result
    return wrapper

# 2. Applying the decorator using @ syntax
@log_activity
def process_video_upload(filename: str):
    print(f"🎥 Uploading new birthday camera vlog: {filename}...")
    time.sleep(1.0)  # Simulate processing time
    print(f"✅ Upload complete for {filename}!")

@log_activity
def calculate_running_pace(distance_km: float, time_minutes: float):
    print(f"🏃 Calculating pace for {distance_km}km in {time_minutes} mins...")
    pace = time_minutes / distance_km
    print(f"⏱️ Average pace: {pace:.2f} min/km")

# 3. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 142 Activity 2 Native Function Decorators...\n")
    
    # Call decorated functions
    process_video_upload("birthday_vlog_day1.mp4")
    calculate_running_pace(5.0, 24.5)

# Day 142 - Activity 3: Stacked Function Decorators (Combining Multiple Wrappers)
import time
from functools import wraps

# 1. Decorator 1: Logging & Timing
def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"🟢 [LOG]: Calling '{func.__name__}'...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"🔴 [LOG]: '{func.__name__}' finished in {end - start:.4f}s.")
        return result
    return wrapper

# 2. Decorator 2: Input Validation
def validate_positive_distance(func):
    @wraps(func)
    def wrapper(distance_km, *args, **kwargs):
        if distance_km <= 0:
            print(f"❌ [VALIDATION ERROR]: Distance must be greater than 0! Got {distance_km}km.")
            return None
        print(f"✅ [VALIDATION PASSED]: Distance {distance_km}km is valid.")
        return func(distance_km, *args, **kwargs)
    return wrapper

# 3. Target Function with Stacked Decorators (Bottom runs first, then top wraps it!)
@log_execution
@validate_positive_distance
def record_run_session(distance_km: float, route_name: str):
    print(f"🏃 Recording running session on '{route_name}' for {distance_km}km...")
    time.sleep(0.5)
    print(f"🏆 Session successfully saved!")
    return "Saved"

# 4. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 142 Activity 3 Stacked Decorators...\n")

    print("--- Test 1: Valid Run Session ---")
    record_run_session(5.0, "Tagum City Track")

    print("\n--- Test 2: Invalid Run Session (Negative Distance) ---")
    record_run_session(-1.5, "Faulty Route")

# Day 142 - Activity 4: Parameterized Decorators (Decorators with Arguments)
import time
from functools import wraps
import random

# 1. Parameterized Decorator Factory (Takes arguments!)
def retry_on_failure(max_attempts: int = 3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                attempts += 1
                try:
                    print(f"🔄 [ATTEMPT {attempts}/{max_attempts}] Calling '{func.__name__}'...")
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"⚠️ [ERROR CAUGHT]: {e}")
                    if attempts >= max_attempts:
                        print(f"❌ [FAILED]: Max attempts ({max_attempts}) reached. Operation aborted.")
                        raise e
                    print(f"⏱️ Retrying in 0.5 seconds...\n")
                    time.sleep(0.5)
        return wrapper
    return decorator

# 2. Target Function with Parameterized Decorator
@retry_on_failure(max_attempts=3)
def upload_birthday_vlog_to_cloud():
    # Simulate an unstable network connection (fails randomly)
    if random.random() < 0.7:  # 70% chance of failing
        raise ConnectionError("Server timeout while uploading video!")
    return "🎥 Birthday camera vlog uploaded successfully!"

# 3. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 142 Activity 4 Parameterized Decorators...\n")
    
    # Set seed so you can test retries predictably
    random.seed(10)  

    try:
        success_message = upload_birthday_vlog_to_cloud()
        print(f"\n{success_message} 🏆")
    except Exception:
        print("\n💥 Final execution failed, but the retry logic handled the attempts gracefully!")

# Day 142 - Activity 5: Stateful Cache Decorator (Memoization)
import time
from functools import wraps

# 1. Stateful Cache Decorator
def memoize_cache(func):
    cache = {}
    cache_hits = 0
    cache_misses = 0

    @wraps(func)
    def wrapper(*args):
        nonlocal cache_hits, cache_misses
        if args in cache:
            cache_hits += 1
            print(f"⚡ [CACHE HIT]: Returning lightning-fast cached result for {args} (Hits: {cache_hits})")
            return cache[args]
        
        cache_misses += 1
        print(f"🐢 [CACHE MISS]: Computing expensive result for {args} (Misses: {cache_misses})")
        result = func(*args)
        cache[args] = result
        return result
    
    # Attach a stats helper function to the wrapper
    wrapper.stats = lambda: print(f"📊 [CACHE STATS]: Total Hits: {cache_hits} | Total Misses: {cache_misses}")
    return wrapper

# 2. Target Function simulating an expensive database calculation
@memoize_cache
def calculate_race_split_time(distance_km: int):
    print("⏳ Running heavy database query & race split simulation...")
    time.sleep(0.8)  # Simulate delay
    return f"Result: Completed {distance_km}km split in {distance_km * 4.5:.1f} minutes!"

# 3. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 142 Activity 5 Stateful Cache Decorator...\n")

    print("--- Test 1: First call for 5km (Cache Miss) ---")
    print(calculate_race_split_time(5))

    print("\n--- Test 2: Second call for 5km (Cache Hit!) ---")
    print(calculate_race_split_time(5))

    print("\n--- Test 3: First call for 10km (Cache Miss) ---")
    print(calculate_race_split_time(10))

    print("\n--- Test 4: Second call for 10km (Cache Hit!) ---")
    print(calculate_race_split_time(10))

    print("\n----------------------------------------")
    calculate_race_split_time.stats()