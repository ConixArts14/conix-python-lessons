# Day 141 - Activity 1: The Strategy Pattern (Interchangeable Algorithms)
from abc import ABC, abstractmethod

# 1. Abstract Strategy Interface
class ShippingStrategy(ABC):
    @abstractmethod
    def calculate_cost(self, weight_kg: float) -> float:
        pass

# 2. Concrete Strategy 1: Standard Shipping
class StandardShipping(ShippingStrategy):
    def calculate_cost(self, weight_kg: float) -> float:
        print("📦 [STANDARD SHIPPING]: Calculating base rate...")
        return weight_kg * 5.0  # $5 per kg

# 3. Concrete Strategy 2: Express Shipping
class ExpressShipping(ShippingStrategy):
    def calculate_cost(self, weight_kg: float) -> float:
        print("⚡ [EXPRESS SHIPPING]: Calculating fast-track rate...")
        return (weight_kg * 10.0) + 15.0  # $10 per kg + $15 flat fee

# 4. Concrete Strategy 3: Overnight VIP Shipping
class OvernightShipping(ShippingStrategy):
    def calculate_cost(self, weight_kg: float) -> float:
        print("🌙 [OVERNIGHT SHIPPING]: Calculating priority VIP rate...")
        return (weight_kg * 20.0) + 30.0  # $20 per kg + $30 flat fee

# 5. Context Class that uses the Strategy
class Order:
    def __init__(self, items: list, weight_kg: float, strategy: ShippingStrategy):
        self.items = items
        self.weight_kg = weight_kg
        self._shipping_strategy = strategy  # Composition: storing the strategy

    def set_shipping_strategy(self, strategy: ShippingStrategy):
        """Allows changing the strategy dynamically at runtime"""
        print(f"🔄 [STRATEGY CHANGED] Switched shipping method.")
        self._shipping_strategy = strategy

    def checkout(self):
        shipping_cost = self._shipping_strategy.calculate_cost(self.weight_kg)
        print(f"🛒 Order items: {self.items}")
        print(f"💰 Total Shipping Cost: ${shipping_cost:.2f}\n")

# 6. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 141 Activity 1 Program...\n")

    # Create an order weighing 3.5 kg with Standard Shipping
    my_order = Order(items=["Python Mastery Book", "Mechanical Keyboard"], weight_kg=3.5, strategy=StandardShipping())
    my_order.checkout()

    # Switch strategy to Express Shipping dynamically
    my_order.set_shipping_strategy(ExpressShipping())
    my_order.checkout()

    # Switch strategy to Overnight Shipping dynamically
    my_order.set_shipping_strategy(OvernightShipping())
    my_order.checkout()

# Day 141 - Activity 2: Payment Processing Strategy Pattern
from abc import ABC, abstractmethod

# 1. Abstract Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass

# 2. Concrete Strategy 1: Credit Card
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float) -> str:
        fee = amount * 0.029  # 2.9% gateway processing fee
        total = amount + fee
        return f"💳 [CREDIT CARD]: Paid ${amount:.2f} + ${fee:.2f} fee = Total Charged: ${total:.2f}"

# 3. Concrete Strategy 2: PayPal
class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float) -> str:
        fee = 0.30  # Flat $0.30 fee
        total = amount + fee
        return f"🅿️ [PAYPAL]: Paid ${amount:.2f} + ${fee:.2f} fee = Total Charged: ${total:.2f}"

# 4. Concrete Strategy 3: Crypto Wallet
class CryptoPayment(PaymentStrategy):
    def pay(self, amount: float) -> str:
        return f"🪙 [CRYPTO WALLET]: Paid ${amount:.2f} with 0% gas fee!"

# 5. Context Class (The Shopping Cart)
class CheckoutCart:
    def __init__(self, cart_id: int, amount: float):
        self.cart_id = cart_id
        self.amount = amount

    def process_checkout(self, payment_strategy: PaymentStrategy):
        print(f"🛍️ Processing Cart #{self.cart_id} (Subtotal: ${self.amount:.2f})")
        result = payment_strategy.pay(self.amount)
        print(result)
        print("-" * 50)

# 6. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 141 Activity 2 Program...\n")

    # Create a shopping cart worth $150.00
    cart = CheckoutCart(cart_id=141, amount=150.00)

    # Customer checks out using Credit Card
    cart.process_checkout(CreditCardPayment())

    # Customer checks out using PayPal
    cart.process_checkout(PayPalPayment())

    # Customer checks out using Crypto Wallet
    cart.process_checkout(CryptoPayment())

# Day 141 - Activity 3: Functional Strategy Pattern (Pythonic Callables)
from typing import Callable, List

# 1. Define Strategy Functions (No classes required!)
def uppercase_strategy(data: str) -> str:
    return data.upper()

def slugify_strategy(data: str) -> str:
    return data.lower().replace(" ", "-")

def kebab_case_strategy(data: str) -> str:
    return f"*** {data} ***"

# 2. Context Class receiving a Callable (Function) Strategy
class DataProcessor:
    def __init__(self, data_items: List[str]):
        self.data_items = data_items

    def process(self, formatter: Callable[[str], str]):
        print("\n⚙️ [DATA PROCESSOR] Running transformation strategy...")
        transformed = [formatter(item) for item in self.data_items]
        for original, result in zip(self.data_items, transformed):
            print(f"  • '{original}'  ➡️  '{result}'")

# 3. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 141 Activity 3 Functional Strategy Program...\n")

    raw_data = [
        "Python Full Stack Mastery",
        "Observer and Strategy Patterns",
        "Day 141 GitHub Streak"
    ]

    processor = DataProcessor(raw_data)

    # Strategy 1: Using named function
    print("--- Strategy 1: Uppercase ---")
    processor.process(uppercase_strategy)

    # Strategy 2: Using named function
    print("--- Strategy 2: Slugify ---")
    processor.process(slugify_strategy)

    # Strategy 3: Using a Lambda (inline strategy) on the fly!
    print("--- Strategy 3: Inline Lambda (Reversing text) ---")
    processor.process(lambda text: text[::-1])

# Day 141 - Activity 4: Dynamic Strategy Registry Pattern
from abc import ABC, abstractmethod

# 1. Abstract Strategy Interface
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, total: float) -> float:
        pass

# 2. Strategy Registry Factory
class DiscountRegistry:
    _registry = {}

    @classmethod
    def register(cls, name: str):
        def decorator(subclass):
            cls._registry[name.lower()] = subclass
            return subclass
        return decorator

    @classmethod
    def get_strategy(cls, name: str) -> DiscountStrategy:
        strategy_class = cls._registry.get(name.lower())
        if not strategy_class:
            raise ValueError(f"Unknown discount strategy: '{name}'")
        return strategy_class()

# 3. Concrete Strategies (Self-Registering via Decorator)
@DiscountRegistry.register("vip")
class VIPDiscount(DiscountStrategy):
    def apply_discount(self, total: float) -> float:
        print("👑 [VIP DISCOUNT]: Applying 20% off!")
        return total * 0.80

@DiscountRegistry.register("holiday")
class HolidayDiscount(DiscountStrategy):
    def apply_discount(self, total: float) -> float:
        print("🎄 [HOLIDAY DISCOUNT]: Applying $15 flat holiday discount!")
        return max(0.0, total - 15.0)

@DiscountRegistry.register("none")
class NoDiscount(DiscountStrategy):
    def apply_discount(self, total: float) -> float:
        print("🏷️ [STANDARD]: No discount applied.")
        return total

# 4. Context Class
class ShoppingCheckout:
    def __init__(self, cart_total: float):
        self.cart_total = cart_total

    def checkout_with_strategy_name(self, strategy_name: str):
        print(f"\n🛒 Checking out subtotal: ${self.cart_total:.2f}")
        # Dynamically fetch the strategy from the registry by string name!
        strategy = DiscountRegistry.get_strategy(strategy_name)
        final_price = strategy.apply_discount(self.cart_total)
        print(f"💰 Final Price to Pay: ${final_price:.2f}")

# 5. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 141 Activity 4 Dynamic Strategy Registry...\n")

    cart = ShoppingCheckout(cart_total=100.00)

    # Test dynamic strategy lookup using strings
    cart.checkout_with_strategy_name("vip")
    cart.checkout_with_strategy_name("holiday")
    cart.checkout_with_strategy_name("none")

# Day 141 - Activity 5: The Strategy Pipeline (Composite Pattern)
from abc import ABC, abstractmethod
from typing import List

# 1. Abstract Strategy Interface
class PipelineStep(ABC):
    @abstractmethod
    def execute(self, total: float) -> float:
        pass

# 2. Concrete Strategy 1: Apply Seasonal Discount
class DiscountStep(PipelineStep):
    def __init__(self, discount_percent: float):
        self.discount_percent = discount_percent

    def execute(self, total: float) -> float:
        discount_amount = total * (self.discount_percent / 100)
        new_total = total - discount_amount
        print(f"🏷️ [DISCOUNT STEP]: Applied {self.discount_percent}% off (-${discount_amount:.2f}) -> Subtotal: ${new_total:.2f}")
        return new_total

# 3. Concrete Strategy 2: Apply State Sales Tax
class TaxStep(PipelineStep):
    def __init__(self, tax_rate_percent: float):
        self.tax_rate_percent = tax_rate_percent

    def execute(self, total: float) -> float:
        tax_amount = total * (self.tax_rate_percent / 100)
        new_total = total + tax_amount
        print(f"🏛️ [TAX STEP]: Applied {self.tax_rate_percent}% tax (+${tax_amount:.2f}) -> Subtotal: ${new_total:.2f}")
        return new_total

# 4. Concrete Strategy 3: Apply Handling Fee
class HandlingFeeStep(PipelineStep):
    def __init__(self, fee: float):
        self.fee = fee

    def execute(self, total: float) -> float:
        new_total = total + self.fee
        print(f"📦 [HANDLING STEP]: Added flat fee (+${self.fee:.2f}) -> Final Total: ${new_total:.2f}")
        return new_total

# 5. Composite Pipeline Manager
class CheckoutPipeline:
    def __init__(self):
        self.steps: List[PipelineStep] = []

    def add_step(self, step: PipelineStep):
        self.steps.append(step)
        return self  # Method chaining support!

    def run_pipeline(self, initial_amount: float) -> float:
        print(f"🚀 [PIPELINE START]: Initial Amount: ${initial_amount:.2f}")
        print("-" * 50)
        current_total = initial_amount
        for step in self.steps:
            current_total = step.execute(current_total)
        print("-" * 50)
        print(f"🏁 [PIPELINE END]: Final Amount to Charge: ${current_total:.2f}\n")
        return current_total

# 6. Execution Block
if __name__ == "__main__":
    print("🚀 Initializing Day 141 Activity 5 Strategy Pipeline...\n")

    # Build a checkout pipeline dynamically using method chaining
    pipeline = (
        CheckoutPipeline()
        .add_step(DiscountStep(discount_percent=15.0)) # 15% off first
        .add_step(TaxStep(tax_rate_percent=8.5))       # 8.5% tax next
        .add_step(HandlingFeeStep(fee=5.00))           # $5 flat fee last
    )

    # Run the entire strategy pipeline on a $200 cart
    pipeline.run_pipeline(initial_amount=200.00)