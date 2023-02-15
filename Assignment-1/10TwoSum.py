# Question 10: TwoSum

# * Approach followed: Hash the elements
# * Time complexity: O(n)
# * Space complexity: O(n)

# * Input: input array, target
# * Output: count of pairs with sum equal to target

# ? Function to get the count of pairs with sum equal to target
def two_sum(input_array, target):

    # Initialize hash table
    hash_table = {}

    # Initialize count
    count = 0

    # Loop through the array
    for i in range(len(input_array)):
        # If target - element is in the hash table, increment count
        if target - input_array[i] in hash_table:
            if input_array[i] in hash_table:
                hash_table[input_array[i]] += 1
            else:
                hash_table[input_array[i]] = 1

            # Increment count by the value of the element in the hash table
            count += hash_table[target - input_array[i]]
            hash_table[target - input_array[i]] += 1

        # Otherwise we add it to the hash table
        else:
            if input_array[i] in hash_table:
                hash_table[input_array[i]] += 1
            else:
                hash_table[input_array[i]] = 1

    # Return the count
    return count


# ? Test cases

# * Test case 1
print(two_sum([1, 2, 3, 4, 5, 6], 7))  # Output: 3

# * Test case 2
print(two_sum([1, 2, 3, 4, 5, 6], 8))  # Output: 2

# * Test case 3
print(two_sum([1, 2, 3, 4, 5, 6], 9))  # Output: 2

# * Test case 4
print(two_sum([1, 2, 3, 4, 5, 6], 10))  # Output: 1

# * Test case 5
print(two_sum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1], 10))  # Output: 4

# * Test case 6
print(two_sum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1], 8))  # Output: 3

# * Test case 7
print(two_sum([4, 3, 3, 5, 7, 0, 2, 3, 8, 6], 5))  # Output: 4

# * Test case 8
print(two_sum([4, 3, 3, 5, 7, 0, 2, 3, 8, 6], 1))  # Output: 0
