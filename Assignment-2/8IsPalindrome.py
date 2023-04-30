# Question 8: IsPalindrome

# * Approach followed: two pointer - forward/backward
# * Time complexity: O(n)
# * Space complexity: O(1)

# * Input: input doubly linked list
# * Output: boolean

# * Time taken: 6 minutes

# ! Node class defintion
class Node:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


# ? Function to check if a linked list is a palindrome
def isPalindrome(head):

    # Get pointer to end of linked list
    endPointer = head
    while endPointer.next:
        endPointer = endPointer.next

    # Defining start pointer and checking palindrome
    startPointer = head

    while startPointer and endPointer:
        if not startPointer.val == endPointer.val:
            return False
        startPointer = startPointer.next
        endPointer = endPointer.next

    return True


# ? Test cases

tree = Node()
print(isPalindrome(tree))

tree = Node()
tree.val = 10
print(isPalindrome(tree))

tree1 = Node(val=10)
tree2 = Node(val=20)
tree3 = Node(val=10)
tree1.next = tree2
tree2.next = tree3
tree2.prev = tree1
print(isPalindrome(tree1))

tree1 = Node(val=10)
tree2 = Node(val=20)
tree3 = Node(val=30)
tree1.next = tree2
tree2.next = tree3
tree2.prev = tree1
print(isPalindrome(tree1))
