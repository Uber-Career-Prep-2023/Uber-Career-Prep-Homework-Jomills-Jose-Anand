# Question 10: Prerequisite Courses

# * Approach followed: topological sort
# * Time complexity: O(V + E) where V is the number of vertices and E is the number of edges
# * Space complexity: O(V + E) where V is the number of vertices and E is the number of edges

# * Input: array, dictionary
# * Output: sorted array

# * Time taken: 34 minutes


# ? Function to find order to take courses
def prerequisiteCourses(courseList, prerequisites):

    # Output array
    outputArray = []

    # Visited set
    visited = set()

    # Trajectory set
    trajectory = set()

    # Define a function for topological sort
    def topologicalSort(course, prerequisites, visited, trajectory, outputArray):

        # If the course was already in the path, return
        if course in trajectory:
            return False
    
        # If the course is already visited, return
        if course in visited:
            return True
        
        # Add the course to the trajectory
        trajectory.add(course)

        # If the course has prerequisites, recursively call the function
        if course in prerequisites:
            for prerequisite in prerequisites[course]:
                if not topologicalSort(prerequisite, prerequisites, visited, trajectory, outputArray):
                    return False
        
        # Remove the course from the trajectory
        trajectory.remove(course)
        
        # Add the course to the visited set
        visited.add(course)

        # Add the course to the output array
        outputArray.append(course)

        return True
    
    # Iterate through the course list
    for course in courseList:
        if not topologicalSort(course, prerequisites, visited, trajectory, outputArray):
            return []
        
    # Return the output array
    return outputArray

# ? Test cases

# Test case 1
print(
    prerequisiteCourses(
        ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"], { "Data Structures": ["Intro to Programming"], "Advanced Algorithms": ["Data Structures"], "Operating Systems": ["Advanced Algorithms"], "Databases": ["Advanced Algorithms"] }
    )
)

# Test case 2
print(
    prerequisiteCourses(
        ["Intro to Writing", "Contemporary Literature", "Ancient Literature", "Comparative Literature", "Plays & Screenplays"], { "Contemporary Literature": ["Intro to Writing"], "Ancient Literature": ["Intro to Writing"], "Comparative Literature": ["Ancient Literature", "Contemporary Literature"], "Plays & Screenplays": ["Intro to Writing"] }
    )
)