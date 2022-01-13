"""
Water Flow
LEVEL : Medium
ASKED: Google
"""
"""
Problem Description

Given an N x M matrix A of non-negative integers representing the height of each unit cell in a continent, the "Blue lake" touches the left and top edges of the matrix and the "Red lake" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the number of cells from where water can flow to both the Blue and Red lake.



Problem Constraints
1 <= M, N <= 1000

1 <= A[i][j] <= 109



Input Format
First and only argument is a 2D matrix A.



Output Format
Return an integer denoting the number of cells from where water can flow to both the Blue and Red lake.



Example Input
Input 1:

 A = [
       [1, 2, 2, 3, 5]
       [3, 2, 3, 4, 4]
       [2, 4, 5, 3, 1]
       [6, 7, 1, 4, 5]
       [5, 1, 1, 2, 4]
     ]
Input 2:

 A = [
       [2, 2]
       [2, 2]
     ]


Example Output
Output 1:

 7
Output 2:

 4


Example Explanation
Explanation 1:

 Blue Lake ~   ~   ~   ~   ~ 
        ~  1   2   2   3  (5) *
        ~  3   2   3  (4) (4) *
        ~  2   4  (5)  3   1  *
        ~ (6) (7)  1   4   5  *
        ~ (5)  1   1   2   4  *
           *   *   *   *   * Red Lake
 Water can flow to both lakes from the cells denoted in parentheses.

Explanation 2:

 Water can flow from all cells.
"""

"""
HINT:
Run bfs twice, one from all the co-ordinates connected to red lake and other from blue lake.

Mark the visited cell and count the cell which are visited in both bfs.

Solution Approach:
Run bfs twice, one from all the co-ordinates connected to red lake and other from blue lake.

Mark the visited cell and count the cell which are visited in both bfs.

Maintain a queue, initially append all the co-ordinates adjacent to blue lake. After that append all the cells adjacent to the current cell and have height >= height of current cell.
Mark the cell blue.
Do similar with cells adjacent to red lake.

Count the cells with both red and blue visited.
"""


from collections import deque


def is_blue_lake_possible(dp, A):
    n, m = len(A), len(A[0])
    visited = set()
    q = deque()
    dirxns = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    for i in range(n):
        q.append((i, 0))
        visited.add((i, 0))
    for j in range(m):
        q.append((0, j))
        visited.add((0, j))
    while q:
        i, j = q.popleft()
        dp[i][j] = True

        for dx, dy in dirxns:
            a, b = i + dx, j + dy
            if (a, b) not in visited and 0 <= a < n and 0 <= b < m and A[i][j] <= A[a][b]:
                visited.add((a, b))
                q.append((a, b))


def is_red_lake_possible(dp, A):
    n, m = len(A), len(A[0])
    visited = set()
    q = deque()
    dirxns = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    for i in range(n):
        q.append((i, m - 1))
        visited.add((i, m - 1))
    for j in range(m):
        q.append((n - 1, j))
        visited.add((n - 1, j))
    while q:
        i, j = q.popleft()
        dp[i][j] = True

        for dx, dy in dirxns:
            a, b = i + dx, j + dy
            if (a, b) not in visited and 0 <= a < n and 0 <= b < m and A[i][j] <= A[a][b]:
                visited.add((a, b))
                q.append((a, b))


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        n, m = len(A), len(A[0])
        blue_lake = [[False for j in range(m)] for i in range(n)]
        is_blue_lake_possible(blue_lake, A)

        red_lake = [[False for j in range(m)] for i in range(n)]
        is_red_lake_possible(red_lake, A)
        return len([True for j in range(m) for i in range(n) if (red_lake[i][j] and blue_lake[i][j])])