"""
Paint Fence
Algorithms
Easy
Accepted Rate
40%

DescriptionSolutionNotesDiscussLeaderboard
Description
There is a fence with n posts, each post can be painted with one of the k colors.
You have to paint all the posts such that no more than two adjacent fence posts have the same color.
Return the total number of ways you can paint the fence.

n and k are non-negative integers.

Example
Example 1:

Input: n=3, k=2
Output: 6
Explanation:
          post 1,   post 2, post 3
    way1    0         0       1
    way2    0         1       0
    way3    0         1       1
    way4    1         0       0
    way5    1         0       1
    way6    1         1       0
Example 2:

Input: n=2, k=2
Output: 4
Explanation:
          post 1,   post 2
    way1    0         0
    way2    0         1
    way3    1         0
    way4    1         1
"""

"""
Solution:
if n=1:
only one position then ans = k

if n == 2:
in case of diff : k*(k-1)
in case of same : k*1
total : k^2

if n==3:
in case of diff : k*(k-1)*k
in case of same : k*1*(k-1)
total = (k-1)*(k^2) + (k-1)*k

so dp[i] = (k-1)*(dp[i-1]+dp[i-2])
"""

class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """
    def numWays(self, n, k):
        # write your code here
        if n == 1:
            return k
        if n == 2:
            return k*k
        dp = [0]*(n+1)
        dp[1] = k
        dp[2] = k*k

        for i in range(3, n+1):
            dp[i] = (k-1)*(dp[i-1] + dp[i-2])
        return dp[n]
