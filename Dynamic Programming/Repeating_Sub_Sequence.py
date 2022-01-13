"""
Repeating Sub-Sequence

Asked In : GOOGLE
LEVEL : MEDIUM

Problem Description

Given a string A, find length of the longest repeating sub-sequence such that the two subsequence don’t have same string character at same position,

i.e., any i’th character in the two subsequences shouldn’t have the same index in the original string.

NOTE: Sub-sequence length should be greater than or equal to 2.



Problem Constraints
 1 <= |A| <= 100



Input Format
The first and the only argument of input contains a string A.



Output Format
Return an integer, 0 or 1:

    => 0 : False
    => 1 : True


Example Input
Input 1:

 A = "abab"
Input 2:

 A = "abba"


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 "ab" is repeated.
Explanation 2:

 There is no repeating subsequence.
"""

"""
HINT1:
Our task is to find a repeating subsequence.
Or rather, lets say if we can find the longest repeating subsequence. If the length > 1, we return 0.

Now, to find longest repeating subsequence, lets try finding the longest common subsequence between the string A and itself ( LCS(A, A) ).
The only restriction we want to impose is that you cannot match a character with its replica in the other string.
In other words, if S1 and S2 are the replicas of the string for which we want to find LCS, S1[i] != S2[i] for all index i.
"""

"""
Solution Approach:
Ok here we will see what is the recurrance relation for our problem

Rec(i, j) =   |
              |   Rec(i + 1, j)
         max  |
              |   Rec(i, j + 1)
              |
              |   Rec(i + 1, j + 1) + 1 IF i != j and A[i] == A[j] 
              |

We will leave it upto you to take care of the base cases
"""


class Solution:
    # @param A : string
    # @return an integer
    def anytwo(self, A):

        def findLongestRepeatingSubSeq(A):
            n = len(A)
            dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    if A[i - 1] == A[j - 1] and i != j:
                        dp[i][j] = 1 + dp[i - 1][j - 1]
                    else:
                        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
            return dp[n][n]

        return int(findLongestRepeatingSubSeq(A) >= 2)

