"""
Largest Distance between nodes of a Tree
Level : Medium
Asked In : Facebook, Google
"""
"""
Problem Description

Given an arbitrary unweighted rooted tree which consists of N nodes.

The goal of the problem is to find largest distance between two nodes in a tree.

Distance between two nodes is a number of edges on a path between the nodes (there will be a unique path between any pair of nodes since it is a tree).

The nodes will be numbered 0 through N - 1.

The tree is given as an array A, there is an edge between nodes A[i] and i (0 <= i < N). Exactly one of the i's will have A[i] equal to -1, it will be root node.



Problem Constraints
1 <= N <= 40000



Input Format
First and only argument is an integer array A of size N.



Output Format
Return a single integer denoting the largest distance between two nodes in a tree.



Example Input
Input 1:

 A = [-1, 0, 0, 0, 3]


Example Output
Output 1:

 3


Example Explanation
Explanation 1:

 node 0 is the root and the whole tree looks like this: 
          0
       /  |  \
      1   2   3
               \
                4

 One of the longest path is 1 -> 0 -> 3 -> 4 and its length is 3, thus the answer is 3.
 """

"""
Hint1:
How would you solve the problem if you knew the longest path certainly goes through root?

Try to generalize this approach for other nodes.

Solution Approach:
1) pick any node u
2) find the node which is farthest from u, call it x (calculate using the same approach as in Solution 1)
3) find the node which is farthest from x, call it q (calculate using the same approach as in Solution 1)
The answer will be the length of a path from x to q.

Proof of correctness:

The crucial step is to prove that x will be one of the endpoints of the path with maximal length (note that there might be more than one such path). If it is, then the longest path from x will be the longest path in the tree.

Let d(v1, v2) be length of path between v1 and v2

Let’s prove it by contradiction: assume there is a strictly longer path between s and t, neither of which is x. Let h be a node which is closest to u among the nodes on a path between s and t. Then there are two cases:
1) h is on path between u and x

    u
    |
    |
    |
    h   x
   / \ /
  /   *
 /     \
s       t 
then d(s, t) = d(s, h) + d(h, t) <= d(s, h) + d(h, x) = d(s, x), which contradicts assumption.

2) h is not on path between u and x

    u
    |
    *---x
    |
    h
   / \
  /   \
 /     \
s       t
then

d(u, s) <= d(u, x) <= d(u, h) + d(h, x)
d(u, t) <= d(u, x) <= d(u, h) + d(h, x)

d(s, t) = d(s, h) + d(h, t)
= d(u, s) + d(u, t) - 2 d(u, h)
<= 2 d(h, x)

2 d(s, t) <= d(s, t) + 2 d(h, x)
= d(s, h) + d(h, x) + d(x, h) + d(h, t)
= d(x, s) + d(x, t)

This means that max(d(v, s), d(v, t)) >= d(s, t), which also contradicts assumption.

Thus, we proved that farthest node of a node will be one of the endpoints of the longest path.
"""

from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 6)


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        graph = defaultdict(list)

        for node, parent in enumerate(A):
            graph[parent].append(node)

        def helper(node):
            if node not in graph:
                # leaf node
                return 1, 1  # curr_path, max_path
            a = []
            for child in graph[node]:
                a.append(helper(child))
            a.sort(reverse=True)
            x = 0
            if len(a) > 0:
                x += a[0][0]
            if len(a) > 1:
                x += a[1][0]
            curr_path = 1 + max([x[0] for x in a])
            max_path = max(curr_path, max([x[1] for x in a]), 1 + x)
            return curr_path, max_path

        return helper(graph[-1][0])[1] - 1


if __name__ == "__main__":
    A = [-1, 0, 0, 1, 2, 1, 5]
    print(Solution().solve(A))
