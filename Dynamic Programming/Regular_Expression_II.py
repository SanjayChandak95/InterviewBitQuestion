"""
Regular Expression II

Level : HARD
Asked In : FACEBOOK, MICROSOFT, GOOGLE

Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.

'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:

int isMatch(const char *s, const char *p)
Some examples:

isMatch("aa","a") → 0
isMatch("aa","aa") → 1
isMatch("aaa","aa") → 0
isMatch("aa", "a*") → 1
isMatch("aa", ".*") → 1
isMatch("ab", ".*") → 1
isMatch("aab", "c*a*b") → 1
Return 0 / 1 ( 0 for false, 1 for true ) for this problem

"""
"""
HINT1:
It might seem deceptively easy even you know the general idea, but programming it correctly with all the details require careful thought.
Think carefully how you would do matching of ‘’. Please note that ‘’ in regular expression is different from wildcard matching, as we match the previous character 0 or more times. But, how many times? If you are stuck, recursion is your friend.
This problem is a tricky one. Due to the huge number of edge cases, many people would write lengthy code and have numerous bugs on their first try. Try your best getting your code correct first, then refactor mercilessly to as clean and concise as possible!

SOLUTION APPROACH:
This looks just like a straight forward string matching, isn’t it? Couldn’t we just match the pattern and the input string character by character? The question is, how to match a '*' ?

A natural way is to use a greedy approach; that is, we attempt to match the previous character as many as we can. Does this work? Let us look at some examples.

s = “abbbc”
p = “ab*c”
Assume we have matched the first ‘a’ on both s and p. When we see "b*" in p, we skip all b’s in s. Since the last ‘c’ matches on both side, they both match.

s = “ac”
p = “ab*c”
After the first ‘a’, we see that there is no b’s to skip for “b*”. We match the last ‘c’ on both side and conclude that they both match.
It seems that being greedy is good. But how about this case?

s = “abbc”
p = “ab*bbc”
When we see “b*” in p, we would have skip all b’s in s. They both should match, but we have no more b’s to match. Therefore, the greedy approach fails in the above case.
One might be tempted to think of a quick workaround. How about counting the number of consecutive b’s in s? If it is smaller or equal to the number of consecutive b’s after “b*” in p, we conclude they both match and continue from there. For the opposite, we conclude there is not a match.
This seem to solve the above problem, but how about this case:
s = “abcbcd” 
p = “a.*c.*d”
Here, “.*” in p means repeat ‘.’ 0 or more times. Since ‘.’ can match any character, it is not clear how many times ‘.’ should be repeated. Should the ‘c’ in p matches the first or second ‘c’ in s? Unfortunately, there is no way to tell without using some kind of exhaustive search.
We need some kind of backtracking mechanism such that when a matching fails, we return to the last successful matching state and attempt to match more characters in s with ‘*’. This approach leads naturally to recursion.
The recursion mainly breaks down elegantly to the following two cases:
If the next character of p is NOT ‘*’, then it must match the current character of s. Continue pattern matching with the next character of both s and p.
If the next character of p is ‘*’, then we do a brute force exhaustive matching of 0, 1, or more repeats of current character of p… Until we could not match any more characters.
You would need to consider the base case carefully too. That would be left as an exercise to the reader. :)

"""
import sys

sys.setrecursionlimit(10 ** 6)


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def isMatch(self, A, B):
        # cache = {}
        # def helper(n,m):
        # 	if n==m ==0:
        # 		return 1
        # 	if n == 0:
        # 		return int(B[:m].count("*") >= m//2)
        # 	if m==0:
        # 		return 0

        # 	if (n,m) in cache:
        # 		return cache[(n,m)]

        # 	elif A[n-1] == B[m-1] or B[m-1] == ".":
        # 		cache[(n,m)] = int(helper(n-1, m-1))
        # 	elif B[m-1] == "*":
        # 		if m > 1 and (A[n-1] == B[m-2] or B[m-2] == "."):
        # 			cache[(n,m)] = int(helper(n-1, m) or helper(n-1, m-2) or helper(n, m-2))
        # 		elif m>1:
        # 			cache[(n,m)] = helper(n, m-2)
        # 		# cache[(n,m)] = int(helper(n-2, m) or helper(n, m-1) or helper(n-1, m-1))
        # 	else:
        # 		cache[(n,m)] = 0
        # 	return cache[(n,m)]
        # return helper(len(A), len(B))
        n, m = len(A), len(B)
        dp = [[0 for j in range(m + 1)] for i in range(n + 1)]
        dp[0][0] = 1
        curr_star = 0
        for j in range(1, m + 1):
            curr_star += (1 if B[j - 1] == "*" else 0)
            if curr_star >= (j // 2):
                dp[0][j] = 1
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if A[i - 1] == B[j - 1] or B[j - 1] == ".":
                    dp[i][j] = dp[i - 1][j - 1]
                elif B[j - 1] == "*":
                    if j > 1 and (A[i - 1] == B[j - 2] or B[j - 2] == "."):
                        dp[i][j] = int(dp[i - 1][j] or dp[i - 1][j - 2] or dp[i][j - 2])
                    elif j > 1:
                        dp[i][j] = dp[i][j - 2]
                else:
                    dp[i][j] = 0
        return dp[-1][-1]
