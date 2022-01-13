"""
Scramble String

Asked In : NONE
LEVEL : HARD

Given a string A, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of A = “great”:


    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t

To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node “gr” and swap its two children, it produces a scrambled string “rgeat”.

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that “rgeat” is a scrambled string of “great”.

Similarly, if we continue to swap the children of nodes “eat” and “at”, it produces a scrambled string “rgtae”.

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that “rgtae” is a scrambled string of “great”.



Given two strings A and B of the same length, determine if B is a scrambled string of S.



Input Format:

The first argument of input contains a string A.
The second argument of input contains a string B.
Output Format:

Return an integer, 0 or 1:
    => 0 : False
    => 1 : True
Constraints:

1 <= len(A), len(B) <= 50
Examples:

Input 1:
    A = "we"
    B = "we"

Output 1:
    1

Input 2:
    A = "phqtrnilf"
    B = "ilthnqrpf"

Output 2:
    0

"""

"""
HINT:
Hint : Divide and Conquer + Dynamic Programming
On every step, you need to figure out if there exists one of the positions at root, using which the 2 parts of strings are scrambled strings of each other.
Try writing a bruteforce solution and see which steps can be memoized.

SOLUTION APPROACH:
Lets first think of a bruteforce solution.
Obviously the 2 strings need to have the same number of characters and the same character set, otherwise the answer is definitely no.

In the bruteforce solution, we loop to find out the root of the tree.
Lets say the root is the ith character of string s1. Then the first part of s1 [0…i) can either match ( be a scrambled string of ) to s2[0…i) or s2(i+1 .. L]. Depending on which part s1[0…i) matches to, we match the remaining part of s1 to remaining part of s2. Just to clarify when we say s1 matches s2, we mean s1 is a scrambled string of s2.

We can write a very easy recursive function for this.

    public boolean isScramble(String s1, String s2) {
        // CHECK BASE CASES HERE

        if (s1 not anagram of s2) return false;
        
        for(int i = 1; i < s1.length(); i++) { // i being the root position
            if(isScramble(s1.substring(0,i), s2.substring(0,i)) && isScramble(s1.substring(i), s2.substring(i))) return true;
            if(isScramble(s1.substring(0,i), s2.substring(s2.length()-i)) && isScramble(s1.substring(i), s2.substring(0, s2.length()-i))) return true;
        }
        return false;
    }
Now note that in any call for this function, the strings s1 and s2 would always be substrings of original S1 and S2. And we can specify substrings using startIndex, endIndex.

Which means the recursive function can only be called with (startIndex1, endIndex1, startIndex2, endIndex2) possible tuples which can only take LLL*L possibilities roughly.

Memoization ?

Additional Hint :

Function calls are only valid if endIndex1 - startIndex1 = endIndex2 - startIndex2.
Can you just look at (startIndex1, endIndex1, startIndex2) and infer the endIndex2 based on these values ?
Or keep passing around (startIndex1, startIndex2, length) ?
"""
"""REFER :  https://www.youtube.com/watch?v=SqA0o-DGmEw"""
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def isScramble(self, A, B):
        if len(A) != len(B):
            return 0
        if len(A) == 0:
            return 1
        if A == B:
            return 1
        if sorted(A) != sorted(B):
            return 0

        for i in range(1, len(A)):
            if self.isScramble(A[:i], B[:i]) and self.isScramble(A[i:], B[i:]):
                return 1
            if self.isScramble(A[-i:], B[:i]) and self.isScramble(A[:-i], B[i:]):
                return 1
        return 0
