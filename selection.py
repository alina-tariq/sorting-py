# Alina Tariq
# 500989574
# Section 7

def selectionsort(unsorted):
    # goes through each index to find the corresponding highest number
    for a in range(len(unsorted)):
        min_pos = a # tracks index of highest element
        # finds biggest element from all elements to the right of current index
        for b in range(a+1, len(unsorted)):
            if unsorted[min_pos] > unsorted[b]:
                min_pos = b
        # swaps element at current index if a higher element exists
        if min_pos != a:
            unsorted[a], unsorted[min_pos] = unsorted[min_pos], unsorted[a]
        print(a+1, ": ", unsorted)
    return unsorted

# unsorted lists
#unsort1 = [86, 0, 66, 31, 90, 78, 54, 72, 91, 27, 69, 6, 41, 3, 96, 99, 94, 68, 56, 12]
unsort1 = [29, 72, 98, 13, 87, 66, 52, 51, 36]
#unsort2 = ['A', 'c', 'G', 'K', 'l', 'x', 'e', 'D', 'X', 'B', 'q', 'P', 'r', 'F', 'g', 's']

# prints unsorted list
print('Unsorted List 1: ', unsort1)
#print('Unsorted List 2: ', unsort2)
print(' ')

# selection sorts
s_sort1 = selectionsort(unsort1)
#s_sort2 = selectionsort(unsort2)

# prints results
print('Selection Sorted List 1: ', s_sort1)
#print('Selection Sorted List 2: ', s_sort2)