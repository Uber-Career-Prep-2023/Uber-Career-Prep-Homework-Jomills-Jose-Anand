# Question 4: Number of Islands

# * Approach followed: depth first search
# * Time complexity: O(m*n) where m is the number of rows and n is the number of columns
# * Space complexity: O(m*n) where m is the number of rows and n is the number of columns

# * Input: input matrix
# * Output: integer denoting number of islands

# * Time taken: 20 minutes


# ? Function to perform depth first search
def dfs(matrix, i, j):

    # Base checks:
    # 1. If i and j are out of bounds
    # 2. If the current cell is 0
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] != 1:
        return
    
    # Mark the current cell as visited
    matrix[i][j] = "X"

    # Perform dfs on all the adjacent cells
    dfs(matrix, i+1, j)
    dfs(matrix, i-1, j)
    dfs(matrix, i, j+1)
    dfs(matrix, i, j-1)


# ? Function to find the number of islands
def numberOfIslands(matrix):

    # Base check
    if len(matrix) == 0:
        return 0
    
    # Initialize the number of islands to 0
    numberOfIslands = 0

    # Traverse through the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[1])):

            # If the current cell is 1, perform dfs on it
            if matrix[i][j] == 1:
                dfs(matrix, i, j)
                numberOfIslands += 1

    # Return the number of islands
    return numberOfIslands


# ? Test cases

# Test case 1
matrix = [[1, 1, 0, 0, 0],[0, 1, 0, 0, 1],[1, 0, 0, 1, 1],[0, 0, 0, 0, 0],[1, 0, 1, 0, 1]]
print(numberOfIslands(matrix))  # Output: 6

# Test case 2
matrix = [[1, 0, 1, 1, 1],[1, 1, 0, 1, 1],[0, 1, 0, 0, 0],[0, 0, 0, 1, 0],[0, 0, 0, 0, 0]]
print(numberOfIslands(matrix))  # Output: 3

# Test case 3
matrix = [[1, 0, 0], [0, 0, 0]]
print(numberOfIslands(matrix))  # Output: 1