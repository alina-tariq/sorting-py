def radixHelper(matrix, a):
    size = len(matrix)
    matsort = [[0] * 10] * size
    count = [0] * 10

    for i in range(size):
        count[int(matrix[i][a])] += 1

    for i in range(1, 10):
        count[i] += count[i-1]

    i = size - 1
    while i >= 0:
        matsort[count[int(matrix[i][a])] - 1] = matrix[i]
        count[int(matrix[i][a])] -= 1
        i -= 1

    for i in range(size):
        matrix[i] = matsort[i]

def radixSort(matrix):
    for a in range(9, -1, -1):
        radixHelper(matrix, a)

num = input("Please enter number of vectors: ")
matrix = []

for a in range(int(num)):
    vector = input("Vector %i: " %(a+1))
    matrix.append(vector.split())

radixSort(matrix)

for a in range(int(num)):
    print(matrix[a])
