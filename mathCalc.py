import math
def uniquePaths(m, n):
    return math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1)

print(uniquePaths(3, 7))
print(uniquePaths(3, 2))