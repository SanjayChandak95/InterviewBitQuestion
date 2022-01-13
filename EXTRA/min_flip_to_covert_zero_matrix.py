from typing import List

dxs = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def all_zero(arr):
    return all(y == 0 for x in arr for y in x)


def validate_move(x, y, n, m):
    return 0 <= x < n and 0 <= y < m


def flip_adjacent(i, j, n, m, mat):
    mat[i][j] ^= 1
    for dx, dy in dxs:
        a, b = i + dx, j + dy
        if validate_move(a, b, n, m):
            mat[a][b] ^= 1


class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        def helper(x, y):
            if x >= n:
                if all_zero(mat):
                    return 0
                return float("inf")

            ans = float("inf")
            next_x = x if ((y + 1) < m) else x + 1
            next_y = y + 1 if y + 1 < m else 0

            # take it
            # 1. flip
            flip_adjacent(x, y, n, m, mat)
            ans = min(ans, 1 + helper(next_x, next_y))

            # backtrack
            flip_adjacent(x, y, n, m, mat)
            ans = min(ans, helper(next_x, next_y))

            return ans

        res = helper(0, 0)
        return res if res < float("inf") else -1


if __name__ == "__main__":
    input = [
        [[0, 0], [0, 1]],
        [[0]],
        [[1, 1, 1], [1, 0, 1], [0, 0, 0]],
        [[1, 0, 0], [1, 0, 0]]
    ]
    for x in input:
        print(x , Solution().minFlips(x))

"""
# v.add((x, y))
            # if all_zero(mat):
            #     return 0
            # if len(v) == m * n:
            #     return float("inf")
            # ans = float("inf")
            # for i in range(n):
            #     for j in range(m):
            #         if (i, j) not in v:
            #             # take it
            #             # 1. flip
            #             flip_adjacent(i, j, n, m, mat)
            #             ans = min(ans, 1 + helper(i, j, v))
            #
            #             flip_adjacent(i, j, n, m, mat)
            #             # not take it
            #             ans = min(ans, helper(i, j, v))
            # v.remove((x, y))
"""
