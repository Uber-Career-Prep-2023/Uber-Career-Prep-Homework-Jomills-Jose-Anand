# Question 6: Word Break

# * Approach followed: dynamic programming
# * Time complexity: O(n)
# * Space complexity: O(n)

# * Input: string and a dictionary of words
# * Output: boolean value indicating if string can be broken into words present in dictionary

# * Time taken: 23 minutes


# ? Function to determine if a string can be broken into words present in a dictionary
def wordBreak(s, wordDict):

    # Lowercase the string
    s = s.lower()
    
    # Define a dp array to store if a substring can be broken into words present in dictionary
    dp = [False] * len(s)

    # Iterate over the string
    for chr in range(len(s)):
        # Check if a word can be formed from the substring
        for word in wordDict:

            # Lowercase the word
            word = word.lower()

            # Get length of the word
            len_word = len(word)

            # If the word is present in the dictionary
            if word == s[chr-len_word+1:chr+1] and (dp[chr-len_word] or chr-len_word == -1):
                dp[chr] = True

    # Return if the string can be broken into words present in dictionary
    return dp[-1]



# ? Test cases

# Define dictionary of words
wordDict = [
"Elf",
"Go",
"Golf",
"Man",
"Manatee",
"Not",
"Note",
"Pig",
"Quip",
"Tee",
"Teen",
]

# Test case 1
print(wordBreak("mangolf", wordDict))
# Expected answer: True

# Test case 2
print(wordBreak("manateenotelf", wordDict))
# Expected answer: True

# Test case 3
print(wordBreak("manateenotelfgolf", wordDict))
# Expected answer: True

# Test case 4
print(wordBreak("quipig", wordDict))
# Expected answer: False

# Test case 5
print(wordBreak("teenot", wordDict))
# Expected answer: True

# Test case 6
print(wordBreak("teenote", wordDict))
# Expected answer: True

# Test case 7
print(wordBreak("teennot", wordDict))
# Expected answer: True

# Test case 8
print(wordBreak("teenotee", wordDict))
# Expected answer: False