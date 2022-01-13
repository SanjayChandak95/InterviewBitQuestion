"""BOOKMARKED"""
"""
Useful Extra Edges
Level : Hard
Asked In : CureFit, DirectI, Juspay 
"""
"""
Problem Description

Given a graph of A nodes. Also given the weighted edges in the form of array B.

You are also given starting point C and destination point D.

Also given are some extra edges in the form of vector E.

You need to find the length of the shortest path from C to D if you can use maximum one road from the given roads in E.

All roads are one way ie they go from B[i][0] to B[i][1].



Problem Constraints
1 <= A <= 100000

1 <= |B| <= 100000

1 <= C, D <= A

1 <= |E| <= 300

All lengths of the roads lie between 1 and 1000.



Input Format
First argument is the integer A.

Second argument is the vector of vectors B.

Third argument is the integer C.

Fourth argument is the integer D.

Fifth argument is the vector of vectors E.



Output Format
Return -1 if C is not reachable from D. Else return the shortest distance between them.



Example Input
Input 1:

 A = 3
B = [   [1, 2, 1]
        [2, 3, 2]
    ]
C = 1
D = 3
E = [   [1, 3, 2]
    ]
Input 2:

 A = 4
B = [   [1, 2, 1]
        [2, 3, 2]
        [3, 1, 4]
    ]
C = 1
D = 4
E = [   [1, 3, 2]
    ]


Example Output
Output 1:

 2
Output 2:

 -1


Example Explanation
Explanation 1:

 Use the direct edge from 1 to 3. It has shortest path from 1 to 3.
Explanation 2:

 4 cannot be reached from 1.
 """

"""
HINT:
You need to get shortest paths using any one of
the auxillary roads. Can you use dijkstra from C and D
to get some relation with the same?

Solution Approach:
Use dijkstra 2 times. Once with C as origin and another
with D as origin. Now for every node, you have the length of the shortest path from
C and from D. Now you can just iterate over each road and check if this road
helps you decreasing the existing distance between C and D.
whenever you get a better answer, you can update your answer to this
value and keep iterating on the auxillary roads.
"""

# import heapq
#
#
# class Solution:
#     # @param A : integer
#     # @param B : list of list of integers
#     # @param C : integer
#     # @param D : integer
#     # @param E : list of list of integers
#     # @return an integer
#     def solve(self, A, B, C, D, E):
#
#         adj = [[] for _ in range(A)]
#         for l in B:
#             adj[l[0] - 1].append((l[1] - 1, l[2]))
#             adj[l[1] - 1].append((l[0] - 1, l[2]))
#
#         def dijikstra(d, start):
#             h = []
#             h = [(0, start)]
#             d[start] = 0
#             while h:
#                 dis, u = h.pop()
#                 if dis != d[u]:
#                     continue
#                 for v in adj[u]:
#                     if d[v[0]] > d[u] + v[1]:
#                         d[v[0]] = d[u] + v[1]
#                         heapq.heappush(h, (d[v[0]], v[0]))
#
#         ds = [float('inf')] * A
#         de = [float('inf')] * A
#         dijikstra(ds, C - 1)
#         dijikstra(de, D - 1)
#         ans = ds[D - 1]
#         for l in E:
#             if 0 <= l[0] - 1 < A and 0 <= l[1] - 1 < A:
#                 a = ds[l[0] - 1] + de[l[1] - 1] + l[2]
#                 b = ds[l[1] - 1] + de[l[0] - 1] + l[2]
#                 ans = min(a, b, ans)
#         if ans == float('inf'):
#             return -1
#
#         return ans

###################### LightWeight ##########################

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @param D : integer
    # @param E : list of list of integers
    # @return an integer
    def solve(self, A, B, C, D, E):
        import sys
        from collections import defaultdict
        import heapq
        graph = defaultdict(list)
        for edge in B:
            graph[edge[0]].append((edge[1], edge[2]))

        def dijkstra(graph, src, dest):
            distArray = [sys.maxsize] * (A + 1)
            distArray[src] = 0
            queue = [(0, src)]
            heapq.heapify(queue)
            while queue:
                u = heapq.heappop(queue)
                if u[1] == dest:
                    return distArray[u[1]]
                for v in graph[u[1]]:
                    if distArray[v[0]] > distArray[u[1]] + v[1]:
                        distArray[v[0]] = distArray[u[1]] + v[1]
                        heapq.heappush(queue, (distArray[v[0]], v[0]))
            return sys.maxsize

        ans = sys.maxsize
        ans = min(ans, dijkstra(graph, C, D))

        for edge in E:
            graph[edge[0]].append((edge[1], edge[2]))
            graph[edge[1]].append((edge[0], edge[2]))
            ans = min(ans, dijkstra(graph, C, D))
            graph[edge[0]].remove((edge[1], edge[2]))
            graph[edge[1]].remove((edge[0], edge[2]))

        if ans == sys.maxsize:
            return -1
        else:
            return ans