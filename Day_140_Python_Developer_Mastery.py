# Day 140 - Activity 1: The Observer Pattern (Event-Driven Architecture)
from abc import ABC, abstractmethod
from typing import List

# 1. Abstract Observer Interface
class Subscriber(ABC):
    @abstractmethod
    def update(self, event_name: str, data: dict):
        pass

# 2. Concrete Observer 1: Email Subscriber
class EmailSubscriber(Subscriber):
    def update(self, event_name: str, data: dict):
        print(f"📧 [EMAIL NOTIFICATION]: Event '{event_name}' received! Payload: {data}")

# 3. Concrete Observer 2: Audit Logger Subscriber
class LoggerSubscriber(Subscriber):
    def update(self, event_name: str, data: dict):
        print(f"📝 [AUDIT LOG]: Event '{event_name}' recorded in system history.")

# 4. Subject / Publisher Class
class EventPublisher:
    def __init__(self):
        self._subscribers: List[Subscriber] = []

    def subscribe(self, subscriber: Subscriber):
        if subscriber not in self._subscribers:
            self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Subscriber):
        if subscriber in self._subscribers:
            self._subscribers.remove(subscriber)

    def notify(self, event_name: str, data: dict):
        print(f"\n📢 [BROADCASTING EVENT]: '{event_name}'")
        for subscriber in self._subscribers:
            subscriber.update(event_name, data)

# 5. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 140 Activity 1 Program...\n")

    # Create Publisher
    publisher = EventPublisher()

    # Create Observers
    email_sub = EmailSubscriber()
    logger_sub = LoggerSubscriber()

    # Register Observers
    publisher.subscribe(email_sub)
    publisher.subscribe(logger_sub)

    # Trigger Event 1
    publisher.notify("USER_REGISTERED", {"user_id": 101, "name": "Conix"})

    # Trigger Event 2
    publisher.notify("PAYMENT_SUCCESS", {"order_id": 9921, "amount": "$50.00"})

# Day 140 - Activity 2: Topic-Based Observer Pattern
from abc import ABC, abstractmethod
from typing import List, Dict

# 1. Abstract Observer Interface
class Subscriber(ABC):
    @abstractmethod
    def update(self, event_name: str, data: dict):
        pass

# 2. Concrete Subscribers
class WelcomeEmailSubscriber(Subscriber):
    def update(self, event_name: str, data: dict):
        print(f"📧 [WELCOME EMAIL SENT]: To {data.get('email')} for event '{event_name}'")

class SecurityAuditSubscriber(Subscriber):
    def update(self, event_name: str, data: dict):
        print(f"🛡️ [SECURITY AUDIT LOG]: Logged sensitive action -> {event_name}")

# 3. Topic-Based Publisher Class
class TopicEventPublisher:
    def __init__(self):
        # Dictionary mapping event names to a list of subscribers
        self._subscribers: Dict[str, List[Subscriber]] = {}

    def subscribe(self, event_name: str, subscriber: Subscriber):
        event_name = event_name.upper()
        if event_name not in self._subscribers:
            self._subscribers[event_name] = []
        if subscriber not in self._subscribers[event_name]:
            self._subscribers[event_name].append(subscriber)

    def notify(self, event_name: str, data: dict):
        event_name = event_name.upper()
        print(f"\n📢 [BROADCASTING TOPIC]: '{event_name}'")
        
        # Only notify subscribers registered for this specific event topic
        if event_name in self._subscribers:
            for subscriber in self._subscribers[event_name]:
                subscriber.update(event_name, data)
        else:
            print(f"⚠️ No subscribers found for topic '{event_name}'.")

# 4. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 140 Activity 2 Program...\n")

    publisher = TopicEventPublisher()

    welcome_email = WelcomeEmailSubscriber()
    security_log = SecurityAuditSubscriber()

    # Subscribe to specific topics
    publisher.subscribe("USER_REGISTERED", welcome_email)
    publisher.subscribe("USER_REGISTERED", security_log)
    publisher.subscribe("SECURITY_BREACH_ATTEMPT", security_log) # Security listens to breaches too

    # Trigger Event 1: User Registered (Both should respond)
    publisher.notify("USER_REGISTERED", {"email": "conix@python.dev", "user_id": 140})

    # Trigger Event 2: Security Breach (Only security log should respond)
    publisher.notify("SECURITY_BREACH_ATTEMPT", {"ip": "192.168.1.50", "status": "blocked"})

# Day 140 - Activity 3: The Global Event Bus (Enterprise Event Hub)
from typing import List, Dict, Callable, Any

# 1. Central Event Bus (Registry & Publisher Combined)
class EventBus:
    _listeners: Dict[str, List[Callable[[Any], None]]] = {}

    @classmethod
    def subscribe(cls, event_name: str, callback: Callable[[Any], None]):
        event_name = event_name.upper()
        if event_name not in cls._listeners:
            cls._listeners[event_name] = []
        if callback not in cls._listeners[event_name]:
            cls._listeners[event_name].append(callback)
            print(f"🔗 [EVENT BUS]: Registered listener -> '{event_name}'")

    @classmethod
    def publish(cls, event_name: str, payload: Any):
        event_name = event_name.upper()
        print(f"\n⚡ [EVENT BUS PUBLISH]: Broadcasting '{event_name}' with payload: {payload}")
        if event_name in cls._listeners:
            for callback in cls._listeners[event_name]:
                callback(payload)
        else:
            print(f"⚠️ [EVENT BUS]: No active listeners for '{event_name}'")

# 2. Independent Application Modules acting as Listeners (Callbacks)
def send_push_notification(data: dict):
    print(f"📱 [PUSH MODULE]: Sending alert -> '{data.get('msg')}'")

def update_analytics_dashboard(data: dict):
    print(f"📊 [ANALYTICS MODULE]: Recording metric for user '{data.get('user')}'")

def write_audit_log(data: dict):
    print(f"📝 [AUDIT MODULE]: Secure log recorded for transaction ID: {data.get('order_id')}")

# 3. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 140 Activity 3 Global Event Bus Program...\n")

    # Modules subscribe to events through the Central Event Bus
    EventBus.subscribe("ORDER_PLACED", send_push_notification)
    EventBus.subscribe("ORDER_PLACED", update_analytics_dashboard)
    EventBus.subscribe("ORDER_PLACED", write_audit_log)
    
    EventBus.subscribe("USER_LOGIN", update_analytics_dashboard)

    # Trigger Event 1 from anywhere in the app
    EventBus.publish("ORDER_PLACED", {"user": "Conix", "order_id": 5001, "msg": "Your Python mastery guide is ready!"})
    
    # Trigger Event 2
    EventBus.publish("USER_LOGIN", {"user": "Eona", "status": "active"})