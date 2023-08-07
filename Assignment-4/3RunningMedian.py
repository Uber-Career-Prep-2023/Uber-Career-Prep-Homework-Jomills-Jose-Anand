# Question 3: Running Median

from heapq import heappush, heappop

# * Approach followed: Min-max heap
# * Time complexity: O(log n)
# * Space complexity: O(n)

# * Input: input stream of integers
# * Output: median of the input stream

# * Time taken: 23 minutes

# ? Class to represent a min-max heap
class MinMaxHeap:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
    
    # Function to insert a new element into the min-max heap
    def insert(self, element):
        heappush(self.max_heap, -element)
        heappush(self.min_heap, -heappop(self.max_heap))

        if len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    # Function to return median of given input stream
    def running_median(self):
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2.0
        else:
            return -self.max_heap[0]


# ? Function to return median of given input stream
def running_median():
    min_max_heap = MinMaxHeap()
    while True:
        try:
            element = int(input())
            min_max_heap.insert(element)
            print(min_max_heap.running_median())
        except EOFError:
            break


# ? Test cases

# Test case 1
running_median()
"""
1 
>>> 1.0
2
>>> 1.5
3
>>> 2.0
11
>>> 2.5
"""