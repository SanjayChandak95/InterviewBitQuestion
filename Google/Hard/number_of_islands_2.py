import collections


class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""


class DSU:
    def __init__(self):
        self._segment = {}
        self._size = {}

    def exist(self, cords):
        return cords in self._segment

    def set_segment(self, cords):
        self._segment[cords] = cords
        self._size[cords] = 1

    def find(self, cords):
        if self._segment[cords] == cords:
            return cords
        self._segment[cords] = self.find(self._segment[cords])
        return self._segment[cords]

    def union(self, cords1, cords2):
        cords1 = self.find(cords1)
        cords2 = self.find(cords2)

        if cords1 != cords2:
            if self._size[cords1] < self._size[cords2]:
                cords1, cords2 = cords2, cords1
            self._segment[cords2] = cords1
            self._size[cords2] += self._size[cords1]
            return True
        return False


class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """

    def numIslands2(self, n, m, operators):
        # write your code here
        count = 0
        ans = [0] * len(operators)
        dxs = ((-1, 0), (1, 0), (0, 1), (0, -1))
        dsu = DSU()
        for i, point in enumerate(operators):
            x, y = point.x, point.y
            if dsu.exist((x, y)):
                ans[i] = count
                continue

            dsu.set_segment((x, y))
            count += 1

            for dx, dy in dxs:
                a, b = x + dx, y + dy
                if 0 <= a < n and 0 <= b < m and dsu.exist((a, b)) and dsu.union((x, y), (a, b)):
                    count -= 1
            ans[i] = count
        return ans



#
#
# class Solution:
#     """
#     @param n: An integer
#     @param m: An integer
#     @param operators: an array of point
#     @return: an integer array
#     """
#
#     def numIslands2(self, n, m, operators):
#         # write your code here
#         ans = [0] * len(operators)
#         count = 0
#         q = collections.deque()
#         dxs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
#         id_map = {}
#         island_found = set()
#         for index, operator in enumerate(operators):
#             x, y = operator.x, operator.y
#             if (x,y) in id_map:
#                 ans[index] = count
#                 continue
#             id_map[(x, y)] = n * x + y
#             count += 1
#             q.append((x, y))
#             while q:
#                 i, j = q.pop()
#                 for dx, dy in dxs:
#                     a, b = i + dx, j + dy
#                     if 0 <= a < n and 0 <= b < m and (a, b) in id_map and id_map[(a, b)] != n * x + y:
#                         q.append((a, b))
#                         if id_map[(a, b)] not in island_found:
#                             count -= 1
#                             island_found.add(id_map[(a, b)])
#                         id_map[(a, b)] = n * x + y
#             island_found.clear()
#             ans[index] = count
#         return ans

if __name__ == "__main__":
    n = 4
    m = 5
    A = [Point(i,j) for i , j in ([1, 1], [1, 2], [1, 3], [1, 4])]
    print(Solution().numIslands2(n,m,A))
