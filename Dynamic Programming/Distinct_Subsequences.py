"""
Distinct Subsequences

Asked In : GOOGLE
Level : MEDIUM

Given two sequences A, B, count number of unique ways in sequence A, to form a subsequence that is identical to the sequence B.

Subsequence : A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, “ACE” is a subsequence of “ABCDE” while “AEC” is not).

Input Format:

The first argument of input contains a string, A.
The second argument of input contains a string, B.
Output Format:

Return an integer representing the answer as described in the problem statement.
Constraints:

1 <= length(A), length(B) <= 700
Example :

Input 1:
    A = "abc"
    B = "abc"

Output 1:
    1

Explanation 1:
    Both the strings are equal.

Input 2:
    A = "rabbbit"
    B = "rabbit"

Output 2:
    3

Explanation 2:
    These are the possible removals of characters:
        => A = "ra_bbit"
        => A = "rab_bit"
        => A = "rabb_it"

    Note: "_" marks the removed character.
"""

"""
HINT 1 : 
Can you solve the problem for some prefix of first string and some prefix of second string and use it to compute the final answer?
Try to think of DP on prefixes of both strings.

Solution Approach:
As a typical way to implement a dynamic programming algorithm, we construct a matrix dp, where each cell dp[i][j] represents the number of solutions of aligning substring T[0..i] with S[0..j];
Rule 1). dp[0][j] = 1, since aligning T = “” with any substring of S would have only ONE solution which is to delete all characters in S.
Rule 2). when i > 0, dp[i][j] can be derived by two cases:
case 1). if T[i] != S[j], then the solution would be to ignore the character S[j] and align substring T[0..i] with S[0..(j-1)]. Therefore, dp[i][j] = dp[i][j-1].
case 2). if T[i] == S[j], then first we could adopt the solution in case 1), but also we could match the characters T[i] and S[j] and align the rest of them (i.e. T[0..(i-1)] and S[0..(j-1)]. As a result, dp[i][j] = dp[i][j-1] + d[i-1][j-1]
e.g. T = B, S = ABC
dp[1][2]=1: Align T’=B and S’=AB, only one solution, which is to remove character A in S’.

"""


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def numDistinct(self, A, B):
        cache = {}

        def helper(n, m):
            # if A == B:
            #     return 1
            if m == 0:
                return 1
            if n == 0:
                return 0

            if (n, m) in cache:
                return cache[(n, m)]
            elif A[n - 1] == B[m - 1]:
                cache[(n, m)] = helper(n - 1, m - 1) + helper(n - 1, m)
            else:
                cache[(n, m)] = helper(n - 1, m)
            return cache[(n, m)]

        helper(len(A), len(B))
        # print(cache)
        return cache[(len(A), len(B))]
