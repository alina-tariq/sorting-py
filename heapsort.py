def heapify(arr, max_i, i):
    largest = i # parent node
    l_child = i * 2 + 1 # left child
    r_child = i * 2 + 2 # right child

    # checks if left child is greater than parent node
    if l_child < max_i and arr[i] < arr[l_child]:
        largest = l_child # sets it as the largest if true

    # checks if right child is greater than the largest node (parent or left child)
    if r_child < max_i and arr[largest] < arr[r_child]:
        largest = r_child # sets it as largest is true

    if largest != i:
        # swaps largest and parent node if parent isn't largest
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, max_i, largest) # heapifies largest element

def heapsort(arr):
    max_i = len(arr)

    # creates a max heap
    for i in range(max_i//2, -1, -1):
        heapify(arr, max_i, i)

    for j in range(max_i-1, 0, -1):
        # swaps first and last node
        arr[0], arr[j] = arr[j], arr[0]
        # builds max heap with all elements except last
        heapify(arr, j, 0)

str = input("Please enter string to be sorted: ")
arr = []
for ch in str:
    arr.append(ch)

print("Original array: ", arr)
heapsort(arr)
print("Sorted array: ", arr)
