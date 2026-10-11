# Day 138 - Activity 1: The Decorator Pattern (Function Wrappers)
import functools
import time

# 1. Define the Decorator Function
def log_task_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"🎬 [START] Executing task: '{func.__name__}'...")
        result = func(*args, **kwargs)
        print(f"✅ [FINISHED] Task: '{func.__name__}' execution complete.\n")
        return result
    return wrapper

# 2. Apply the Decorator to a Function using @
@log_task_execution
def process_data_task():
    print("⚡ Processing task data in progress...")
    time.sleep(1)  # Simulate work

@log_task_execution
def export_report_task(report_name):
    print(f"📊 Exporting report: '{report_name}'...")
    time.sleep(1)  # Simulate work

# 3. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 138 Activity 1 Program...\n")
    
    process_data_task()
    export_report_task("Monthly Performance")

# Day 138 - Activity 1: The Decorator Pattern (Function Wrappers)
import functools
import time

# 1. Define the Decorator Function
def log_task_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"🎬 [START] Executing task: '{func.__name__}'...")
        result = func(*args, **kwargs)
        print(f"✅ [FINISHED] Task: '{func.__name__}' execution complete.\n")
        return result
    return wrapper

# 2. Apply the Decorator to a Function using @
@log_task_execution
def process_data_task():
    print("⚡ Processing task data in progress...")
    time.sleep(1)  # Simulate work

@log_task_execution
def export_report_task(report_name):
    print(f"📊 Exporting report: '{report_name}'...")
    time.sleep(1)  # Simulate work

# 3. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 138 Activity 1 Program...\n")
    
    process_data_task()
    export_report_task("Monthly Performmance")

# Day 138 - Activity 2: Stacking Multiple Decorators (Timing + Logging)
import functools
import time

# 1. First Decorator: Logging
def log_task_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"🎬 [LOG] Starting task: '{func.__name__}'")
        result = func(*args, **kwargs)
        print(f"🏁 [LOG] Finished task: '{func.__name__}'\n")
        return result
    return wrapper

# 2. Second Decorator: Execution Timer
def measure_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(f"⏱️ [PERFORMANCE] '{func.__name__}' took {duration:.4f} seconds to run.")
        return result
    return wrapper

# 3. Stacking Multiple Decorators on a Task Function
@log_task_execution
@measure_execution_time
def heavy_database_query_task():
    print("🗄️ Querying database records...")
    time.sleep(1.5)  # Simulate a slow database query
    print("📦 Records retrieved successfully!")

# 4. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 138 Activity 2 Program...\n")
    heavy_database_query_task()

# Day 138 - Activity 3: Parameterized Decorators (Decorators with Arguments)
import functools
import time

# 1. Parameterized Decorator (3-Layer Structure)
def task_logger_with_prefix(prefix):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"🏷️ [{prefix}] Starting task: '{func.__name__}'")
            result = func(*args, **kwargs)
            print(f"✅ [{prefix}] Completed task: '{func.__name__}'\n")
            return result
        return decorator
    return decorator

# 2. Applying the Parameterized Decorator with a Custom Argument
@task_logger_with_prefix("AUTOMATION-PIPELINE")
def sync_user_database_task(user_count):
    print(f"🔄 Syncing {user_count} user accounts across domains...")
    time.sleep(1)
    print("✨ Sync complete!")

# 3. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 138 Activity 3 Program...\n")
    
    sync_user_database_task(1483)