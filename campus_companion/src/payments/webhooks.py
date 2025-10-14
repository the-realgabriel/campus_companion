from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    if not data:
        return jsonify({'error': 'Invalid payload'}), 400

    event_type = data.get('event_type')

    if event_type == 'payment.succeeded':
        handle_payment_succeeded(data)
    elif event_type == 'payment.failed':
        handle_payment_failed(data)
    elif event_type == 'refund.succeeded':
        handle_refund_succeeded(data)
    else:
        return jsonify({'error': 'Unhandled event type'}), 400

    return jsonify({'status': 'success'}), 200

def handle_payment_succeeded(data):
    # Process successful payment
    payment_info = data.get('data')
    # Add your logic to handle successful payment

def handle_payment_failed(data):
    # Process failed payment
    payment_info = data.get('data')
    # Add your logic to handle failed payment

def handle_refund_succeeded(data):
    # Process successful refund
    refund_info = data.get('data')
    # Add your logic to handle successful refund

if __name__ == '__main__':
    app.run(port=5000)