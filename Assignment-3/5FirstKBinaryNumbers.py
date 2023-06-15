# Question 5: First K Binary Numbers

# * Approach followed: Using a queue
# * Time complexity: O(n)
# * Space complexity: O(n)

# * Input: integer
# * Output: array of first k binary numbers

# * Time taken: 10 minutes


# ? Function to find the first k binary numbers
def firstKBinaryNumbers(k):

    # Base check
    if k == 0:
        return []
    
    # Initialize the queue
    queue = []

    # Initialize the array of first k binary numbers
    firstKBinaryNumbers = ["0"]

    # Append 1 to the queue
    queue.append("1")

    # Traverse through the queue
    for i in range(k - 1):
        
        # Append the first element of the queue to the array of first k binary numbers
        top = queue.pop(0)
        firstKBinaryNumbers.append(top)

        queue.append(top + "0")
        queue.append(top + "1")

    # Return the array of first k binary numbers
    return firstKBinaryNumbers


# ? Test cases

# Test case 1
print(firstKBinaryNumbers(5))  # Output: ['0', '1', '10', '11', '100']

# Test case 2
print(firstKBinaryNumbers(10))  # Output: ['0', '1', '10', '11', '100', '101', '110', '111', '1000', '1001']

# Test case 3
print(firstKBinaryNumbers(0))  # Output: []

# Test case 4
print(firstKBinaryNumbers(1))  # Output: ['0']