
"""
You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array sweetness.

You want to share the chocolate with your k friends so you start cutting the chocolate bar into k + 1 pieces using k cuts, each piece consists of some consecutive chunks.

Being generous, you will eat the piece with the minimum total sweetness and give the other pieces to your friends.

Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.


Example 1:

Input: sweetness = [1,2,3,4,5,6,7,8,9], k = 5
Output: 6
Explanation: You can divide the chocolate to [1,2,3], [4,5], [6], [7], [8], [9]
Example 2:

Input: sweetness = [5,6,7,8,9,1,2,3,4], k = 8
Output: 1
Explanation: There is only one way to cut the bar into 9 pieces.
Example 3:

Input: sweetness = [1,2,2,1,2,2,1,2,2], k = 2
Output: 5
Explanation: You can divide the chocolate to [1,2,2], [1,2,2], [1,2,2]
"""

# is it possible to divide the choc bar into k + 1 pieces s.t.
# each piece has at least sweetness of x

# st = 6
# k = 2
# s = [1, 2, 3, 4, 5, 8]
# [1, 2, 3] [4, 5] [8]

# [1, 2, 3]
# x = 3
# k = 1
# [1, 2] [3]

def is_possible(sweetness, k, level):
    pieces = 0
    current_sweetness = 0
    for s in sweetness:
        current_sweetness += s
        if current_sweetness >= level:
            pieces += 1
            current_sweetness = 0
    return pieces >= k + 1

def get_max_total_sweetness(sweetness, k):
    low = 0
    high = sum(sweetness) // (k+1)
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        if is_possible(sweetness, k, mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans

# sweetness = [1,2,3,4,5,6,7,8,9]
# k = 5

# sweetness = [5,6,7,8,9,1,2,3,4]
# k = 8

sweetness = [1,2,2,1,2,2,1,2,2]
k = 2

# [1, 2, 3, 4] [5] [6] [7] [8] [9]

# 6
# [1, 2, 3] []

print(get_max_total_sweetness(sweetness, k))