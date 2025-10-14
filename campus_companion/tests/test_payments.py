import pytest
from src.payments.stripe_integration import create_charge, handle_webhook
from src.payments.paypal_integration import create_paypal_payment

@pytest.fixture
def stripe_payment_data():
    return {
        "amount": 1000,
        "currency": "usd",
        "source": "tok_visa",  # Test token
        "description": "Test Charge"
    }

@pytest.fixture
def paypal_payment_data():
    return {
        "amount": "10.00",
        "currency": "USD",
        "description": "Test PayPal Payment"
    }

def test_create_charge(stripe_payment_data):
    charge = create_charge(**stripe_payment_data)
    assert charge['status'] == 'succeeded'
    assert charge['amount'] == stripe_payment_data['amount']

def test_create_paypal_payment(paypal_payment_data):
    payment = create_paypal_payment(**paypal_payment_data)
    assert payment['state'] == 'created'
    assert payment['transactions'][0]['amount']['total'] == paypal_payment_data['amount']

def test_handle_webhook_success():
    event_data = {
        "id": "evt_test_webhook",
        "type": "payment_intent.succeeded",
        "data": {
            "object": {
                "id": "pi_test_payment",
                "amount": 1000,
                "currency": "usd"
            }
        }
    }
    response = handle_webhook(event_data)
    assert response['status'] == 'success'

def test_handle_webhook_failure():
    event_data = {
        "id": "evt_test_webhook",
        "type": "payment_intent.payment_failed",
        "data": {
            "object": {
                "id": "pi_test_payment",
                "amount": 1000,
                "currency": "usd"
            }
        }
    }
    response = handle_webhook(event_data)
    assert response['status'] == 'failure'