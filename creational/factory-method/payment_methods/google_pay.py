from decimal import Decimal
from .payment import Payment


class GooglePayPayment(Payment):
    def pay(self, amount: Decimal):
        print(f"Successfully paid ${amount} to merchant using Google Pay")
