# Question 5: Minimum Cost Stair Climbing

# * Approach followed: dynamic programming
# * Time complexity: O(n)
# * Space complexity: O(n)

# * Input: array of costs (greater than or equal to size 2)
# * Output: minimum cost to reach the top of the floor

# * Time taken: 17 minutes

# ? Function to return minimum cost to reach the top of the floor
def minCostClimbingStairs(cost):
    
    # Make a dp array to store minimum cost to reach ith floor
    dp = [0] * len(cost)

    # Base cases
    if not cost:
        return 0
    
    dp[0] = cost[0]
    dp[1] = cost[1]

    # Fill dp array
    for i in range(2, len(cost)):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])

    # Return minimum cost to reach the top of the floor
    return min(dp[-1], dp[-2])


# ? Test cases

# Test case 1
print(minCostClimbingStairs([4, 1, 6, 3, 5, 8]))
# Expected output: 9

# Test case 2
print(minCostClimbingStairs([11, 8, 3, 4, 9, 13, 10]))
# Expected output: 25

# Test case 3
print(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
# Expected output: 6

# Test case 4
print(minCostClimbingStairs([1, 1]))
# Expected output: 1

# Test case 5
print(minCostClimbingStairs([1, 1, 1, 1]))
# Expected output: 2