# Question 4: BackspaceStringCompare

# * Approach followed: Strings increment
# * Time complexity: O(n)
# * Space complexity: O(1)

# * Input: input strings
# * Output: boolean of whether the given strings are equal after backspace


# ? Function to produce the final string after backspace
def backspace_string_process(input_string):

    # Initialize backspace index
    backspace_index = 0

    # Iterate through the string
    for i in range(len(input_string)):

        # Check if backspace index is greater than 0
        if backspace_index < 0:
            backspace_index = 0

        # Check if the current character is backspace
        if input_string[i] == "#":
            backspace_index -= 1

        # Otherwise we keep the string up until the index, the ith character, and the rest of the string
        else:
            input_string = (
                input_string[:backspace_index]
                + input_string[i]
                + input_string[backspace_index + 1 :]
            )
            backspace_index += 1

    # Return the final string
    return input_string[:backspace_index]


# ? Function to check if the given strings are equal after backspace
def backspace_string_compare(string_1, string_2):

    # Return the boolean of whether the final strings are equal
    return backspace_string_process(string_1) == backspace_string_process(string_2)


# ? Test cases

# * Test case 1
print(backspace_string_compare("abcde", "abcde"))  # Output: True

# * Test case 2
print(
    backspace_string_compare("Uber Career Prep", "u#Uber Careee#r Prep")
)  # Output: True

# * Test case 3
print(backspace_string_compare("abcdef###xyz", "abcw#xyz"))  # Output: True

# * Test case 4
print(backspace_string_compare("abcdef###xyz", "abcdefxyz###"))  # Output: False

# * Test case 5
print(backspace_string_compare("", "u#"))  # Output: True

# * Test case 6
print(backspace_string_compare("abcxyz###def", "abcdefxyz###"))  # Output: True

# * Test case 7
print(backspace_string_compare("Great#####", "###"))  # Output: False

# * Test case 8
print(backspace_string_compare("##Okay", "Okay"))  # Output: True
