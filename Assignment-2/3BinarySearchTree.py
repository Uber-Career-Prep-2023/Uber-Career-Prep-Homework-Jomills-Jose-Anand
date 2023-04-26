# Question 3: Binary Search Tree

# * Time taken: all 40 minutes + additional for comments

# ! Node class defintion
class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # ? Function to find the minimum value of BST
    def min(self):

        # * Approach followed: iterate left
        # * Time complexity: O(n)
        # * Space complexity: O(1)

        # * Input: root node
        # * Output: value of left leaf node

        minNode = self.left
        while minNode.left:
            minNode = minNode.left
        minNode = self if not minNode else minNode
        return minNode

    # ? Function to find the maximum value of BST
    def max(self):

        # * Approach followed: iterate right
        # * Time complexity: O(n)
        # * Space complexity: O(1)

        # * Input: root node
        # * Output: value of right leaf node

        maxNode = self.right
        while maxNode.right:
            maxNode = maxNode.right
        maxNode = self if not maxNode else maxNode
        return maxNode

    # ? Check if a value is present in the BST
    def contains(self, val):

        # * Approach followed: recursion
        # * Time complexity: O(n)
        # * Space complexity: O(1)

        # * Input: root node
        # * Output: boolean

        # Helper function
        def find(node, val):

            # Value is not present
            if not node:
                return False

            # Value is present
            if node.val == val:
                return True

            # Value is lesser than the node's value
            if val < node.val:
                return find(node.left, val)
            # Value is greater than the node's value
            else:
                return find(node.right, val)

        return find(self, val)

    # ? Function to insert value into the BST
    def insert(self, val):

        # * Approach followed: recursion
        # * Time complexity: O(n)
        # * Space complexity: O(1)

        # * Input: root node
        # * Output: None

        # Helper function
        def push(node, val):

            # Creating new node
            if not node:
                return Node(val=val, left=None, right=None)

            # Value is lesser than the node's value
            if val < node.val:
                node.left = push(node.left, val)
            # Value is greater than the node's value
            else:
                node.right = push(node.right, val)

            return node

        # Check if BST contains val
        if not self.contains(val):
            push(self, val)

    # ? Function to delete value from the BST
    def delete(self, val):

        # * Approach followed: recursion
        # * Time complexity: O(n)
        # * Space complexity: O(1)

        # * Input: root node
        # * Output: None

        # Helper function
        def remove(node, val):

            # Base case
            if not node:
                return None

            # If we find the element matching val
            if node.val == val:

                # Cases with empty/one leaf node

                if not node.left:
                    modifiedNode = node.right
                    node = None
                    return modifiedNode

                if not node.right:
                    modifiedNode = node.left
                    node = None
                    return modifiedNode

                # Cases with both children

                modifiedNode = node.left.max()
                node.val = modifiedNode.val
                node.left = self.remove(node.left, modifiedNode.val)

            # Value is lesser than the node's value
            if val < node.val:
                node.left = remove(node.left, val)
            # Value is greater than the node's value
            elif val > node.val:
                node.right = remove(node.right, val)

        # Check if BST contains val
        if self.contains(val):
            remove(self, val)


# ? Tests
tree = Node(val=30)
tree.insert(20)
tree.insert(10)
tree.insert(25)
tree.insert(40)
tree.insert(50)
tree.insert(100)
x = tree.max()
print(x.val)
y = tree.min()
print(y.val)
print(tree.contains(50))
tree.delete(50)
print(tree.contains(50))
