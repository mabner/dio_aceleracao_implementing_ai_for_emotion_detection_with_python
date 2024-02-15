n = int(input())
matrices = []

for n in range(0, n):
    matrix = input()
    matrices.append(matrix.split(','))


# TODO: Create a function to calculate accuracy and precision metrics

# TODO: Create a function to find the matrix index with the best combined accuracy and precision
def best_performance(matrices):
    best_index = 0
    best_accuracy = 0
    best_precision = 0
    best_metrics = 0
    # TODO: Define Loop through each matrix to calculate metrics
    for index, matrix in enumerate(matrices):
        # TODO: Define tp, fp fn and tn
        tp, fp, fn, tn = matrix
        tp = float(tp)
        fp = float(fp)
        fn = float(fn)
        tn = float(tn)

        # TODO: Calculate accuracy and precision
        accuracy = (tp + tn) / (tp + fp + fn + tn)
        precision = tp / (tp + fp)

        # TODO: Update best metrics if found
        combined_metrics = [accuracy, precision]
        sum_metrics = [index, sum(combined_metrics)]
        if sum_metrics[1] > best_metrics:
            best_metrics = sum_metrics[1]
            best_index = index
            best_accuracy = accuracy
            best_precision = precision
        else:
            continue

    return (f"""Index: {best_index + 1} 
Accuracy: {round(best_accuracy, 2)}
Precision: {round(best_precision, 2)}""")


# Print the results
print(best_performance(matrices))
