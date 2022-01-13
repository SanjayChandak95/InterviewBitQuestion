"""
Cycle in Directed Graph
Level: Easy
Asked In: Amazon, Morgan Stanley
"""

"""
Problem Description

Given an directed graph having A nodes. A matrix B of size M x 2 is given which represents the M edges such that there is a edge directed from node B[i][0] to node B[i][1].

Find whether the graph contains a cycle or not, return 1 if cycle is present else return 0.

NOTE:

The cycle must contain atleast two nodes.
There are no self-loops in the graph.
There are no multiple edges between two nodes.
The graph may or may not be connected.
Nodes are numbered from 1 to A.
Your solution will run on multiple test cases. If you are using global variables make sure to clear them.


Problem Constraints
2 <= A <= 105

1 <= M <= min(200000,A(A-1))

1 <= B[i][0], B[i][1] <= A



Input Format
The first argument given is an integer A representing the number of nodes in the graph.

The second argument given a matrix B of size M x 2 which represents the M edges such that there is a edge directed from node B[i][0] to node B[i][1].



Output Format
Return 1 if cycle is present else return 0.



Example Input
Input 1:

 A = 5
 B = [  [1, 2] 
        [4, 1] 
        [2, 4] 
        [3, 4] 
        [5, 2] 
        [1, 3] ]
Input 2:

 A = 5
 B = [  [1, 2]
        [2, 3] 
        [3, 4] 
        [4, 5] ]


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation*
Explanation 1:

 The given graph contain cycle 1 -> 3 -> 4 -> 1 or the cycle 1 -> 2 -> 4 -> 1
Explanation 2:

 The given graph doesn't contain any cycle.
 """

"""
HINT:
There is a cycle in a graph only if there is a back edge present in the graph. A back edge is an edge that is from a node to itself (self-loop) or one of its ancestor in the tree produced by DFS.

Solution Approach:
Approach:
Depth First Traversal can be used to detect a cycle in a Graph.
DFS for a connected graph produces a tree. There is a cycle in a graph only if there is a back edge present in the graph.
A back edge is an edge that is from a node to itself (self-loop) or one of its ancestor in the tree produced by DFS.

For a disconnected graph, Get the DFS forest as output. To detect cycle, check for a cycle in individual trees by checking back edges.

To detect a back edge, keep track of vertices currently in recursion stack of function for DFS traversal.
If a vertex is reached that is already in the recursion stack, then there is a cycle in the tree.
The edge that connects current vertex to the vertex in the recursion stack is a back edge.
Use recStack[] array to keep track of vertices in the recursion stack.

Algorithm:

Create the graph using the given number of edges and vertices.
Create a recursive function that that current index or vertex, visited, and recusrsion stack.
Mark the current node as visited and also mark the index in recursion stack.
Find all the vertices which are not visited and are adjacent to current node. Recursively call the function for those vertices, If the recursive function returns true return true.
If the adjacent vertices are already marked in the recursion stack then return true.
Create a wrapper class, that calls the recursive function for all the vertices and if any function returns true return true. Else if for all vertices the function returns false return false.
Complexity Analysis:

Time Complexity: O(V+E).Time Complexity of this method is same as time complexity of DFS traversal which is O(V+E).
Space Complexity: O(V). To store the visited and recursion stack O(V) space is needed.
"""

import sys

sys.setrecursionlimit(10 ** 6)


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        graph = {i: [] for i in range(1, A + 1)}
        for src, dest in B:
            graph[src].append(dest)
        visited = set()

        def is_cycle_exist(node, visited1):
            if node in visited1:
                return True
            if node not in graph:
                return False
            visited1.add(node)
            visited.add(node)
            for child in graph[node]:
                if is_cycle_exist(child, visited1):
                    return True
            visited1.discard(node)
            return False

        for root in range(1, A + 1):
            if root not in visited and is_cycle_exist(root, set()):
                return 1
        return 0
