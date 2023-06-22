# Question 11: Vacation Destinations

# * Approach followed: BFS
# * Time complexity: O(m + n) where m is the number of cities and n is the number of routes
# * Space complexity: O(m) where m is the number of cities

# * Input: origin city, travel time k, array of arrays
# * Output: integers

# * Time taken: 23 minutes


# ? Function to find the maximum number of cities that can be visited in k hours
def vacationDestination(inputArray, originCity, k):

    # City count
    cityCount = -1

    # Make an adjacency list
    adjacencyList = {}
    for i in range(len(inputArray)):
        if not inputArray[i][0] in adjacencyList:
            adjacencyList[inputArray[i][0]] = []
        adjacencyList[inputArray[i][0]].append((inputArray[i][1], inputArray[i][2]))
        if not inputArray[i][1] in adjacencyList:
            adjacencyList[inputArray[i][1]] = []
        adjacencyList[inputArray[i][1]].append((inputArray[i][0], inputArray[i][2]))

    # Visited set
    visited = set()

    # Queue
    queue = []

    # Add origin city to queue
    queue.append((originCity, -1)) 

    # While queue is not empty
    while queue:

        city, time = queue.pop(0)

        # If time is greater than k, break
        if time > k:
            continue

        # If the city is visited, continue
        if city in visited:
            continue

        # Increment city count
        cityCount += 1

        # Add city to visited set
        visited.add(city)

        # Add stopover time
        time += 1

        # Iterate over the input array
        if city in adjacencyList:
            for i in range(len(adjacencyList[city])):
                queue.append((adjacencyList[city][i][0], time + adjacencyList[city][i][1]))

    # Return city count
    return cityCount

# ? Test cases

# Test case 1
print(
    vacationDestination(
       [("Boston", "New York", 4), ("New York", "Philadelphia", 2), ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)],
       "New York", 5 
    )
)

# Test case 2
print(
    vacationDestination(
       [("Boston", "New York", 4), ("New York", "Philadelphia", 2), ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)],
       "New York", 7 
    )
)

# Test case 3
print(
    vacationDestination(
       [("Boston", "New York", 4), ("New York", "Philadelphia", 2), ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)],
       "New York", 8 
    )
)