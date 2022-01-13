"""
Delete Edge!
Level : Medium
Asked In : Flipkart
"""

"""
Problem Description

Given a undirected tree with N nodes labeled  from 1 to N.

Each node has a certain weight assigned to it given by an integer array A of size N.

You need to delete an edge in such a way that Product between sum of weight of nodes in one subtree with sum of weight of nodes in other subtree is maximized.

Return this maximum possible product modulo 109 + 7.

NOTE:

The tree is rooted at node labeled with 1.


Problem Constraints
2 <= N <= 105

1 <= A[i] <= 103



Input Format
First argument is an integer array A of size N denoting the weight of each node.

Second argument is a 2-D array B of size (N-1) x 2 denoting the edge of the tree.



Output Format
Return a single integer denoting the maximum product prossible of sum of weights of nodes in the two subtrees formed by deleting an edge with modulo 109 + 7.



Example Input
Input 1:

 A = [10, 5, 12, 6]
 B = [

        [1, 2]
        [1, 4]
        [4, 3]
     ]
Input 2:

 A = [11, 12]
 B = [

        [1, 2]
     ]


Example Output
Output 1:

 270
Output 2:

 132


Example Explanation
Explanation 1:

 Removing edge (1, 4) created two subtrees.
 Subtree-1 contains nodes (1, 2) and Subtree-2 contains nodes (3, 4)
 So product will be = (A[1] + A[2]) * (A[3] + A[4]) = 15 * 18 = 270
Explanation 2:

 Removing edge (1, 2) created two subtrees.
 Subtree-1 contains node (1) and Subtree-2 contains node (3)
 So product will be = (A[1]) * (A[2]) = 11 * 12 = 132
"""

"""
HINT:
If you know the subtree sum at an node then you can get the sum of other tree by subtracting sum of one subtree from the total sum of tree, in this way subtree sum product can be calculated at each node in O(1) time.

use this fact to find a solution to the problem.

Solution Approach:
We can solve this problem using DFS.
One simple solution is to delete each edge one by one and check subtree sum product.
Finally choose the minimum of them. This approach takes quadratic amount of time.


An efficient method can solve this problem in linear time by calculating the sum of both subtrees using total sum of the tree. We can get the sum of other tree by subtracting sum of one subtree from the total sum of tree, in this way subtree sum product can be calculated at each node in O(1) time.
First we calculate the weight of complete tree and then while doing the DFS at each node, we calculate its subtree sum, by using these two values we can calculate subtree sum product and maintain the maximum among all.

"""

from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 6)
MOD = 10 ** 9 + 7


class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return an integer
    def deleteEdge(self, A, B):
        graph = defaultdict(list)
        # weight_subtree = [0] * (len(A))
        for src, dest in B:
            graph[src - 1].append(dest - 1)
            graph[dest - 1].append(src - 1)
        ans = [0]
        max_sum = sum(A)

        def post_order_helper(node, visited):
            subtree_weight = A[node]
            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    subtree_weight += post_order_helper(child, visited)
                    visited.discard(child)
            ans[0] = max(ans[0], (subtree_weight*(max_sum-subtree_weight))%MOD)
            return subtree_weight

        v = set()
        v.add(0)
        post_order_helper(0, v)
        v.discard(0)
        return ans[0] % MOD