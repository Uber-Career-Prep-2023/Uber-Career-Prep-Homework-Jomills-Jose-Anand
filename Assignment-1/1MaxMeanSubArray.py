# Question 1: Maximum Mean Subarray

# * Approach followed: fixed-size sliding window
# * Time complexity: O(n)
# * Space complexity: O(1)

# * Input: array of integers, size of subarray
# * Output: maximum mean subarray

# ? Function to find maximum mean subarray
def max_mean_sub_array(integer_array, k):
    # Checking base cases
    if (len(integer_array) == 0) or (k == 0) or (k > len(integer_array)):
        return None

    # Variable to store maximum sum
    maximum_sum = 0
    # Variable to store current sum
    current_sum = 0

    # Initialising current sum
    for i in range(k):
        current_sum += integer_array[i]

    # Setting maximum sum to current sum
    maximum_sum = current_sum

    # Looping through the rest of the array
    for i in range(k, len(integer_array)):
        # Updating current sum
        current_sum += integer_array[i] - integer_array[i - k]
        # Updating maximum sum
        if current_sum > maximum_sum:
            maximum_sum = current_sum

    # Returning maximum mean
    return float(maximum_sum) / k


# ? Test cases

# * Test case 1
print(max_mean_sub_array([4, 5, -3, 2, 6, 1], 2))  # 4.5

# * Test case 2
print(max_mean_sub_array([4, 5, -3, 2, 6, 1], 3))  # 3.0

# * Test case 3
print(max_mean_sub_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0))  # None

# * Test case 4
print(max_mean_sub_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11))  # None

# * Test case 5
print(max_mean_sub_array([], 4))  # None

# * Test case 6
print(max_mean_sub_array([1, 1, 1, 1, -1, -1, 2, -1, -1], 3))  # 1.0

# * Test case 7
print(max_mean_sub_array([1, 1, 1, 1, -1, -1, 2, -1, -1, 6], 5))  # 1.0

# * Test case 8
print(max_mean_sub_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))  # 8.0
