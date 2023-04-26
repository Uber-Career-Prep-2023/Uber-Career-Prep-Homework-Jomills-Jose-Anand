# Question 6: Dedup Sorted List

# * Approach followed: similar to catch-up two pointer
# * Time complexity: O(n)
# * Space complexity: O(1)

# * Input: input linked list
# * Output: None

# * Time taken: 9 minutes

# ! Node class defintion
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


# ? Function to remove duplicates from linked list
def dedupSortedArray(head):

    currNode = head

    # Iterate through the linked list
    while currNode:

        if not currNode.next:
            break

        # We check if there are duplicates
        if currNode.val == currNode.next.val:
            currNode.next = currNode.next.next
            continue

        # If not, we continue
        currNode = currNode.next


# ? Test cases

linkedList = Node()
linkedList.val = 1
linkedList.next = Node(val=2, next=Node(val=2))
dedupSortedArray(linkedList)
print(linkedList.val, linkedList.next.val, linkedList.next.next)

linkedList = Node()
dedupSortedArray(linkedList)
print(linkedList.val, linkedList.next)

linkedList = Node(val=1)
dedupSortedArray(linkedList)
print(linkedList.val, linkedList.next)
