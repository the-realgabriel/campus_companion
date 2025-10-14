from abc import ABC, abstractmethod

class PaymentProvider(ABC):
    @abstractmethod
    def create_payment(self, amount, currency):
        pass

    @abstractmethod
    def refund_payment(self, payment_id):
        pass

    @abstractmethod
    def get_payment_status(self, payment_id):
        pass

class StripeProvider(PaymentProvider):
    def create_payment(self, amount, currency):
        # Logic to create a payment with Stripe
        pass

    def refund_payment(self, payment_id):
        # Logic to refund a payment with Stripe
        pass

    def get_payment_status(self, payment_id):
        # Logic to get payment status from Stripe
        pass

class PayPalProvider(PaymentProvider):
    def create_payment(self, amount, currency):
        # Logic to create a payment with PayPal
        pass

    def refund_payment(self, payment_id):
        # Logic to refund a payment with PayPal
        pass

    def get_payment_status(self, payment_id):
        # Logic to get payment status from PayPal
        pass