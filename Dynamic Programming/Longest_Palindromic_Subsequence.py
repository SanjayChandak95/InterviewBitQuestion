"""
Longest Palindromic Subsequence

Asked In : LINKEDIN
Level : MEDIUM

Problem Description

Given a string A, find the common palindromic sequence ( A sequence which does not need to be contiguous and is a pallindrome), which is common in itself.
You need to return the length of longest palindromic subsequence in A.

NOTE:
Your code will be run on multiple test cases (<=10). Try to come up with an optimised solution.

Problem Constraints
 1 <= |A| <= 1005

Input Format
First and only argument is an string A.

Output Format
Return a integer denoting the length of longest palindromic subsequence in A.


Example Input
Input 1:

 A = "bebeeed"


Example Output
Output 1:

 4


Example Explanation
Explanation 1:

 The longest common palindromic subsequence is "eeee", which has a length of 4

"""

"""
Hint1 :
Suppose L[i][j] denotes the length of longest palindromic subsequence of substring [i, j] of string A.
So consider you know the value for L[i+1][j-1], L[i+1][j], L[i][j-1] how will you calculate the value of L[i][j].
"""

"""
Solution Approach:

The naive solution for this problem is to generate all subsequences of the given sequence and find the longest palindromic subsequence. This solution is exponential in term of time complexity. Let us see how this problem possesses both important properties of a Dynamic Programming (DP) Problem and can efficiently solved using Dynamic Programming.

1) Optimal Substructure:
Let X[0..n-1] be the input sequence of length n and L(0, n-1) be the length of the longest palindromic subsequence of X[0..n-1].

If last and first characters of X are same, then L(0, n-1) = L(1, n-2) + 2.
Else L(0, n-1) = MAX (L(1, n-1), L(0, n-2)).

Following is a general recursive solution with all cases handled.

// Every single character is a palindrome of length 1
L(i, i) = 1 for all indexes i in given sequence

// IF first and last characters are not same
If (X[i] != X[j])  L(i, j) =  max{L(i + 1, j),L(i, j - 1)} 

// If there are only 2 characters and both are same
Else if (j == i + 1) L(i, j) = 2  

// If there are more than two characters, and first and last 
// characters are same
Else L(i, j) =  L(i + 1, j - 1) + 2 
Considering the above implementation, following is a partial recursion tree for a sequence of length 6 with all different characters.

               L(0, 5)
             /        \ 
            /          \  
        L(1,5)          L(0,4)
       /    \            /    \
      /      \          /      \
  L(2,5)    L(1,4)  L(1,4)  L(0,3)
In the above partial recursion tree, L(1, 4) is being solved twice. If we draw the complete recursion tree, then we can see that there are many subproblems which are solved again and again. Since same suproblems are called again, this problem has Overlapping Subprolems property. So LPS problem has both properties (see this and this) of a dynamic programming problem. Like other typical Dynamic Programming(DP) problems, recomputations of same subproblems can be avoided by constructing a temporary array L[][] in bottom up manner.

"""

import sys

sys.setrecursionlimit(10 ** 6)


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        cache = {}

        def helper(A, start, end):
            if start == end:
                return 1
            if start > end:
                return 0

            if (start, end) in cache:
                return cache[(start, end)]
            if A[start] == A[end]:
                cache[(start, end)] = 2 + helper(A, start + 1, end - 1)
            else:
                cache[(start, end)] = max(helper(A, start + 1, end), helper(A, start, end - 1))
            return cache[(start, end)]

        return helper(A, 0, len(A) - 1)
