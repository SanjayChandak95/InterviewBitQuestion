"""
Length of Longest Subsequence

LEVEL : MEDIUM
Asked In: MICROSOFT

Problem Description

Given an 1D integer array A of length N, find the length of longest subsequence which is first increasing then decreasing.



Problem Constraints
0 <= N <= 3000

 -107 <= A[i] <= 107



Input Format
The first and the only argument contains an integer array A.



Output Format
Return an integer representing the answer as described in the problem statement.



Example Input
Input 1:

 A = [1, 2, 1]
Input 2:

 A = [1, 11, 2, 10, 4, 5, 2, 1]


Example Output
Output 1:

 3
Output 2:

 6


Example Explanation
Explanation 1:

 [1, 2, 1] is the longest subsequence.
Explanation 2:

 [1 2 10 4 2 1] is the longest subsequence.
"""

##### Solution 1 TC = O(n2log(n)) => TLE


# from bisect import bisect_left
# class Solution:
#     # @param A : tuple of integers
#     # @return an integer
#     def longestSubsequenceLength(self, A):
#         def get_max_length(arr, maximum_value):
#             ans = []
#             for x in arr:
#                 if x < maximum_value:
#                     if not ans:
#                         ans.append(x)
#                     elif ans[-1] < x:
#                         ans.append(x)
#                     else:
#                         ans[bisect_left(ans, x)] = x
#             return len(ans)
#
#         def helper(n):
#             ans = 0
#             curr_max = -float("inf")
#             for i in range(1, n + 1):
#                 curr_max = max(curr_max, A[i - 1])
#                 left = A[:i]
#                 right = A[i:]
#                 left_sub = get_max_length(left, float("inf"))
#                 right_sub = get_max_length(right[::-1], curr_max)
#                 ans = max(ans, left_sub + right_sub)
#             return ans
#
#         return helper(len(A))

########################################################################################

from bisect import bisect_left
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestSubsequenceLength(self, A):
        def LIS(arr, dp_arr):
            n = len(arr)
            for i in range(1, n):
                for j in range(0, i):
                    if ((arr[i] > arr[j]) and (dp_arr[i] < dp_arr[j] + 1)):
                        dp_arr[i] = dp_arr[j] + 1
            # ans = []
            # for i, x in enumerate(arr):
            #     if not ans:
            #         ans.append(x)
            #     elif ans[-1] < x:
            #         ans.append(x)
            #     else:
            #         ans[bisect_left(ans, x)] = x
            #     dp_arr[i+1] = len(ans)

        def LDS(arr, dp_arr):
            n = len(arr)
            for i in reversed(range(n - 1)):
                for j in reversed(range(i - 1, n)):
                    if arr[i] > arr[j] and dp_arr[i] < dp_arr[j] + 1:
                        dp_arr[i] = dp_arr[j] + 1
            # ans = []
            # for i,x in enumerate(arr):
            #     if not ans:
            #         ans.append(x)
            #     elif ans[-1] > x:
            #         ans.append(x)
            #     else:
            #         ans[len(ans) - bisect_left(ans[::-1], x) - 1] = x
            #     dp_arr[i+1] = len(ans)

        ####
        n = len(A)+1
        left = [1]*n
        LIS(A, left)

        right = [1]*n
        LDS(A, right)

        # print(left)
        # print(right)
        def helper(n):
            ans = 0
            curr_max = -float("inf")
            for i in range(n + 1):
                left_sub = left[i]
                right_sub = right[i]
                ans = max(ans, left_sub + right_sub-1)
            return ans

        return helper(len(A))




if __name__ == "__main__":
    A = [1]
    print(Solution().longestSubsequenceLength(A))
