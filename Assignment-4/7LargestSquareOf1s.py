# Question 7: Largest Square of 1s

# * Approach followed: dynamic programming
# * Time complexity: O(m*n) where m is the number of rows and n is the number of columns
# * Space complexity: O(m*n) where m is the number of rows and n is the number of columns

# * Input: 2d matrix of 1s and 0s
# * Output: integer indicating the largest square of 1s in the matrix

# * Time taken: 42 minutes


# ? Function to determine the largest square of 1s in a matrix
def largestSquareof1s(matrix):
    
    # Create the dp matrix
    dp = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]

    # Initialize the maximum length of the square
    maxSquareLength = 0

    # Iterate over the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):

            # If the current element is 1
            if matrix[i][j] == 1:

                # Update the dp matrix
                dp[i + 1][j + 1] = min(dp[i][j], dp[i][j + 1], dp[i + 1][j]) + 1

                # Update the maximum length of the square
                maxSquareLength = max(maxSquareLength, dp[i + 1][j + 1])

    # Return the maximum length of the square
    return maxSquareLength
   


# ? Test cases

# Test case 1
print(largestSquareof1s([[1, 1, 1, 0, 1, 1, 1, 1], [1, 1, 0, 1, 1, 0, 1, 1], [1, 1, 1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 0, 1, 1, 1]]))
# Output: 2

# Test case 2
print(largestSquareof1s([[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 0, 1, 1, 0, 1, 1], [1, 1, 1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 0, 1, 1, 1]]))
# Output: 2

# Test case 3
print(largestSquareof1s([[0, 1, 0, 1, 1], [0, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 1, 1, 0, 0]]))
# Output: 3

# Test case 4
print(largestSquareof1s([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))
# Output: 0

# Test case 5
print(largestSquareof1s([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]))
# Output: 2

# Test case 6
print(largestSquareof1s([[1, 1, 1, 1, 1]]))
# Output: 1