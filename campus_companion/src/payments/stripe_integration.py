import stripe
import os

# Set up Stripe API key
stripe.api_key = os.getenv("STRIPE_API_KEY")

def create_charge(amount, currency, source, description):
    try:
        charge = stripe.Charge.create(
            amount=amount,
            currency=currency,
            source=source,
            description=description
        )
        return charge
    except stripe.error.StripeError as e:
        return {"error": str(e)}

def retrieve_charge(charge_id):
    try:
        charge = stripe.Charge.retrieve(charge_id)
        return charge
    except stripe.error.StripeError as e:
        return {"error": str(e)}

def refund_charge(charge_id):
    try:
        refund = stripe.Refund.create(charge=charge_id)
        return refund
    except stripe.error.StripeError as e:
        return {"error": str(e)}