"""
There is a row of n houses, where each house can be painted one of three colors: red, blue, or green.
The cost of painting each house with a certain color is different.
You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by an n x 3 cost matrix costs.

For example, costs[0][0] is the cost of painting house 0 with the color red;
costs[1][2] is the cost of painting house 1 with color green, and so on...

Return the minimum cost to paint all houses.

Input: costs = [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
"""

def minCost(costs):
    """
    0 - red (17) blue (2) green (17)
    dp[i][j] - mimimum cost of painting of 0th to ith houses making sure to paint the ith house with j color
    ans - min(dp[n-1][0], dp[n-1][1], dp[n-1][2])
    """
    n = len(costs)
    dp = [[ 0 for j in range(3)] for i in range(n)]

    for i in range(3):
        dp[0][i] = costs[0][i]

    for i in range(1, n):
        for j in range(3):
            if j == 0:
                dp[i][j] = costs[i][j] + min(dp[i-1][1], dp[i-1][2])
            elif j == 1:
                dp[i][j] = costs[i][j] + min(dp[i-1][0], dp[i-1][2])
            else:
                dp[i][j] = costs[i][j] + min(dp[i-1][0], dp[i-1][1])
    
    return min(dp[n-1])

costs = [[17,2,17],[16,16,5],[14,3,19]]
print(minCost(costs))


"""
There are a row of n houses, each house can be painted with one of the k colors.
The cost of painting each house with a certain color is different.
You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by an n x k cost matrix costs.

For example, costs[0][0] is the cost of painting house 0 with color 0;
costs[1][2] is the cost of painting house 1 with color 2, and so on...

Return the minimum cost to paint all houses.

Input: costs = [[1,5,3],[2,9,4]]
Output: 5
"""

def minCostK(costs):
    n = len(costs)
    k = len(costs[0])
    dp = [[ 0 for j in range(k)] for i in range(n)]

    for i in range(k):
        dp[0][i] = costs[0][i]

    # O(1) + O(n*k) + O(k) + O(n*k*k) + O(k)
    # O(n*k*k)
    

    for i in range(1, n):
        for j in range(k):
            minCost = float("inf")
            for l in range(k):
                if l == j: continue
                else: minCost = min(minCost, dp[i-1][l])
            dp[i][j] = costs[i][j] + minCost
    
    return min(dp[n-1])

costs = [[1,5,3],[2,9,4]]
print(minCostK(costs))




"""
Input: costs = [[1,3],[2,4]]
Output: 5
"""