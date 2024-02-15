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
    # TODO: Define Loop through each matrix to calculate metrics
    for index, matrix in enumerate(matrices):
        # TODO: Define tp, fp fn and tn
        tp, fp, fn, tn = [i.split(",") for i in matrix]

        # print(f"Index:{index}, Matrix:{matrix}")
        # TODO: Calculate accuracy and precision

        # TODO: Update best metrics if found

    return best_index, best_accuracy, best_precision


# Print the results
best_performance(matrices)

"""Sample data:
4
70,15,8,78
60,20,10,80
45,5,3,92
80,7,15,98

Return:
Index: 1
Accuracy: 1.0
Precision: 1.0
"""
