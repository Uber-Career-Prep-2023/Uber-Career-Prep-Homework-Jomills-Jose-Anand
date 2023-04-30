# Question 7: MoveNthLastToFront

# * Approach followed: two pointer - reset/catch up
# * Time complexity: O(n)
# * Space complexity: O(1)

# * Input: input BST
# * Output: None

# * Time taken: 40 minutes

# ! Node class defintion
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    # ? Function to move nth element from the last to the front
    def moveNthElement(self, n):

        # Base checks
        if not self.val or (n < 1):
            return None

        # Define node to update
        tempNode = Node()
        head = Node(val=self.val, next=self.next)

        # Get the length of the linked list
        length = 0
        curNode = self

        while curNode:
            curNode = curNode.next
            length += 1

        # Check length against n
        if n > length:
            return None

        # Replace given node
        curNode = self
        maxLength = length - n - 1 if ((length - n - 1) > 0) else 0
        for i in range(0, maxLength):
            curNode = curNode.next
        if curNode.next:
            tempNode.val = curNode.next.val
            curNode.next = curNode.next.next
            tempNode.next = head
        else:
            return
        # Update head
        self.val = tempNode.val
        self.next = tempNode.next


# ? Test cases

newNode = Node()
newNode.moveNthElement(1)
print(newNode.val, newNode.next)

newNode = Node(val=1)
newNode.moveNthElement(1)
print(newNode.val, newNode.next)
newNode.moveNthElement(2)
print(newNode.val, newNode.next)

newNode = Node(val=1, next=Node(val=2))
newNode.moveNthElement(1)
print(newNode.val, newNode.next.val)
