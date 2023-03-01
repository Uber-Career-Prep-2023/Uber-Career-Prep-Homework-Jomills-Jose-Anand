# Question 5: Shortest Substring

# * Approach followed: Variable length size sliding window and hash the elements
# * Time complexity: O(x), O(n) < O(x) < O(n^2)
# * Space complexity: O(m + n)

# * Input: input string and substring
# * Output: first index of shortest substring that matches input substring/characters


# ? Function to produce the final string after backspace
def shortest_substring(input_string, substring):

    # Variable to hold shortest length
    shortest_length = len(input_string)

    # Hashmap of input substring characters:
    character_map = {}

    # Populating character map
    for i in substring:
        character_map[i] = 0
    for i in substring:
        character_map[i] += 1

    # Hashmap of traversal
    traversal_map = {}

    # Initializing pointers
    left_pointer = 0
    right_pointer = 0

    # Update condition
    update_map = True

    # Iterate through the input string
    while right_pointer < len(input_string):

        # Update traversal map
        if update_map:
            if input_string[right_pointer] in traversal_map:
                traversal_map[input_string[right_pointer]] += 1
            else:
                traversal_map[input_string[right_pointer]] = 1

        # Variable check
        condition_met = True

        # Check if the substring contains the input substring
        for j in character_map:
            if j in traversal_map:
                if character_map[j] > traversal_map[j]:
                    condition_met = False
                    break
            else:
                condition_met = False
                break

        # Update shortest length
        if condition_met:
            if shortest_length > (right_pointer - left_pointer):
                shortest_length = right_pointer - left_pointer + 1
        else:
            # Update right pointer
            update_map = True
            right_pointer += 1
            continue

        # Shorten substring
        update_map = False
        traversal_map[input_string[left_pointer]] -= 1
        left_pointer += 1

    # Return index
    return shortest_length


# ? Test cases

# * Test case 1
print(shortest_substring("abracadabra", "abc"))  # Output: 4

# * Test case 2
print(shortest_substring("zxycbaabcdwxyzzxwdcbxyzabccbazyx", "zzyzx"))  # Output: 10

# * Test case 3
print(shortest_substring("dog", "god"))  # Output: 3
