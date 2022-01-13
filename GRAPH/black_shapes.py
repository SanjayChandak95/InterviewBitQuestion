"""
Black Shapes
Level : Medium
Asked In : Amazon
"""

"""
Given N x M character matrix A of O's and X's, where O = white, X = black.


Return the number of black shapes. A black shape consists of one or more adjacent X's (diagonals not included)




Input Format:

    The First and only argument is a N x M character matrix.
Output Format:

    Return a single integer denoting number of black shapes.
Constraints:

    1 <= N,M <= 1000
    A[i][j] = 'X' or 'O'
Example:

Input 1:
    A = [ OOOXOOO
          OOXXOXO
          OXOOOXO  ]
Output 1:
    3
Explanation:
    3 shapes are  :
    (i)    X
         X X
    (ii)
          X
    (iii)
          X
          X
Note: we are looking for connected shapes here.

XXX
XXX
XXX
is just one single connected black shape.
"""

"""
HINT:
You need to find number of different connected components here. Any graph traversal algorithm can do this.

Solution Approach:
Simple graph traversal approach:

Answer := 0
Loop i = 1 to N :
    Loop j = 1 to M:
          IF MATRIX at i, j equal to 'X' and not visited:
                 BFS/DFS to mark the connected area as visited
                 update Answer
    EndLoop
EndLoop

return Answer
"""

from collections import deque


class Solution:
    # @param A : list of strings
    # @return an integer
    def black(self, A):
        n, m = len(A), len(A[0])
        B = [[0 if A[i][j] == "O" else 1 for j in range(m)] for i in range(n)]
        dirxn = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        count = 0
        q = deque()

        def mark_it(a, b):
            q.append((a, b))
            while q:
                i, j = q.popleft()
                for dx, dy in dirxn:
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < m and B[x][y] == 1:
                        q.append((x, y))
                        B[x][y] = 2

        for i in range(n):
            for j in range(m):
                if B[i][j] == 1:
                    B[i][j] = 2
                    count += 1
                    mark_it(i, j)
        return count
