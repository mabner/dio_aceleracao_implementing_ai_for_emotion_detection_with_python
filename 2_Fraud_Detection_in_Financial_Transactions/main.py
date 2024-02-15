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
    #for transaction in transactions:

        # TODO: Unpack the transaction into its components: id, value, and threshold and convert transaction value
        #  and fraud threshold to integers

    # TODO: Check if the transaction value exceeds the fraud threshold

    return '\n'.join(suspicious_transactions)

# TODO: Print the suspicious transactions list
print(transactions)