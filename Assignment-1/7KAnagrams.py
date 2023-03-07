# Question 7: K Anagrams

# * Approach followed: hash the elements
# * Time complexity: O(n)
# * Space complexity: O(n)

# * Input: input strings and k value (integer)
# * Output: boolean

# * Time taken: 23 minutes

# ? Function to find if two strings are k-anagrams
def k_anagram(array_1, array_2, k):

    # Base cases
    if len(array_1) != len(array_2):
        return False

    # Make two hashmaps for each array
    array_1_map = {}
    array_2_map = {}

    # Iterate through the arrays and populate the array
    for i in array_1:
        if i in array_1_map:
            array_1_map[i] += 1
        else:
            array_1_map[i] = 1
    for i in array_2:
        if i in array_2_map:
            array_2_map[i] += 1
        else:
            array_2_map[i] = 1

    # We add the extra characters of array 2 to array 1 with a 0 count
    for i in array_2_map:
        if i not in array_1_map:
            array_1_map[i] = 0

    # Find the amount of letters that have to be changed for anagram words
    count = 0

    for i in array_1_map:
        if i in array_2_map:
            count += abs(array_2_map[i] - array_1_map[i])
        else:
            count += array_1_map[i]

    # Since only half the letters need to be changed we get half of count
    if count % 2 == 0:
        count = count / 2
    else:
        count = (count // 2) + 1

    # We return a boolean of whether the strings are k-anagrams or not
    return count <= k


# ? Test cases

# * Test case 1
print(k_anagram("apple", "peach", 1))  # Output: False

# * Test case 2
print(k_anagram("apple", "peach", 2))  # Output: True

# * Test case 3
print(k_anagram("cat", "dog", 3))  # Output: True

# * Test case 4
print(k_anagram("debit curd", "bad credit", 1))  # Output: True

# * Test case 5
print(k_anagram("baseball", "basketball", 2))  # Output: False

# * Test case 6
print(k_anagram("", "", 1))  # Output: True

# * Test case 7
print(k_anagram("mars", "arms", 2))  # Output: True

# * Test case 8
print(k_anagram("green", "cream", 1))  # Output: False
