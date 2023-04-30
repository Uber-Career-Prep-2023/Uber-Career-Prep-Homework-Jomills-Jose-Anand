# Question 9: Disconnect Cycle

# * Approach followed: two pointer - fast/slow
# * Time complexity: O(mn)
# * Space complexity: O(1)

# * Input: input linked list
# * Output: None

# * Time taken: 40 minutes -- incomplete

# ! Node class defintion
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    # ? Function to remove cycles in a linked list
    def disconnectCycle(self):

        # base tests
        if not self.val or not self.next:
            return None

        # Defining head
        head = Node(val=self.val, next=self.next)

        # Setting slow and fast pointers
        slowPointer = head
        fastPointer = head

        while slowPointer and fastPointer:

            if not fastPointer.next:
                break

            fastPointer = fastPointer.next.next
            slowPointer = slowPointer.next

            if slowPointer == fastPointer:

                fastPointer = head

                while True:
                    if slowPointer.next == fastPointer.next:
                        break
                    slowPointer = slowPointer.next
                    fastPointer = fastPointer.next

                fastPointer.next = None

        # Updating object
        self.val = head.val
        self.next = head.next


# ? Test cases

test = Node()
test.disconnectCycle()
print(test.val)

test = Node(val=1)
test.disconnectCycle()
print(test.val)

test = Node(val=1, next=Node(val=2))
test.disconnectCycle()
print(test.val, test.next.val, test.next.next)

test = Node(val=1, next=Node(val=2))
test.next.next = test
print(test.val, test.next.val, test.next.next.val)
test.disconnectCycle()
print(test.val, test.next, test.next)
