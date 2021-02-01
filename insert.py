# Alina Tariq
# 500989574
# Section 7

def insertsort(unsorted):
    # performs comparisons for each element except first
    for a in range(1, len(unsorted)):
        pos = a # tracks index to which element can be moved 
        # compares element with all previous ones to determine index to which element should be moved
        for b in range(a-1,-1,-1):
            if unsorted[a] < unsorted[b]:
                pos = b # stores lowest/farthest left index 
        # moves element to an earlier index if such an index exists
        if pos != a:
            unsorted.insert(pos, unsorted[a])
            unsorted.pop(a+1)
        print(a, ": ", unsorted)
    return unsorted

# unsorted lists
unsort1 = [86, 0, 66, 31, 90, 78, 54, 72, 91, 27, 69, 6, 41, 3, 96, 99, 94, 68, 56, 12]
unsort2 = ['A', 'c', 'G', 'K', 'l', 'x', 'e', 'D', 'X', 'B', 'q', 'P', 'r', 'F', 'g', 's']
unsort1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]

# prints unsorted lsits
print('Unsorted List 1: ', unsort1)
#print('Unsorted List 2: ', unsort2)
print(' ')

# insertion sorts
i_sort1 = insertsort(unsort1)
#i_sort2 = insertsort(unsort2)

# prints results 
print('Insert Sorted List 1: ', i_sort1)
#print('Insert Sorted List 2: ', i_sort2)
