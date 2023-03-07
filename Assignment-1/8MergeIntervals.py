# Question 8: Merge Intervals

# * Approach followed: hash the elements
# * Time complexity: O(n)
# * Space complexity: O(n)

# * Input: array of integer pairs
# * Output: array of integer pairs

# * Time taken: 37 minutes

# ? Function to return the merged intervals of a list of integer pairs
def merge_intervals(input_array):

    # We make a hashmap of the starting elements elements
    starting_map = {}

    # We find the last starting element
    last_start = None

    # We sort the input array
    input_array.sort()

    # We iterate through the input array
    for i in input_array:

        # If there's no element, we populate it
        if not last_start:
            starting_map[i[0]] = i[1]
            last_start = i[0]

        # We check if the current element is outside the interval
        if starting_map[last_start] < i[0]:
            starting_map[i[0]] = i[1]
            last_start = i[0]

        # Otherwise we check the later occurring element
        else:
            starting_map[last_start] = max(starting_map[last_start], i[1])

    # Initialize final array of merged intervals
    final_array = []

    # Populate the array
    for i in starting_map:
        final_array.append((i, starting_map[i]))

    # Return final array
    return final_array


# ? Test cases

# * Test case 1
print(
    merge_intervals([(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)])
)  # Output: [(4, 8), (1, 3), (9, 12)]

# * Test case 2
print(merge_intervals([(5, 8), (6, 10), (2, 4), (3, 6)]))  # Output: [(2, 10)]

# * Test case 3
print(
    merge_intervals([(10, 12), (5, 6), (7, 9), (1, 3)])
)  # Output: [(10, 12), (5, 6), (7, 9), (1, 3)]
