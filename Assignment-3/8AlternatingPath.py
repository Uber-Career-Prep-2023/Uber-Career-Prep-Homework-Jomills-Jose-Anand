# Question 8: Alternating Path

# * Approach followed: BFS
# * Time complexity: O(m + n) where m is the number of edges and n is the number of nodes
# * Space complexity: O(n) where n is the number of nodes

# * Input: Array of tuples, origin, destination
# * Output: integer

# * Time taken: 27 minutes


# ? Function to find the shortest alternating path between two nodes
def alternatingPath(edges, origin, destination):

    # Create an adjacency list
    adjacency_list = {}

    for edge in edges:
        if edge[0] not in adjacency_list:
            adjacency_list[edge[0]] = []
        adjacency_list[edge[0]].append((edge[1], edge[2]))
    
    # Create a queue
    queue = []

    # Create a visited set
    visited = set()

    # Add the origin to the queue
    queue.append((origin, None, 0))

    # We will use a BFS approach to find the shortest path
    while queue:

        # Pop the first element from the queue
        node, color, length = queue.pop(0)

        # If the node is the destination, return the distance
        if node == destination:
            return length

        # If the node is not visited, add it to the visited set
        if node not in visited:
            if node in adjacency_list:
                for neighbour in adjacency_list[node]:
                    if neighbour[1] != color:
                        visited.add(node)
                        queue.append((neighbour[0], neighbour[1], length + 1))

    # If no path is found, return -1
    return -1


# ? Test cases

# Test case 1
print(
    alternatingPath(
        [("A", "B", "blue"), ("A", "C", "red"), ("B", "D", "blue"), ("B", "E", "blue"), ("C", "B", "red"), ("D", "C", "blue"), ("A", "D", "red"), ("D", "E", "red"), ("E", "C", "red")],
        "A", "E"
    )
)

# Test case 2
print(
    alternatingPath(
        [("A", "B", "blue"), ("A", "C", "red"), ("B", "D", "blue"), ("B", "E", "blue"), ("C", "B", "red"), ("D", "C", "blue"), ("A", "D", "red"), ("D", "E", "red"), ("E", "C", "red")],
        "E", "D"
    )
)