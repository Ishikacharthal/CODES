from abc import ABC, abstractmethod
from functools import wraps
from datetime import datetime
import uuid

class Receipt:
    def __init__(self, amount, method, status):
        self.txn_id = str(uuid.uuid4())[:8]
        self.amount = amount
        self.method = method
        self.status = status
        self.timestamp = datetime.now()

    def __str__(self):
        return (
            f"\nTransaction ID : {self.txn_id}\n"
            f"Amount         : ₹{self.amount}\n"
            f"Method         : {self.method}\n"
            f"Status         : {self.status}\n"
            f"Date & Time    : {self.timestamp.strftime('%d-%m-%Y %H:%M:%S')}"
        )

def log_transaction(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("\n========== PAYMENT STARTED ==========")
        result = func(*args, **kwargs)
        print("========== PAYMENT COMPLETED ==========")
        return result
    return wrapper

class PaymentStrategy(ABC):
    name = "Payment"

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    name = "Credit Card"

    def __init__(self, card_number, cvv, expiry):
        self.card_number = card_number
        self.cvv = cvv
        self.expiry = expiry

    def validate(self):
        return len(self.card_number) == 16 and len(self.cvv) == 3

    def pay(self, amount):
        if self.validate():
            return Receipt(amount, self.name, "SUCCESS")
        return Receipt(amount, self.name, "FAILED")

class PayPalPayment(PaymentStrategy):
    name = "PayPal"

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def validate(self):
        return "@" in self.email and len(self.password) >= 6

    def pay(self, amount):
        if self.validate():
            return Receipt(amount, self.name, "SUCCESS")
        return Receipt(amount, self.name, "FAILED")

class UPIPayment(PaymentStrategy):
    name = "UPI"

    def __init__(self, upi_id):
        self.upi_id = upi_id

    def validate(self):
        return "@" in self.upi_id

    def pay(self, amount):
        if self.validate():
            return Receipt(amount, self.name, "SUCCESS")
        return Receipt(amount, self.name, "FAILED")

class NetBankingPayment(PaymentStrategy):
    name = "Net Banking"

    def __init__(self, bank_name, account_number):
        self.bank_name = bank_name
        self.account_number = account_number

    def validate(self):
        return len(self.account_number) >= 10

    def pay(self, amount):
        if self.validate():
            return Receipt(amount, self.name, "SUCCESS")
        return Receipt(amount, self.name, "FAILED")

class PaymentProcessor:
    _registry = {}

    def __init__(self, strategy=None):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy
        print(f"\n[CONFIG] Strategy changed to {strategy.name}")

    @log_transaction
    def process_payment(self, amount):
        if self.strategy is None:
            raise Exception("No payment strategy selected.")
        return self.strategy.pay(amount)

    @classmethod
    def register_strategy(cls, key, strategy_class):
        cls._registry[key] = strategy_class

    @classmethod
    def available_methods(cls):
        return list(cls._registry.keys())

    @classmethod
    def create(cls, key, **kwargs):
        strategy = cls._registry[key](**kwargs)
        return cls(strategy)


PaymentProcessor.register_strategy("credit_card", CreditCardPayment)
PaymentProcessor.register_strategy("paypal", PayPalPayment)
PaymentProcessor.register_strategy("upi", UPIPayment)
PaymentProcessor.register_strategy("net_banking", NetBankingPayment)

print("Available Payment Methods:")
print(PaymentProcessor.available_methods())

processor = PaymentProcessor.create("upi", upi_id="ishika@oksbi")
receipt = processor.process_payment(1500)
print(receipt)

processor.set_strategy(
    CreditCardPayment("1234567812345678", "123", "12/29")
)
receipt = processor.process_payment(2500)
print(receipt)

processor.set_strategy(
    NetBankingPayment("SBI", "123456789012")
)
receipt = processor.process_payment(5000)
print(receipt)

processor.set_strategy(
    PayPalPayment("abcgmail.com", "123")
)
receipt = processor.process_payment(1000)
print(receipt)