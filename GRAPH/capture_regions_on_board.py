"""
Capture Regions on Board
Level : Hard
Asked : GOOGLE
"""
"""
Problem Description

Given a 2D character matrix A of size N x M, containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.



Problem Constraints
1 <= N, M <= 103



Input Format
First and only argument 2D character matrix A of size N X M.



Output Format
Make changes to the the input only as matrix is passed by reference.



Example Input
Input 1:

 A = [  [X, X, X, X],
        [X, O, O, X],
        [X, X, O, X],
        [X, O, X, X]
     ]


Example Output
Output 1:

 A = [  [X, X, X, X],
        [X, X, X, X],
        [X, X, X, X],
        [X, O, X, X]
     ]


Example Explanation
Explanation 1:

 'O' in (4,2) is not surrounded by X from below.
"""

"""
Hint:
Note that all the chunks of O which remain as O are the ones which have at least one O connected to them which is on the boundary. Otherwise they will turn into X.

Think of graph traversal.

Solution Approach:
We already know chunks of O which remain as O are the ones which have at least one O connected to them which is on the boundary.

Use BFS starting from ‘O’s on the boundary and mark them as ‘B’, then iterate over the whole board and mark ‘O’ as ‘X’ and ‘B’ as ‘O’.
"""

from collections import deque


class Solution:
    # @param A : list of list of chars
    def solve(self, A):
        n, m = len(A), len(A[0])
        root = []
        for i in range(n):
            if A[i][0] == "O":
                root.append((i, 0))
            if A[i][m - 1] == "O":
                root.append((i, m - 1))
        for j in range(m):
            if A[0][j] == "O":
                root.append((0, j))
            if A[n - 1][j] == "O":
                root.append((n - 1, j))
        q = deque()
        dxs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        # print(root)
        for x, y in root:
            if A[x][y] == "O":
                q.append((x, y))
                A[x][y] = "W"
                while q:
                    i, j = q.popleft()
                    for dx, dy in dxs:
                        a, b = i + dx, j + dy
                        if 0 <= a < n and 0 <= b < m and A[a][b] == "O":
                            q.append((a, b))
                            A[a][b] = "W"
        # print(A)
        for i in range(n):
            for j in range(m):
                if A[i][j] == "W":
                    A[i][j] = "O"
                elif A[i][j] == "O":
                    A[i][j] = "X"
