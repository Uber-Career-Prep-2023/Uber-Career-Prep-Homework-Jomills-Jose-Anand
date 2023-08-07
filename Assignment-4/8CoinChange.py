# Question 8: Coin Change

# * Approach followed: dynamic programming
# * Time complexity: O(sum * len(coins))
# * Space complexity: O(len(coins))

# * Input: integer sum, list of coins
# * Output: integer number of ways to get the sum using the coins

# * Time taken: 34 minutes


# ? Function to determine the denominations of coins to be used to get the target sum
def coinChange(sum, coins):
    
    # Initialize the array to store the number of ways to get the sum
    dp = [0] * (sum + 1)

    # Base case
    dp[0] = 1

    # Iterate over the coins
    for coin in coins:
        # Iterate over the sum
        for i in range(coin, sum + 1):
            # Update the number of ways to get the sum
            dp[i] += dp[i - coin]
   
    # Return the number of ways to get the sum
    return dp[-1]


# ? Test cases

# Test case 1
print(coinChange(3, [1, 2, 3])) # 3

# Test case 2
print(coinChange(5, [2])) # 0

# Test case 3
print(coinChange(10, [10])) # 1

# Test case 4
print(coinChange(0, [1, 2, 3])) # 1

# Test case 5
print(coinChange(20, [2, 5, 10])) # 6

# Test case 6
print(coinChange(15, [2, 5, 10])) # 3