# Question 7: Reverse Words

# * Approach followed: Using a stack to store the words and then reversing them
# * Time complexity: O(n)
# * Space complexity: O(n)

# * Input: string
# * Output: string

# * Time taken: 6 minutes


# ? Function to reverse words in a string
def ReverseWords(inputString):

    #  Split the string into words
    words = []
    temp_word = ""

    for i in range(len(inputString)):
        if inputString[i] == " ":
            words.append(temp_word)
            temp_word = ""
        else:
            temp_word += inputString[i]
    words.append(temp_word)

    #  Reverse the words
    final_string = words[-1]
    for i in range(len(words)-2, -1, -1):
        final_string += " " + words[i]
    
    return final_string


# ? Test cases

# Test case 1
print(ReverseWords("Hello World!"))

# Test case 2
print(ReverseWords("The quick brown fox jumps over the lazy dog."))

# Test case 3
print(ReverseWords("Uber Career Prep"))

# Test case 4
print(ReverseWords("Hello"))

# Test case 5
print(ReverseWords(""))

# Test case 6
print(ReverseWords("Emma lives in Brooklyn, New York."))

# Test case 7
print(ReverseWords(" "))