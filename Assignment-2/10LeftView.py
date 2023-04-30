# Question 10: LeftView

# * Approach followed: breadth first search
# * Time complexity: O(n)
# * Space complexity: O(n)

# * Input: input binary tree
# * Output: integer array

# * Time taken: 21 minutes

# ! Node class defintion
class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ? Function to get an array of the left view of a BT
def leftView(root):

    # Base checks
    if not root:
        return None

    # Define left view array and iterator array
    leftArray = []
    iteratorArray = [root]

    # Perform breadth first search
    while iteratorArray:
        for i in range(len(iteratorArray)):
            curNode = iteratorArray[0]

            # Append leftmost element at the level to array
            if not i:
                leftArray.append(curNode.val)

            # Updating iterator array
            iteratorArray.pop(0)
            if curNode.left:
                iteratorArray.append(curNode.left)
            if curNode.right:
                iteratorArray.append(curNode.right)

    # Return left array
    return leftArray


# ? Test cases
tree = Node()
print(leftView(tree))

tree = Node(val=1)
print(leftView(tree))

tree = Node(val=1)
tree_left = Node(val=3)
tree_right = Node(val=5)
tree.left = tree_left
tree.right = tree_right
print(leftView(tree))
