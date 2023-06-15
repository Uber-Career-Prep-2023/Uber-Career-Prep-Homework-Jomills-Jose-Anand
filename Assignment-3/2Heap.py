# Question 2: Min Heap

# * Time taken: ~1 hour

#? Class to represent a heap
class Heap:

    # Initialization function
    def __init__(self, array):
        self.heap = []
        self.size = 0

        # Fix the heap
        for i in range(len(array)):
            self.insert(array[i])
            self.fixHeap(i)
        
    # Function to fix the heap
    def fixHeap(self, index):
        parent = index // 2
        while (self.heap[index] < self.heap[parent]):
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = index // 2

    # Function to fix the heap downwards
    def fixDown(self):
        index = 0
        left = 2 * index + 1
        right = 2 * index + 2
        leftFlag = rightFlag = None
        if (left < self.size):
            leftFlag = True
        if (right < self.size):
            rightFlag = True
        while (leftFlag or rightFlag):
            if (self.heap[index] > self.heap[left] or self.heap[index] > self.heap[right]):
                if (self.heap[left] < self.heap[right]):
                    self.heap[index], self.heap[left] = self.heap[left], self.heap[index]
                    index = left
                else:
                    self.heap[index], self.heap[right] = self.heap[right], self.heap[index]
                    index = right
                left = 2 * index + 1
                right = 2 * index + 2
                leftFlag = rightFlag = None
                if (left < self.size):
                    leftFlag = True
                if (right < self.size):
                    rightFlag = True
            else:
                break

    # Function to print the heap
    def printHeap(self):
        print(self.heap)

    # Function to return the minimum element
    def top(self):
        return self.heap[0]
    
    # Function to insert an element
    def insert(self, element):
        self.heap.append(element)
        self.size += 1
        self.fixHeap(self.size - 1)
    
    # Function to delete an element
    def remove(self):
        self.heap[0], self.heap[self.size - 1] = self.heap[self.size - 1], self.heap[0]
        self.heap.pop()
        self.size -= 1
        self.fixDown()


# ? Tests

newHeap = Heap([1, 2, 3, 4, 5, 6, 7, 8, 9])
newHeap.printHeap()
print(newHeap.top())
newHeap.insert(0)
newHeap.printHeap()
print(newHeap.top())
newHeap.remove()
newHeap.printHeap()
print(newHeap.top())
newHeap.remove()
newHeap.printHeap()
print(newHeap.top())
newHeap.remove()
newHeap.printHeap()
print(newHeap.top())