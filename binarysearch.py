# Binary Search
# Searches for a key in a sorted list of integers
# Worst-case Time Complexity: O(log n)
# seq is the sorted list
# key is the integer to search for
# if key is found, the index will be returned
# if key is not found, False is returned

def binarySearch(seq, key):

    lo = 0
    hi = len(seq) - 1

    while hi >= lo:
        mid = lo + (hi - lo) // 2
        if seq[mid] < key:
            lo = mid + 1
        elif seq[mid] > key:
            hi = mid - 1
        else:
            return mid
    return False

# Test case 1
numbers = [1,2,3,4,5]
print(binarySearch(numbers, 2)) # returns index 1

# Test case 2
numbers = [1,2,3,4,5]
print(binarySearch(numbers, 6)) # returns False
