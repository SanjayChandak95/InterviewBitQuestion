"""
Interleaving Strings

LEVEL : HARD
Asked In : GOOGLE, YAHOO

Given A, B, C, find whether C is formed by the interleaving of A and B.

Input Format:*

The first argument of input contains a string, A.
The second argument of input contains a string, B.
The third argument of input contains a string, C.
Output Format:

Return an integer, 0 or 1:
    => 0 : False
    => 1 : True
Constraints:

1 <= length(A), length(B), length(C) <= 150
Examples:

Input 1:
    A = "aabcc"
    B = "dbbca"
    C = "aadbbcbcac"

Output 1:
    1

Explanation 1:
    "aa" (from A) + "dbbc" (from B) + "bc" (from A) + "a" (from B) + "c" (from A)

Input 2:
    A = "aabcc"
    B = "dbbca"
    C = "aadbbbaccc"

Output 2:
    0

Explanation 2:
    It is not possible to get C by interleaving A and B.
"""

"""
HINT1:
Let n,m be the length of s1 and s2 respectively.
You need to check if using portion upto n and portion upto m if s3 can be formed or not.
So basically last character of s3 should be something from nth postion of s1 or mth position of s2. How can you recursively simulate this?

SOLUTION APPROACH:
Lets again look at the bruteforce solution for this question.
Given the string S1, S2, S3, the first character of S3 has to match with either the first character of S1 or S2. If it matches with first character of S1, we try to see if solution is possible with remaining part of S1, all of S2, and remaining part of S3. Then we do the same thing for S2.

The pseudocode might look something like this :

    bool isInterleave(int index1, int index2, int index3) {
                    // HANDLE BASE CASES HERE
        
        bool answer = false; 
        if (index1 < s1.length() && s1[index1] == s3[index3]) answer |= isInterleave(index1 + 1, index2, index3 + 1);
        if (index2 < s2.length() && s2[index2] == s3[index3]) answer |= isInterleave(index1, index2 + 1, index3 + 1);
        
        return answer;
    }
Again, index1, index2, and index3 can only take S1.length(), S2.length() and S3.length() possibilities respectively. Can you think of a memoization solution using the observation ?
BONUS: Can you eliminate one of the state i.e. come up with something having only two arguments.
"""

"""USING TWO STATE ONLY"""
class Solution:
    # @param A : string
    # @param B : string
    # @param C : string
    # @return an integer
    def isInterleave(self, A, B, C):
        cache = {}

        c = list(C)

        def helper(n, m):
            k = len(c)
            if n + m != k:
                return 0
            if n == m == k == 0:
                return 1
            if n == 0:
                return C[:k] == B[:m]
            if m == 0:
                return C[:k] == A[:n]
            if k == 0:
                return 0

            if (n, m) in cache:
                return cache[(n, m)]

            ans = 0
            check = c.pop()
            if A[n - 1] == check:
                ans = int(ans or helper(n - 1, m))
            if B[m - 1] == check:
                ans = int(ans or helper(n, m - 1))
            cache[(n, m)] = ans
            c.append(check)
            return cache[(n, m)]

        return helper(len(A), len(B))

