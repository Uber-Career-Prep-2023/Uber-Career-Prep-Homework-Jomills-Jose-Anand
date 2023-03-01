# Question 6: Missing Integer

# * Approach followed: ?
# * Time complexity: O(n)
# * Space complexity: O(1)

# * Input: input array and number n
# * Output: missing integer in the array


# ? Function to find the missing integer in an array of integers from 1 to n
def missing_integer(input_array, n):

    # Iterator variable
    iterator = 0

    # Iterating through input array
    for i in input_array:

        # We increment the iterator
        iterator += 1

        # Check if it matches the sorted element in the array
        if not (iterator == i):
            return iterator

    # If no element matches, we return None or n
    if input_array[-1] != n:
        return n

    return None


# ? Test cases

# * Test case 1
print(missing_integer([1, 2, 3, 4, 6, 7], 7))  # Output: 5

# * Test case 2
print(missing_integer([1], 2))  # Output: 2

# * Test case 3
print(missing_integer([1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12], 12))  # Output: 9
