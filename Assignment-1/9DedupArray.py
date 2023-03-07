# Question 9: Dedup Array

# * Approach followed: hashing the elements
# * Time complexity: O(n)
# * Space complexity: O(n)

# * Input: input array
# * Output: modified array

# * Time taken: 16 minutes

# ? Function to remove duplicates in the array
def dedup_array(input_array):

    # Make a hashmap of elements
    element_map = {}

    # Iterate over the input array
    for i in range(len(input_array)):
        element_map[input_array[i]] = True

    # Initialize final array
    final_array = []

    # Fill the final array
    for i in element_map:
        final_array.append(i)

    # Return final array
    return final_array


# ? Test cases

# * Test case 1
print(dedup_array([1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4]))  # Output: [1, 2, 3, 4]

# * Test case 2
print(
    dedup_array([0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15])
)  # Output: [0, 1, 4, 5, 8, 9, 10, 11, 15]

# * Test case 3
print(dedup_array([1, 3, 4, 8, 10, 12]))  # Output: [1, 3, 4, 8, 10, 12]

# # * Test case 4
print(dedup_array([]))  # Output: []

# # * Test case 5
print(dedup_array([1]))  # Output: [1]
