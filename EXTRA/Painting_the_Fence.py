"""
https://practice.geeksforgeeks.org/problems/painting-the-fence3727/1
Painting the Fence

LEVEL : MEDIUM
"""

"""
Given a fence with n posts and k colors, 
find out the number of ways of painting the fence such that at most 2 adjacent 
posts have the same color. Since answer can be large return it modulo 10^9 + 7.


"""


def countWays(n, k):
    if k <= 1 and n > 2:
        # only one color
        return 0
    MOD = 10 ** 9 + 7
    # code here.
    if k <= 1 and n > 2:
        # only one color
        return 0
    first = k
    second = k * k
    for i in range(3, n + 1):
        third = ((first + second) * (k - 1)) % MOD
        first, second = second, third
    if n == 1:
        return first
    return second
    # cache = {}
    # def helper(past_seq, n, k):
    #     # if n==0:
    #     #     return 1
    #     if n == 1:
    #         return k
    #     if n == 2:
    #         return k*k
    #     if (past_seq, n) in cache:
    #         return cache[(past_seq, n)]
    #     ans = 0
    #     if past_seq == 2:
    #         ans = helper(1, n-1, k)
    #     if past_seq == 1:
    #         ans = (helper(1, n-2, k)+helper(1, n-1, k))*(k-1)
    #     cache[(past_seq, n)] = ans
    #     return cache[(past_seq, n)]
    # return helper(1,n,k)


if __name__ == "__main__":
    N = 4
    K = 2
    print(countWays(N, K))
