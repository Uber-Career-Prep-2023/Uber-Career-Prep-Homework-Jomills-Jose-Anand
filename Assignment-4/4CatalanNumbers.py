# Question 4: Catalan Numbers

# * Approach followed: returning catalan number from 0 to n
# * Time complexity: O(3^N)
# * Space complexity: O(n)

# * Input: integer n
# * Output: catalan number from 0 to n

# * Time taken: 9 minutes

# ? Function to calculate factorial of a number
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

# ? Function to calculate catalan number from 0 to n
def catalanNumber(n):
    catalan_array = []
    for i in range(n+1):
        catalan_array.append(factorial(2*i) // (factorial(i+1) * factorial(i)))
    
    return catalan_array


# ? Test cases

# Test case 1
print(catalanNumber(5))
# Expected output: [1, 1, 2, 5, 14, 42]

# Test case 2
print(catalanNumber(10))
# Expected output: [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796]

# Test case 3
print(catalanNumber(1))
# Expected output: [1, 1]

# Test case 4
print(catalanNumber(0))
# Expected output: [1]

# Test case 5
print(catalanNumber(20))
# Expected output: [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796,  58786, 208012, 742900, 2674440, 9694845, 35357670, 129644790, 477638700, 1767263190, 6564120420]