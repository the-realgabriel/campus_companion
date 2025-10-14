def format_currency(amount):
    return f"₦{amount:,.2f}"

def calculate_percentage(part, whole):
    if whole == 0:
        return 0
    return (part / whole) * 100

def validate_input(value, value_type):
    if value_type == 'number':
        return isinstance(value, (int, float)) and value >= 0
    elif value_type == 'string':
        return isinstance(value, str) and len(value) > 0
    return False

def generate_unique_id():
    import uuid
    return str(uuid.uuid4())