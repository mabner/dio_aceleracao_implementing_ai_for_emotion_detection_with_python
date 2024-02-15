n = int(input())
lines = []

for n in range(0, n):
    lines.append(input())

# TODO: Split each line into individual transactions and append them to a transaction list
transactions = [line.split(", ") for line in lines]


# TODO: Define a function to detect fraudulent transactions
def detect_frauds(transactions):
    suspicious_transactions = []

    # TODO: Iterate over each transaction
    for transaction in transactions:

        # TODO: Unpack the transaction into its components: id, value, and threshold and convert
        #  transaction value and fraud threshold to integers
        for unpacked in transaction:
            transaction_id, transaction_value, transaction_fraud_threshold = unpacked.split(",")

            # TODO: Check if the transaction value exceeds the fraud threshold
            if (transaction_value >= transaction_fraud_threshold and transaction_id
                    not in suspicious_transactions):
                suspicious_transactions.append(transaction_id)
            else:
                continue


    return '\n'.join(suspicious_transactions)


# TODO: Print the suspicious transactions list
print(detect_frauds(transactions))
