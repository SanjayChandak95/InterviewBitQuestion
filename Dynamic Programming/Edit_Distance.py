"""
Edit Distance

Asked In : GOOGLE, LINKEDIN, MICROSOFT, AMAZON
LEVEL : MEDIUM

Given two strings A and B, find the minimum number of steps required to convert A to B. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character


Input Format:

The first argument of input contains a string, A.
The second argument of input contains a string, B.
Output Format:

Return an integer, representing the minimum number of steps required.
Constraints:

1 <= length(A), length(B) <= 450
Examples:

Input 1:
    A = "abad"
    B = "abac"

Output 1:
    1

Explanation 1:
    Operation 1: Replace d with c.

Input 2:
    A = "Anshuman"
    B = "Antihuman"

Output 2:
    2

Explanation 2:
    => Operation 1: Replace s with t.
    => Operation 2: Insert i.

"""

"""
HINT 1:
Can you solve the problem for some prefix of first string and some prefix of 
second string and use it to compute the final answer?
Try to think of DP on prefixes of both strings.
"""
"""
This is a very standard Dynamic programming problem.

Lets look at the bruteforce approach for finding edit distance of S1 and S2.
We are trying to modify S1 to become S2.

We look at the first character of both the strings.
If they match, we can look at the answer from remaining part of S1 and S2.
If they don’t, we have 3 options.
1) Insert S2’s first character and then solve the problem for remaining part of S2, and S1.
2) Delete S1’s first character and trying to match S1’s remaining string with S2.
3) Replace S1’s first character with S2’s first character in which case we solve the problem for remaining part of S1 and S2.

The code would probably look something like this :

int editDistance(string &S1, int index1, string &S2, int index2) {
// BASE CASES

if (S1[index1] == S2[index2]) {
     return editDistance(S1, index1 + 1, S2, index2 + 1);
} else {
     return min(
    1 + editDistance(S1, index1 + 1, S2, index2), // Delete S1 char
            1 + editDistance(S1, index1, S2, index2 + 1), // Insert S2 char
            1 + editDistance(S1, index1 + 1, S2, index2 + 1) // Replace S1 first char with S2 first char
     );
} }
The above approach is definitely exponential.
However, lets look at the number of ways in which the function can be called. S1 and S2 remain constant. The only thing changing is index1 and index2 which can take len(S1) * len(S2) number of values. Can you use it to memoize ?

You can use the above observation to also come up with a non recursive solution.
"""

import sys

sys.setrecursionlimit(10 ** 6)


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
        cache = {}

        def helper(n, m):
            if n == 0:
                return m
            if m == 0:
                return n
            if (n, m) in cache:
                return cache[(n, m)]

            if A[n - 1] == B[m - 1]:
                cache[(n, m)] = helper(n - 1, m - 1)
            else:
                cache[(n, m)] = 1 + min(helper(n, m - 1), helper(n - 1, m - 1), helper(n - 1, m))
            return cache[(n, m)]

        return helper(len(A), len(B))
