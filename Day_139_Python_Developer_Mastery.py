# Day 139 - Activity 1: The Factory Pattern (Object Creation Control)
from abc import ABC, abstractmethod

# 1. Base Abstract Product Class
class Notification(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

# 2. Concrete Product 1: Email Notification
class EmailNotification(Notification):
    def send(self, message: str):
        print(f"📧 [EMAIL SENT]: '{message}'")

# 3. Concrete Product 2: SMS Notification
class SMSNotification(Notification):
    def send(self, message: str):
        print(f"📱 [SMS SENT]: '{message}'")

# 4. Factory Class to Encapsulate Object Creation
class NotificationFactory:
    @staticmethod
    def create_notification(channel_type: str) -> Notification:
        channel_type = channel_type.lower()
        if channel_type == "email":
            return EmailNotification()
        elif channel_type == "sms":
            return SMSNotification()
        else:
            raise ValueError(f"Unknown notification channel type: '{channel_type}'")

# 5. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 139 Activity 1 Program...\n")
    
    # Create email notifier via factory
    email_notifier = NotificationFactory.create_notification("email")
    email_notifier.send("Welcome to Day 139 of your Python Mastery Journey!")
    
    # Create SMS notifier via factory
    sms_notifier = NotificationFactory.create_notification("sms")
    sms_notifier.send("Reminder: GitHub commit streak active!")

# Day 139 - Activity 2: Expanding the Factory Pattern
from abc import ABC, abstractmethod

# 1. Base Abstract Product Class
class Notification(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

# 2. Concrete Products
class EmailNotification(Notification):
    def send(self, message: str):
        print(f"📧 [EMAIL SENT]: '{message}'")

class SMSNotification(Notification):
    def send(self, message: str):
        print(f"📱 [SMS SENT]: '{message}'")

# NEW: Concrete Product 3
class PushNotification(Notification):
    def send(self, message: str):
        print(f"🔔 [PUSH NOTIFICATION SENT]: '{message}'")

# 3. Factory Class with Enhanced Types
class NotificationFactory:
    @staticmethod
    def create_notification(channel_type: str) -> Notification:
        channel_type = channel_type.lower()
        if channel_type == "email":
            return EmailNotification()
        elif channel_type == "sms":
            return SMSNotification()
        elif channel_type == "push":
            return PushNotification()
        else:
            raise ValueError(f"Unsupported notification channel: '{channel_type}'")

# 4. Execution Block with Error Handling
if __name__ == "__main__":
    print("🚀 Initializing Day 139 Activity 2 Program...\n")
    
    channels = ["email", "sms", "push", "discord"]
    
    for channel in channels:
        try:
            notifier = NotificationFactory.create_notification(channel)
            notifier.send(f"Testing {channel.upper()} dispatcher channel!")
        except ValueError as e:
            print(f"⚠️ [FACTORY ERROR]: {e}")

# Day 139 - Activity 3: Abstract Factory Pattern (Object Families)
from abc import ABC, abstractmethod

# 1. Abstract Products
class Logger(ABC):
    @abstractmethod
    def log(self, message: str):
        pass

class Dispatcher(ABC):
    @abstractmethod
    def dispatch(self, data: str):
        pass

# 2. Concrete Family 1: Development Environment
class DevLogger(Logger):
    def log(self, message: str):
        print(f"🐛 [DEV-LOG]: {message}")

class DevDispatcher(Dispatcher):
    def dispatch(self, data: str):
        print(f"🧪 [DEV-DISPATCH] Mock sent: {data}")

# 3. Concrete Family 2: Production Environment
class ProdLogger(Logger):
    def log(self, message: str):
        print(f"🛡️ [PROD-LOG]: {message}")

class ProdDispatcher(Dispatcher):
    def dispatch(self, data: str):
        print(f"🚀 [PROD-DISPATCH] Live broadcast sent: {data}")

# 4. Abstract Factory
class SystemFactory(ABC):
    @abstractmethod
    def create_logger(self) -> Logger:
        pass

    @abstractmethod
    def create_dispatcher(self) -> Dispatcher:
        pass

# 5. Concrete Factories for Families
class DevSystemFactory(SystemFactory):
    def create_logger(self) -> Logger:
        return DevLogger()

    def create_dispatcher(self) -> Dispatcher:
        return DevDispatcher()

class ProdSystemFactory(SystemFactory):
    def create_logger(self) -> Logger:
        return ProdLogger()

    def create_dispatcher(self) -> Dispatcher:
        return ProdDispatcher()

# 6. Application Client Logic
def run_system(factory: SystemFactory):
    logger = factory.create_logger()
    dispatcher = factory.create_dispatcher()
    
    logger.log("System initialized successfully.")
    dispatcher.dispatch("Sync payload #139")

# 7. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 139 Activity 3 Program...\n")
    
    print("--- Running in Development Mode ---")
    run_system(DevSystemFactory())
    
    print("\n--- Running in Production Mode ---")
    run_system(ProdSystemFactory())

# Day 139 - Activity 4: Bonus Capstone (Factory + Decorator Combined)
import functools
import time
from abc import ABC, abstractmethod

# 1. Reusing our Decorator from Day 138
def log_task_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"🎬 [DECORATOR START] Running factory method: '{func.__name__}'")
        result = func(*args, **kwargs)
        print(f"✅ [DECORATOR FINISHED] Factory method complete.\n")
        return result
    return wrapper

# 2. Abstract Product
class Notification(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

# 3. Concrete Products
class EmailNotification(Notification):
    def send(self, message: str):
        print(f"📧 [EMAIL SENT]: '{message}'")
        time.sleep(0.5)

class SMSNotification(Notification):
    def send(self, message: str):
        print(f"📱 [SMS SENT]: '{message}'")
        time.sleep(0.5)

# 4. Factory Class decorated with Day 138 Decorator
class NotificationFactory:
    @staticmethod
    @log_task_execution  # Combining Factory with Decorator!
    def create_and_send(channel_type: str, message: str):
        channel_type = channel_type.lower()
        if channel_type == "email":
            notifier = EmailNotification()
        elif channel_type == "sms":
            notifier = SMSNotification()
        else:
            raise ValueError(f"Unknown channel: {channel_type}")
        
        notifier.send(message)
        return notifier

# 5. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 139 Activity 4 Capstone Program...\n")
    
    # Send notifications using our combined pattern
    NotificationFactory.create_and_send("email", "Hello Conix, factory and decorators work together!")
    NotificationFactory.create_and_send("sms", "Python full-stack mastery is leveling up!")

# Day 139 - Activity 5: Dynamic Registry Factory Pattern (Plugin Architecture)
from abc import ABC, abstractmethod

# 1. Base Abstract Product Class
class Notification(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

# 2. Dynamic Registry Factory
class RegistryNotificationFactory:
    _registry = {}  # Dictionary to store registered classes
    
    @classmethod
    def register(cls, name: str):
        """Decorator to register new notification classes automatically"""
        def decorator(subclass):
            cls._registry[name.lower()] = subclass
            return subclass
        return decorator
        
    @classmethod
    def create(cls, name: str) -> Notification:
        """Create an instance based on the registry lookup"""
        creator = cls._registry.get(name.lower())
        if not creator:
            raise ValueError(f"No registered handler for channel: '{name}'")
        return creator()

# 3. Concrete Classes that Self-Register using the Decorator
@RegistryNotificationFactory.register("email")
class EmailNotification(Notification):
    def send(self, message: str):
        print(f"📧 [REGISTRY EMAIL]: '{message}'")

@RegistryNotificationFactory.register("sms")
class SMSNotification(Notification):
    def send(self, message: str):
        print(f"📱 [REGISTRY SMS]: '{message}'")

# NEW: Zero-modification extension! We added Telegram without touching the factory logic.
@RegistryNotificationFactory.register("telegram")
class TelegramNotification(Notification):
    def send(self, message: str):
        print(f"✈️ [REGISTRY TELEGRAM]: '{message}'")

# 4. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 139 Activity 5 Dynamic Registry Program...\n")
    
    # Test dispatching across registered and unregistered channels
    channels = ["email", "sms", "telegram", "slack"]
    
    for channel in channels:
        try:
            notifier = RegistryNotificationFactory.create(channel)
            notifier.send(f"Testing dynamic dispatch for {channel.upper()}!")
        except ValueError as e:
            print(f"⚠️ [REGISTRY ERROR]: {e}")