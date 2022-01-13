"""BOOKMARKED"""
"""
Valid Path
Level: Medium
Asked In: Morgan Stanley, Amazon, Codenation, DirectI
"""

"""
There is a rectangle with left bottom as  (0, 0) and right up as (x, y). There are N circles such that their centers are inside the rectangle.

Radius of each circle is R. Now we need to find out if it is possible that we can move from (0, 0) to (x, y) without touching any circle.

Note :  We can move from any cell to any of its 8 adjecent neighbours and we cannot move outside the boundary of the rectangle at any point of time.




Input Format

1st argument given is an Integer x.
2nd argument given is an Integer y.
3rd argument given is an Integer N, number of circles.
4th argument given is an Integer R, radius of each circle.
5th argument given is an Array A of size N, where A[i] = x cordinate of ith circle
6th argument given is an Array B of size N, where B[i] = y cordinate of ith circle
Output Format

Return YES or NO depending on weather it is possible to reach cell (x,y) or not starting from (0,0).
Constraints

0 <= x, y, R <= 100
1 <= N <= 1000
Center of each circle would lie within the grid
For Example

Input:
    x = 2
    y = 3
    N = 1
    R = 1
    A = [2]
    B = [3]
Output:
    NO
   
Explanation:
    There is NO valid path in this case
"""

"""
HINT:
Focus on every single points inside the rectangle. You can’t go to some points which lie inside any of the circle. So basically you know all the points where you can stand at. Can you use this info to figure out a path between origin and destination.

Solution Approach:
Check if (i,j) is a valid point for all 0<=i<=x, 0<=j<=y. By valid point we mean that none of the circle should contain it.
Now you know all the valid point in rectangle. You need to figure out if you can go from (0,0) to (x,y) through valid points. This can be done with any graph traversal algorithms like BFS/DFS.
"""

from collections import deque

a1 = [1, 1, 1, -1, -1, -1, 0, 0]
b1 = [-1, 0, 1, -1, 0, 1, -1, 1]
m1 = [1, 0, 1, -1, -1]
m2 = [1, 1, 0, 0, 1]


class Solution:
    def isValid(self, row, col, x, y):
        return (row >= 0) and (row <= x) and (col >= 0) and (col <= y)


    def BFS(self, mat, i, j, x, y):
        if mat[i][j] != 1 or mat[x][y] != 1:
            return False
        visited = [[False for _ in range(y + 1)] for _ in range(x + 1)]
        visited[i][j] = True
        q = deque()
        s = (i, j)
        q.append(s)
        while q:

            curr = q.popleft()
            pt = curr[:]
            if pt[0] == x and pt[1] == y:
                return True

            for i in range(5):
                row = pt[0] + m1[i]
                col = pt[1] + m2[i]
                if (self.isValid(row, col, x, y) and mat[row][col] == 1 and not visited[row][col]):
                    visited[row][col] = True
                    Adjcell = (row, col)
                    q.append(Adjcell)
        return False


    def solve(self, x, y, n, r, a, b):
        arr = [[1] * (y + 1) for i in range(x + 1)]
        for x1, y1 in zip(a, b):

            s = 1
            if self.isValid(x1, y1, x, y):
                arr[x1][y1] = 0
            for _ in range(r):
                for j in range(8):
                    if self.isValid(x1 + (a1[j] * s), y1 + (b1[j] * s), x, y):
                        arr[x1 + (a1[j] * s)][y1 + (b1[j] * s)] = 0
                s += 1
        '''for i in arr:
            print(i)'''
        if self.BFS(arr, 0, 0, x, y):
            return "YES"
        return "NO"

if __name__ == "__main__":
    A= 7
    B= 91
    C= 8
    D= 7
    E= [1, 7, 1, 7, 1, 5, 1, 6]
    F= [25, 4, 74, 14, 90, 58, 37, 4]
    print(Solution().solve(A,B,C,D,E,F))