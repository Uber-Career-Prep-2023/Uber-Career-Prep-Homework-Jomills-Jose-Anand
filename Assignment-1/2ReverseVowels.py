# Question 2: Reverse Vowels

# * Approach followed: forward/back two pointer approach
# * Time complexity: O(n)
# * Space complexity: O(1)

# * Input: input string
# * Output: string with vowels reversed

# ? Function to reverse vowels in a string
def reverse_vowels(input_string):
    # Checking if input string is empty
    if len(input_string) == 0:
        return None

    # Initializing two pointers
    left_pointer = 0
    right_pointer = len(input_string) - 1

    # Initializing vowels list
    vowels = ["a", "e", "i", "o", "u"]

    # Initializing output string
    output_string = ""
    input_string = list(input_string)

    # Looping through the string
    while left_pointer <= right_pointer:
        # Checking if left pointer is a vowel
        if input_string[left_pointer].lower() in vowels:
            # Checking if right pointer is a vowel
            if input_string[right_pointer].lower() in vowels:
                # Adding right pointer to output string
                input_string[left_pointer], input_string[right_pointer] = (
                    input_string[right_pointer],
                    input_string[left_pointer],
                )

                # Incrementing left pointer
                left_pointer += 1

                # Decrementing right pointer
                right_pointer -= 1
            else:

                # Decrementing right pointer
                right_pointer -= 1
        else:

            # Incrementing left pointer
            left_pointer += 1

    # Converting list to string
    output_string = "".join(input_string)

    return output_string


# ? Test cases

# * Test case 1
input_string = "hello"
print(reverse_vowels(input_string))  # Output: holle

# * Test case 2
input_string = "Uber Career Prep"
print(reverse_vowels(input_string))  # Output: eber Ceraer PrUp

# * Test case 3
input_string = "aA"
print(reverse_vowels(input_string))  # Output: Aa

# * Test case 4
input_string = ""
print(reverse_vowels(input_string))  # Output: None

# * Test case 5
input_string = " "
print(reverse_vowels(input_string))  # Output:

# * Test case 6
input_string = "a"
print(reverse_vowels(input_string))  # Output: a

# * Test case 7
input_string = "flamingo"
print(reverse_vowels(input_string))  # Output: flominga

# * Test case 8
input_string = "xyz"
print(reverse_vowels(input_string))  # Output: xyz
