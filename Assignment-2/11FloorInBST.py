# Question 11: Floor In BST

# * Approach followed: breadth first search
# * Time complexity: O(n)
# * Space complexity: O(1)

# * Input: input binary tree, integer
# * Output: integer

# * Time taken: 14 minutes

# ! Node class defintion
class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ? Function to get the floor of an integer in a BST
def floorInBST(root, val):

    # We keep going to the larger side in the BST
    # until we hit the given value

    iterator = root

    while iterator and iterator.right:
        if val < iterator.val:
            iterator = iterator.left
        elif val > iterator.val and val >= iterator.right.val:
            iterator = iterator.right
        else:
            break

    # We check if the val is the floor
    if not iterator:
        return None
    if val < iterator.val:
        return None

    # If it is, return the floor
    return iterator.val


# ? Test cases
tree = Node(val=1)
print(floorInBST(tree, 2))

tree = Node(val=3)
tree_left = Node(val=2)
tree_right = Node(val=5)
tree.left = tree_left
tree.right = tree_right
print(floorInBST(tree, 6))

tree = Node(val=3)
tree_left = Node(val=0)
tree_right = Node(val=5)
tree.left = tree_left
tree.right = tree_right
print(floorInBST(tree, 1))
