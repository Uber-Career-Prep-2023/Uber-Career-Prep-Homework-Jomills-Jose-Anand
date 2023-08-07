# Question 1: Building a Trie

# * Time taken: ~1 hour

#? Class to represent a trie node
class TrieNode:

    # Constructor
    def __init__(self):
        self.children = {}
        self.validWord = False


#? Class to represent a trie
class Trie:

    # Constructor
    def __init__(self):
        self.root = TrieNode()
    

    # Function to insert a word into the trie
    def insert(self, word):

        # Iterator node
        node = self.root

        # Iterate over the word
        for char in word:
            
            # Check if the character is present in the trie
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        # Mark the last node as a valid word
        node.validWord = True


    # Function to check if a word is present in the trie
    def isValidWord(self, word):

        # Iterator node
        node = self.root

        # Iterate over the word
        for char in word:

            # Check if the character is present in the trie
            if char not in node.children:
                return False
            node = node.children[char]

        # Check if the last node is a valid word
        return node.validWord


    # Function to remove a word from the trie
    def remove(self, word):

        # Base check
        if not self.root:
            return

        # Iterator node
        node = self.root

        # Node array to store the nodes
        nodes = []

        # Iterate over the word
        for char in word:

            # Check if the character is present in the trie
            if char not in node.children:
                return
            
            # Append the node to the array
            nodes.append(node)
            node = node.children[char]

        # Check if the last node is a valid word
        if node.validWord:
            node.validWord = False

        # Check if the last node has children
        if node.children:
            return

        # Iterate over the nodes
        for i in range(len(nodes)-1, -1, -1):

            # If the node is not a valid word and has only one child, delete it
            if not nodes[i].validWord and len(nodes[i].children) == 1:
                nodes[i].children = {}
                continue
            else:
                break
    

# ? Tests

# Test 1
trie = Trie()
trie.insert("apple")
print(trie.isValidWord("apple")) # True
print(trie.isValidWord("app")) # False
print(trie.isValidWord("ap")) # False
trie.remove("apple")
print(trie.isValidWord("apple")) # False

# Test 2
trie = Trie()
trie.insert("cartoon")
trie.insert("car")
trie.insert("carpet")
trie.insert("carpenter")
print(trie.isValidWord("car")) # True   
trie.remove("car")
print(trie.isValidWord("car")) # False
print(trie.isValidWord("cartoon")) # True
print(trie.isValidWord("carpet")) # True
print(trie.isValidWord("carpenter")) # True
trie.remove("carpenter")
print(trie.isValidWord("carpenter")) # False
