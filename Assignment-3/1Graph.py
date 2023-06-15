# Question 1: Adjacency List Representation of Graph

# * Time taken: ~1 hour

#? Class to represent a graph
class Graph:
    def __init__(self, vertices):

        self.graph = {}
        for i in vertices:
            if i[0] not in self.graph:
                self.graph[i[0]] = []
            if i[1] not in self.graph:
                self.graph[i[1]] = []
            self.graph[i[0]].append(i[1])
        
        self.V = len(self.graph)
    
    def printGraph(self):
        print(self.graph)
        

# ? Function to perform breadth first search
def bfs(target, graph):

    # * Time complexity: O(v+e) v: number of vertices, e: number of edges
    # * Space complexity: O(v) v: number of vertices
 
    # * Input: target value, graph
    # * Output: boolean value

    # Initialize visited and queue arrays
    visited = []
    queue = []
    element = None

    # Find the first element in the graph
    for i in range(graph.V):
        if i in graph.graph:
            element = i
            break

    # Add the first element to the queue
    queue.append(element)
    visited.append(element)

    # Iterate over the queue
    while queue:
        temp = queue.pop(0)
        if temp == target:
            return True

        for vertex in graph.graph[temp]:
            if vertex not in visited:
                queue.append(vertex)
                visited.append(vertex)
            if vertex == target:
                return True

    return False


# ? Function to perform depth first search
def dfs(target, graph):

    # * Time complexity: O(v+e) v: number of vertices, e: number of edges
    # * Space complexity: O(v+e) v: number of vertices, e: number of edges

    # * Input: target value, graph
    # * Output: boolean value

    # ? Helper function to perform depth first search
    def helper_dfs(target, node, visited):

        visited.append(node)

        if node == target:
            return True
        
        for vertex in graph.graph[node]:
            if vertex not in visited:
                if helper_dfs(target, vertex, visited):
                    return True
    
        return False
    

    # Initialize visited and stack arrays
    visited = []
    element = None

    # Find the first element in the graph
    for i in range(graph.V):
        if i in graph.graph:
            element = i
            break
    
    # Call the helper function
    return helper_dfs(target, element, visited)


# ? Function to perform topological sort
def topologicalSort(graph):

    # * Time complexity: O(v+e) v: number of vertices, e: number of edges
    # * Space complexity: O(v) v: number of vertices

    # * Input: graph
    # * Output: array of sorted elements

    # ? Helper function to perform topological sort
    def helper_topologicalSort(node, visited, stack):

        visited.append(node)

        for vertex in graph.graph[node]:
            if vertex not in visited:
                helper_topologicalSort(vertex, visited, stack)
        
        stack.insert(0, node)

    
    # Initialize visited and stack arrays
    visited = []
    stack = []
    element = None

    # Find the first element in the graph
    for i in range(graph.V):
        if i in graph.graph:
            element = i
            break

    # Call the helper function
    for i in range(graph.V):
        if i not in visited:
            helper_topologicalSort(i, visited, stack)

    return stack


# ? Tests

newGraph = Graph([(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)])
newGraph.printGraph()

print(bfs(0, newGraph))
print(bfs(4, newGraph))

print(dfs(0, newGraph))
print(dfs(4, newGraph))

print(topologicalSort(newGraph))