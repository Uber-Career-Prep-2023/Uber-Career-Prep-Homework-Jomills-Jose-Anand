# Question 3: ZeroSumSubArrays

# * Approach followed: Hash the elements
# * Time complexity: O(n)
# * Space complexity: O(n)

# * Input: input array
# * Output: number of subarrays with sum 0

# * Assumptions: we consider repeated subarrays as well

# ? Function to get the number of subarrays with sum 0
def zero_sum_subarrays(input_array):
    # Initialize hash table
    hash_table = {0: 1}

    # Initialize sum and count
    sum = 0
    count = 0

    # Loop through the array
    for i in range(len(input_array)):
        # Add the element to the sum
        sum += input_array[i]

        # If the sum is in the hash table, increment count by the value
        if sum in hash_table:
            count += hash_table[sum]
            hash_table[sum] += 1

        # If the sum is not in the hash table, add it with value 1
        else:
            hash_table[sum] = 1

    # Return the count
    return count


# ? Test cases

# * Test case 1
print(zero_sum_subarrays([4, 5, 2, -1, -3, -3, 4, 6, -7]))  # Output: 2

# * Test case 2
print(zero_sum_subarrays([1, 8, 7, 3, 11, 9]))  # Output: 0

# * Test case 3
print(zero_sum_subarrays([8, -5, 0, -2, 3, -4]))  # Output: 2

# * Test case 4
print(zero_sum_subarrays([1, 2, 3, 4, 5, 6]))  # Output: 0

# * Test case 5
print(zero_sum_subarrays([0, 0, 0, 0, 0, 0]))  # Output: 21

# * Test case 6
print(zero_sum_subarrays([-1, 1, -1, 1, -1, 1]))  # Output: 9

# * Test case 7
print(zero_sum_subarrays([-1, 1, -1, 1, -1, 1, 0]))  # Output: 13

# * Test case 8
print(zero_sum_subarrays([]))  # Output: 0
