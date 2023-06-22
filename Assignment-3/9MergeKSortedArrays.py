# Question 9: Merge K Sorted Arrays

# * Approach followed: min-heap
# * Time complexity: O(nlogn) where n is the total number of elements in all the arrays
# * Space complexity: O(n) where n is the total number of elements in all the arrays

# * Input: int, array of arrays
# * Output: array

# * Time taken: 11 minutes

import heapq

# ? Function to merge k sorted arrays
def mergeKSortedArrays(k, inputArray):

    # Build a min-heap
    heap = []
    
    # Output array
    outputArray = []

    # Insert the all the elements of inputArray into the heap
    for i in range(k):
        for j in range(len(inputArray[i])):
            heapq.heappush(heap, inputArray[i][j])

    # Remove the minimum element from the heap and append it to the output array
    while (len(heap) > 0):
        outputArray.append(heapq.heappop(heap))

    # Return the output array
    return outputArray


# ? Test cases

# Test case 1
print(mergeKSortedArrays(2, [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]))

# Test case 2
print(mergeKSortedArrays(3, [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]))