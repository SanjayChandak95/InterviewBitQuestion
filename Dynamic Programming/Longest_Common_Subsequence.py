"""
Longest Common Subsequence

Asked In : AJIO
Level : EASY

Problem Description:
    Given two strings A and B. Find the longest common sequence ( A sequence which does not need to be contiguous),
     which is common in both the strings.
    You need to return the length of such longest common subsequence.

Problem Constraints
    1 <= |A|, |B| <= 1005

Input Format
First argument is an string A.

Second argument is an string B.



Output Format
Return the length of such longest common subsequence between string A and string B.


Example Input
Input 1:

 A = "abbcdgf"
 B = "bbadcgf"


Example Output
Output 1:

 5


Example Explanation
Explanation 1:

 The longest common subsequence is "bbcgf", which has a length of 5

"""

"""
HINT 1:
if for some (i, j) A[i] = B[j], then one of the possible longest common subsequence can be
 Longest common subsequence of(A[1..i-1], B[1....j-1]) + A[i] +  Longest common subsequence
  of(A[i+1....n], B[j+1....m])

Solution Approach : 
LCS(A[1.....i], B[1........j]) = 
    maximum (LCS(A[1.....i-1], B[1.....j-1] + 1,       //if(A[i] = B[j])
             LCS(A[1.....i-1], B[1.....j] ,
             LCS(A[1.....i], B[1.....j-1] )

"""

import sys

sys.setrecursionlimit(10 ** 6)


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        # cache = {}
        # def helper(A,B):
        #     n,m = len(A), len(B)
        #     if n == 0 or m == 0:
        #         return 0
        #     if (n,m) in cache:
        #         return cache[(n,m)]
        #     if A[-1] == B[-1]:
        #         cache[(n,m)] =  1+helper(A[:-1], B[:-1])
        #     else:
        #         cache[(n,m)] = max(helper(A, B[:-1]), helper(A[:-1],B))
        #     return cache[(n,m)]
        # return helper(A,B)
        n = len(A)
        m = len(B)
        dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]