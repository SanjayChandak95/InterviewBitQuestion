"""
Path with good nodes!
Level : Easy
Asked In : Tower Research Capital
"""
"""
Problem Description

Given a tree with N nodes labelled from 1 to N.

Each node is either good or bad denoted by binary array A of size N where if A[i] is 1 then ithnode is good else if A[i] is 
0 then ith node is bad.

Also the given tree is rooted at node 1 and you need to tell the number of root to leaf paths in the tree that contain not more than C good nodes.

NOTE:

Each edge in the tree is bi-directional.


Problem Constraints
2 <= N <= 105

A[i] = 0 or A[i] = 1

0 <= C <= N



Input Format
First argument is an binary integer array A of size N.

Second argument is a 2-D array B of size (N-1) x 2 denoting the edge of the tree.

Third argument is an integer C.



Output Format
Return an integer denoting the number of root to leaf paths in the tree that contain not more than C good nodes.



Example Input
Input 1:

 A = [0, 1, 0, 1, 1, 1]
 B = [  [1, 2]
        [1, 5]
        [1, 6]
        [2, 3]
        [2, 4]
     ]
 C = 1


Example Output
Output 1:

 3


Example Explanation
Explanation 1:

 Path (1 - 2 - 3) and (1 - 5) and (1 - 6) are the paths which contain atmost C nodes.
 """

"""
HINT1:
DFS always works in root to leaf direction. So when a DFS completes its execution we can say that we have traversed each and every root to leaf paths in the tree.

Try to use the above fact to find a solution to the problem.

Approach:
You need to find the number of root to leaf paths which contain atmost C good nodes.

So if we start DFS from node 1 and maintain a counter of good nodes seen till now so if we reach a leaf and this count is less than or equal to C then increment the count of paths and go back to previous node.
The point to note here is that in DFS suppose you are at a current node u then the recursion stack contains dfs calls from root to this u so that’s why we can maintain a count of good nodes and while going back we can decrement it simultaneously.

Time Complexity: O(N)
"""


from collections import defaultdict


class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        graph = defaultdict(list)
        for src, dest in B:
            graph[src].append(dest)
            graph[dest].append(src)
        count = [0]
        visited = set()

        def helper(node, good_threshhold, visited):
            if good_threshhold < 0:
                return

            if all([c in visited for c in graph[node]]):
                count[0] += 1
                return

            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    helper(child, good_threshhold - A[child-1], visited)
                    visited.discard(child)
        visited.add(1)
        helper(1, C - A[0], visited)
        return count[0]


if __name__ == "__main__":
    # A = [0, 1, 0, 1, 1, 1]
    # B = [[1, 2],
    #      [1, 5],
    #      [1, 6],
    #      [2, 3],
    #      [2, 4],
    #      ]
    # C = 1
    A = [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1]
    B = [[10, 6],
         [3, 2],
         [12, 7],
         [9, 5],
         [2, 1],
         [8, 3],
         [7, 1],
         [4, 2],
         [6, 3],
         [11, 4],
         [5, 3],
         [13, 11]]
    C = 7
    print(Solution().solve(A,B,C))
