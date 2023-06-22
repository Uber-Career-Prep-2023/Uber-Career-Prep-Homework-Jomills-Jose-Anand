# Question 6: Road Networks

# * Approach followed: DFS 
# * Time complexity: O(m + n) where m is the number of roads and n is the number of towns
# * Space complexity: O(n) where n is the number of towns

# * Input: array of towns, array of roads
# * Output: integer denoting the number of road networks

# * Time taken: 13 minutes


# ? Function to find the number of road networks
def RoadNetworks(listOfTowns, listOfRoads):

    # Create an adjacency list
    adjacencyList = {}
    for i in range(len(listOfRoads)):
        if listOfRoads[i][0] not in adjacencyList:
            adjacencyList[listOfRoads[i][0]] = []
        adjacencyList[listOfRoads[i][0]].append(listOfRoads[i][1])
        if listOfRoads[i][1] not in adjacencyList:
            adjacencyList[listOfRoads[i][1]] = []
        adjacencyList[listOfRoads[i][1]].append(listOfRoads[i][0])
    
    # Create a visited array
    visited = {}
    for i in adjacencyList:
        visited[i] = False

    # Create a function to perform DFS
    def DFS(node):
        visited[node] = True
        for i in adjacencyList[node]:
            if not visited[i]:
                DFS(i)

    # Create a variable to store the number of road networks
    numberOfRoadNetworks = 0

    # Iterate through the adjacency list
    for i in adjacencyList:
        if not visited[i]:
            DFS(i)
            numberOfRoadNetworks += 1

    # Return the number of road networks
    return numberOfRoadNetworks


# ? Test cases

# Test case 1
print(RoadNetworks(["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy"], 
[("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"), ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"), ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")]))

# Test case 2
print(RoadNetworks(["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"], 
[("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"), ("Kahului", "Haiku"), ("Hana", "Haiku"), ("Kahului", "Lahaina"), ("Princeville", "Lihue"), ("Lihue", "Waimea")]))