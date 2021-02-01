def bubblesort(unsorted):
    # goes through entire array
    for a in range(len(unsorted)):
        # compares each unsorted element to the element before it
        for b in range(1, len(unsorted)-a):
            # swaps if previous element is smaller
            if unsorted[b-1] > unsorted[b]:
                unsorted[b], unsorted[b-1] = unsorted[b-1], unsorted[b]
        print(a+1, ": ", unsorted)
    return unsorted

# unsorted lists
unsort1 = [86, 0, 66, 31, 90, 78, 54, 72, 91, 27, 69, 6, 41, 3, 96, 99, 94, 68, 56, 12]
unsort2 = ['A', 'c', 'G', 'K', 'l', 'x', 'e', 'D', 'X', 'B', 'q', 'P', 'r', 'F', 'g', 's']
unsort1 = [5, 3, 9, 5]

# prints unsorted lists
print('Unsorted List 1: ', unsort1)
print('Unsorted List 2: ', unsort2)
print(' ')

# bubble sorts
b_sort1 = bubblesort(unsort1)
b_sort2 = bubblesort(unsort2)

# prints results
print('Bubble Sorted List 1: ', b_sort1)
print('Bubble Sorted List 2: ', b_sort2)
