def detect_fraud(transaction_id, amount, date):
    """
    Detects potential fraud based on simple rules.

    Args:
        transaction_id (str): The transaction ID.
        amount (float): The transaction amount.
        date (str): The transaction date in YYYY-MM-DD format.

    Returns:
        str: A message indicating whether the transaction is potentially fraudulent.
    """

    # Basic fraud detection rules (adjust as needed)
    if amount > 100000:  # Large transaction amount
        return "Potential high-value fraud detected."
    elif date.startswith('2023-12'):  # Suspicious date range (adjust as needed)
        return "Potential fraudulent transaction detected."
    else:
        return "Transaction appears legitimate."

# Get input from the user
transaction_id = input("Enter transaction ID: ")
amount = float(input("Enter amount: "))
date = input("Enter date (YYYY-MM-DD): ")

# Detect fraud
result = detect_fraud(transaction_id, amount, date)
print(result)