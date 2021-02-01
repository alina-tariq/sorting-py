def partition(arr, min, max):
    pivot = arr[max] # last element is the pivot
    i = min - 1

    for a in range(min, max):
        # array elements smaller of equal to pivot are kept to the left
        if arr[a] <= pivot:
            # tracks position of the last checked element smaller than pivot
            i += 1
            # moves current element to the right of last element smaller than pivot
            arr[i], arr[a] = arr[a], arr[i]

    # swaps pivot with the element to the right of the last element smaller than pivot
    arr[i+1], arr[max] = arr[max], arr[i+1]

    # returns position of pivot element
    return i + 1

def quicksort(arr, min, max):
    if min < max:
        # finds pivot position after sorting array so that
        # with all elements smaller than pivot are to the left
        # and all elements larger than pivot are to the right
        piv = partition(arr, min, max)
        # sorts elements to the left of the pivot
        quicksort(arr, min, piv - 1)
        # sorts elements to the right of the pivot
        quicksort(arr, piv + 1, max)

str = input("Please enter string to be sorted: ")
arr = []
for ch in str:
    arr.append(ch)

size = len(arr) - 1
print("Original array: ", arr)
quicksort(arr, 0, size)
print("Sorted array: ", arr)
