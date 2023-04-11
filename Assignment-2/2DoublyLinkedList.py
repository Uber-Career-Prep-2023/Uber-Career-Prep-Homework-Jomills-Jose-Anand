# Question 2: Doubly Linked List

# * Time taken: 17 minutes + additional for comments

# ! Node class defintion
class Node:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


# ? Function to create new Node at the front of the linked list
def insertAtFront(head, val):

    # * Approach followed: nil (create new node and reassign pointers)
    # * Time complexity: O(1)
    # * Space complexity: O(1)

    # * Input: current head and value of new node
    # * Output: new head

    # create a new Node and populate it; then return it as the new head
    newNode = Node()
    newNode.val = val
    newNode.next = head
    newNode.prev = None
    return newNode


# ? Function to create new Node at the back of the linked list
def insertAtBack(head, val):

    # * Approach followed: iterate to the end of the list and add new Node
    # * Time complexity: O(n)
    # * Space complexity: O(1)

    # * Input: current head and value of new node
    # * Output: None

    # create a new Node and populate it
    newNode = Node()
    newNode.val = val
    newNode.next = None

    # create an iterator to reach the end of the linked list
    iterator = head
    if not head:
        # if there's no linked list, we return None
        return None

    # iterate over the linked list
    while iterator.next:
        iterator = iterator.next

    # assign the new Node as the last element
    newNode.prev = iterator
    iterator.next = newNode


# ? Function to create new Node after a specific node
def insertAfter(head, val, loc):

    # * Approach followed: iterate to the specified node and insert element after
    # * Time complexity: O(n)
    # * Space complexity: O(1)

    # * Input: current head, value of new node, and specified node
    # * Output: None

    # create a new Node and populate it
    newNode = Node()
    newNode.val = val

    # create an iterator to reach the specified node
    iterator = head
    if not head:
        return None

    # iterate over the linked list
    while iterator != loc:

        # If the specified node doesn't exist, it returns None
        if not iterator:
            return None

        iterator = iterator.next

    # assign the new Node as the element after the specified Node
    newNode.next = iterator.next
    iterator.next = newNode
    newNode.prev = iterator


# ? Function to delete first node
def deleteFront(head):

    # * Approach followed: nil (delete first node and return new head)
    # * Time complexity: O(1)
    # * Space complexity: O(1)

    # * Input: current head
    # * Output: updated head

    # update head
    if head.next:
        head = head.next
        head.prev = None
    else:
        return None

    # return the updated head
    return head


# ? Function to delete last node
def deleteBack(head):

    # * Approach followed: iterate to second last element and delete element element after
    # * Time complexity: O(1)
    # * Space complexity: O(n)

    # * Input: current head
    # * Output: None

    # create an iterator to reach the end of the linked list
    iterator = head
    if not head:
        return None

    # iterate over the linked list
    while iterator.next and iterator.next.next:
        iterator = iterator.next

    # update second last element
    iterator.next = None


# ? Function to delete specified node
def deleteNode(head, loc):

    # * Approach followed: fixed distance two pointer
    # * Time complexity: O(1)
    # * Space complexity: O(n)

    # * Input: current head
    # * Output: None

    # create an iterator to reach the specified Node of the linked list
    iterator = head
    if not head:
        return None

    # If head is loc
    if head == loc:
        return None

    # iterate over the linked list
    while iterator.next != loc:

        # If the specified node doesn't exist, it returns None
        if not iterator.next:
            return None

        iterator = iterator.next

    # update linked list
    iterator.next = iterator.next.next
    iterator.next.prev = iterator


# ? Function to find length of linked list
def length(head):

    # * Approach followed: iterate to the end of the list
    # * Time complexity: O(n)
    # * Space complexity: O(1)

    # * Input: current head
    # * Output: None

    # create a counter
    counter = 0

    # create an iterator to reach the end of the linked list
    iterator = head
    if not head:
        # if there's no linked list, we return 0
        return counter

    # iterate over the linked list
    while iterator:
        counter += 1
        iterator = iterator.next

    # return count
    return counter


# ? Function to reverse a linked list iteratively
def reverseIterative(head):

    # * Approach followed: iterate to the end of the list
    # * Time complexity: O(n)
    # * Space complexity: O(1)

    # * Input: current head
    # * Output: None

    # create temporary nodes and iterator
    curr_node = head
    prev_node = None
    temp_node = None

    # iterate through the linked list
    while curr_node:
        temp_node = curr_node
        curr_node = curr_node.next
        temp_node.next = prev_node
        temp_node.prev = curr_node
        prev_node = temp_node

    # return updated head
    return temp_node


# ? Function to reverse a linked list recursively
def reverseRecursive(head):

    # * Approach followed: recursively call the function to reverse the linked list
    # * Time complexity: O(n)
    # * Space complexity: O(1)

    # * Input: current head
    # * Output: None

    # case for no head
    if not head:
        return None

    # reverse current node
    head.next, head.prev = head.prev, head.next

    # check if previous node exists, otherwise return head
    if head.prev:
        return reverseRecursive(head.prev)

    return head


# ? Tests

newNode = insertAtFront(None, 5)
insertAtBack(newNode, 10)
insertAfter(newNode, 7, newNode)
print(length(newNode))
insertAtBack(newNode, 15)
insertAtBack(newNode, 20)
insertAtBack(newNode, 25)
print(length(newNode))
newNode = deleteFront(newNode)
deleteBack(newNode)
print(length(newNode))
newNode = reverseIterative(newNode)
print(length(newNode))
newNode = reverseRecursive(newNode)
print(length(newNode))
