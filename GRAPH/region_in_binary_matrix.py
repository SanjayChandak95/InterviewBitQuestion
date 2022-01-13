"""
Region in BinaryMatrix
Level : Easy
Asked In : Amazon
"""
"""
Problem Description

Given a binary matrix A of size N x M.

 Cells which contain 1 are called filled cell and cell that contain 0 are called empty cell.

Two cells are said to be connected if they are adjacent to each other horizontally, vertically, or diagonally.

If one or more filled cells are also connected, they form a region. Find the length of the largest region.



Problem Constraints
 1 <= N, M <= 102

 A[i][j]=0 or A[i][j]=1



Input Format
First argument is a 2D binary matrix Aof size  N x M.



Output Format
Return a single interger denoting the length of largest region.



Example Input
Input 1:

 A = [  [0, 0, 1, 1, 0]
        [1, 0, 1, 1, 0]
        [0, 1, 0, 0, 0]
        [0, 0, 0, 0, 1]
    ]
Input 2:

 A = [  [1, 1, 1]
        [0, 0, 1]
    ]


Example Output
Output 1:

 6
Output 2:

 4


Example Explanation
Explanation 1:

 The largest region is denoted by red color in the matrix:
    00110
    10110
    01000
    00001
Explanation 2:

 The largest region is:
    111
    001
"""

"""
HINT:
Idea is based on the problem finding number of islands in Boolean 2D-matrix.
Just perform dfs from each unvisited one and count the number of ones which can be visited from here and maintain the maximum.

Solution Approach:
Idea is based on the problem finding number of islands in Boolean 2D-matrix.Just perform dfs from each unvisited one and count the number of ones which can be visited from here and maintain the maximum.
Just perform dfs from each unvisited one and count the number of ones which can be visited from here and maintain the maximum.
A cell in 2D matrix can be connected to at most 8 neighbors. So in DFS, we make recursive calls for 8 neighbors. We keep track of the visited 1’s in every DFS and update maximum length region.
Time complexity: O(N x M)
"""

from collections import deque


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        drxs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        n, m = len(A), len(A[0])

        def isvalid(i, j):
            return 0 <= i < n and 0 <= j < m and A[i][j] == 1

        def mark_pass(i, j):
            q = deque()
            q.append((i, j))
            region = 1
            while q:
                x, y = q.popleft()
                for dx, dy in drxs:
                    if isvalid(x + dx, y + dy):
                        region += 1
                        q.append((x + dx, y + dy))
                        A[x + dx][y + dy] = -1
            return region

        max_segment = 0
        for i in range(n):
            for j in range(m):
                if A[i][j] == 1:
                    A[i][j] = -1
                    max_segment = max(max_segment, mark_pass(i, j))
        return max_segment
