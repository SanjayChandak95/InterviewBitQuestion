"""
 Bomb Enemy
 Level : Medium
"""
import collections

"""
Description
Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.

You can only put the bomb at an empty cell.

Example
Example1

Input:
grid =[
     "0E00",
     "E0WE",
     "0E00"
]
Output: 3
Explanation:
Placing a bomb at (1,1) kills 3 enemies
Example2

Input:
grid =[
     "0E00",
     "EEWE",
     "0E00"
]
Output: 2
Explanation:
Placing a bomb at (0,0) or (0,3) or (2,0) or (2,3) kills 2 enemies
"""


class Solution:
    """
    @param grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
    @return: an integer, the maximum enemies you can kill using one bomb
    """

    def maxKilledEnemies(self, grid):
        # write your code here
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        if m == 0:
            return 0
        bomb_array = [[0 for j in range(m)] for i in range(n)]
        curr_enemy = 0
        ans = 0
        stack = collections.deque()
        for i in range(n):
            for j in range(m):
                curr_enemy += (grid[i][j] == "E")
                if grid[i][j] == "0":
                    stack.append(j)
                if grid[i][j] == "W" or j == m - 1:
                    while stack:
                        x = stack.pop()
                        bomb_array[i][x] += curr_enemy
                        ans = max(ans, bomb_array[i][x])
                    curr_enemy = 0

        for j in range(m):
            for i in range(n):
                curr_enemy += (grid[i][j] == "E")
                if grid[i][j] == "0":
                    stack.append(i)

                if grid[i][j] == "W" or i == n - 1:
                    while stack:
                        x = stack.pop()
                        bomb_array[x][j] += curr_enemy
                        ans = max(ans, bomb_array[x][j])
                    curr_enemy = 0

        return ans
