"""
Two teams?
Level : Medium
Asked In : Direct I
"""

"""
Problem Description

There are A people numbered 1 to A in a football academy.

The coach of the academy wants to make two teams (not necessary of equal size) but unfortunately, not all people get along, and several refuse to be put on the same team as that of their enemies.

Given a 2-D array B of size M x 2 denoting the enemies i.e B[i][0] and B[i][1] both are enemies of each other.

Return 1 if it possible to make exactly two teams else return 0.



Problem Constraints
2 <= A <= 105

1 <= M <= 105

1 <= B[i][0], B[i][1] <= A

B[i][0] != B[i][1]



Input Format
First argument is an integer A denoting number of peoples.

Second argument is a 2-D array B of size M x 2 denoting enemies.



Output Format
Return 1 if it possible to make exactly two teams else return 0.



Example Input
Input 1:

 A = 5
 B = [ [1, 2],
       [2, 3],
       [1, 5],
       [2, 4] ] 
Input 2:

 A = 4
 B = [ [1, 4],
       [3, 1],
       [4, 3],
       [2, 1] ]


Example Output
Output 1:

 1 
Output 2:

 0 


Example Explanation
Explanation 1:

 We can make two teams [1, 3, 4] and [2, 5].
Explanation 2:

 No possible way to create two teams. So, we need to return 0.
 """

"""
HINT:
Think of converting the problem into Graph i.e there will be an edge between two enemies.
Is this a problem of Bipartite graph?

Solution Approach:
Create a graph such that there is a edge between each pair of enemies.
We need to find that the above graph is bipartite or not. Check whether the graph is 2-colorable or not
We can do that by running dfs and using an auxilary array col to store the assigned col of the node.
If we can color the graph with two color such that no two enemies have same color then only we can create two teams.
Note: Since the graph can be disconnected so run dfs on each component.
"""

import sys
sys.setrecursionlimit(10**6)
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        players = ["W" for i in range(A+1)]
        graph = {i:[] for i in range(1,A+1)}

        for src, dest in B:
            graph[src].append(dest)
            graph[dest].append(src)
        def possible(node):
            new_team = "R" if players[node] == "B" else "B"
            for child in graph[node]:
                if players[child] != "W":
                    if players[child] == players[node]:
                        return False
                else:
                    players[child] = new_team
                    possible(child)
            return True

        for i in range(1, A+1):
            if players[i] == "W":
                players[i] = "R"
                if not possible(i):
                    return 0
        return 1