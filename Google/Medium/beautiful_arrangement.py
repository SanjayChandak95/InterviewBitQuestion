"""
Beautiful Arrangement
Algorithms
Medium
Accepted Rate
52%

DescriptionSolutionNotesDiscussLeaderboard
Description
Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully if one of the following is true for the ith position (1 <= i <= N) in this array:

The number at the ith position is divisible by i.
i is divisible by the number at the ith position.
Now given N, how many beautiful arrangements can you construct?

N is a positive integer and will not exceed 15.

Example
Example1

Input: 2
Output: 2
Explanation:

The first beautiful arrangement is [1, 2]:

Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).

Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

The second beautiful arrangement is [2, 1]:

Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).

Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
Example2

Input: 3
Output: 3
"""


class Solution:
    """
    @param N: The number of integers
    @return: The number of beautiful arrangements you can construct
    """

    def countArrangement(self, N):
        # Write your code here
        visited = ['1'] * N
        dp = {}

        def helper(index):
            if index == N + 1:
                return 1
            key = (index, ''.join(visited))
            if key in dp:
                return dp[key]
            a = 0
            for i in range(1, N + 1):
                if visited[i - 1] == '1' and (i % index == 0 or index % i == 0):
                    visited[i - 1] = '0'
                    a += helper(index + 1)
                    visited[i - 1] = '1'
            dp[(index, ''.join(visited))] = a
            return a

        return helper(1)
