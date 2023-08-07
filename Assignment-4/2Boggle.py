# Question 2: Boggle

# * Approach followed: trie + dfs
# * Time complexity: 
# * Space complexity: 

# * Input: board, dictionary
# * Output: all possible words that can be made from the given set of characters

# * Time taken: 45+ minutes

#? Class to represent a trie
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['$'] = True

    def isValidWord(self, word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return '$' in node


# ? Function to return all possible words that can be made from the given set of characters
def boggle(board, dictionary):
    
    # ? Function to perform dfs
    def dfs(x, y, stem, wordStem):

        # Check the letter in the current position
        letter = board[x][y].lower()

        # Check if the letter is present in the trie
        if letter not in stem:
            return

        # Get node
        node = stem[letter]

        # Check if the node is a valid word
        if '$' in node:
            returnArray.append(wordStem + letter)

        # Mark the letter as visited
        board[x][y] = '#'

        # Iterate over the neighbours
        if (x > 0 and board[x-1][y] != '#'):
            dfs(x-1, y, node, wordStem + letter)
        if (x < len(board)-1 and board[x+1][y] != '#'):
            dfs(x+1, y, node, wordStem + letter)
        if (y > 0 and board[x][y-1] != '#'):
            dfs(x, y-1, node, wordStem + letter)
        if (y < len(board[0])-1 and board[x][y+1] != '#'):
            dfs(x, y+1, node, wordStem + letter)

        # Unmark the letter
        board[x][y] = letter

        # If current node is a leaf node, return
        if not node:
            trie.pop(letter)

    
    # Build the trie
    trie = Trie()
    for word in dictionary:
        trie.insert(word.lower())

    # Array to store the words
    returnArray = []

    # Iterate over the board
    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs(i, j, trie.root, "")

    # Return the array
    return returnArray


# ? Test cases

# Test case 1
dictionary = [
"Ace",
"Ape",
"Cape",
"Clap",
"Clay",
"Gape",
"Grape",
"Lace",
"Lap",
"Lay",
"Mace",
"Map",
"May",
"Pace",
"Pay",
"Rap",
"Ray",
"Tap",
"Tape",
"Trace",
"Trap",
"Tay",
"Yap",
]

board = [
    ['A', 'D', 'E'],
    ['R', 'C', 'P'],
    ['L', 'A', 'Y'],
]

print(boggle(board, dictionary))

# Expected Output:

"""
Ace
Race
Pace
Lace
Pay
Lay
Clay
Ray
Lap
Rap
Clap
Ape
Cape
Yap
"""