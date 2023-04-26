# Question 5: IsBST

# * Approach followed: depth first - pre order
# * Time complexity: O(n)
# * Space complexity: O(1)

# * Input: input BST
# * Output: boolean

# * Time taken: 7 minutes

# ! Node class defintion
class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ? Function to check if a tree is a BST
def isBST(root):

    if not root:
        return True

    leftCheck = True if not root.left else True if root.val > root.left.val else False
    rightCheck = (
        True if not root.right else True if root.val < root.right.val else False
    )

    return leftCheck and rightCheck and isBST(root.left) and isBST(root.right)


# ? Test cases

tree = Node()
print(isBST(tree))

tree = Node()
tree.val = 10
tree.left = Node(val=5)
tree.right = Node(val=12)
print(isBST(tree))

tree = Node()
tree.val = 10
tree.left = Node(val=12)
tree.right = Node(val=5)
print(isBST(tree))
