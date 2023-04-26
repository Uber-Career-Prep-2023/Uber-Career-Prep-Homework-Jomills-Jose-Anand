# Question 4: Copy Tree

# * Approach followed: depth first - pre order
# * Time complexity: O(n)
# * Space complexity: O(n)

# * Input: input BST
# * Output: output BST

# * Time taken: 12 minutes

# ! Node class defintion
class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ? Function to create a deep copy of a BST
def copyTree(root):

    # base case
    if not root:
        return root

    # create new node
    newNode = Node(val=root.val)

    # Define left and right nodes
    newNode.left = copyTree(root.left)
    newNode.right = copyTree(root.right)

    # Return nodes
    return newNode


# ? Test cases

tree = Node()
firstTree = copyTree(tree)
del tree
print(firstTree.val)
print(firstTree.left)
print(firstTree.right)

tree = Node()
tree.val = 10
tree.left = Node(val=5)
tree.right = Node(val=12)
newTree = copyTree(tree)
del tree
print(newTree.val)
print(newTree.left.val)
print(newTree.right.val)
