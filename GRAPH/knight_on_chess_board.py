"""
Knight On Chess Board
Level : Medium
Asked In : Goldman Sachs, Amazon
"""

"""
Given any source point, (C, D) and destination point, (E, F) on a chess board, we need to find whether Knight can move to the destination or not.
The above figure details the movements for a knight ( 8 possibilities ).
If yes, then what would be the minimum number of steps for the knight to move to the said point.
If knight can not move from the source point to the destination point, then return -1.
Note: A knight cannot go out of the board.

Input Format:

The first argument of input contains an integer A.
The second argument of input contains an integer B.
    => The chessboard is of size A x B.
The third argument of input contains an integer C.
The fourth argument of input contains an integer D.
    => The Knight is initially at position (C, D).
The fifth argument of input contains an integer E.
The sixth argument of input contains an integer F.
    => The Knight wants to reach position (E, F).
Output Format:

If it is possible to reach the destination point, return the minimum number of moves.
Else return -1.
Constraints:

1 <= A, B <= 500
Example

Input 1:
    A = 8
    B = 8
    C = 1
    D = 1
    E = 8
    F = 8
    
Output 1:
    6

Explanation 1:
    The size of the chessboard is 8x8, the knight is initially at (1, 1) and the knight wants to reach position (8, 8).
    The minimum number of moves required for this is 6.
"""

"""
HINT:
Assume this problem as searching in graph where each block of chess board is vertex.
How would you define edges in such a graph ?
When can you travel from vertex i to vertex j ?

Once you have the graph, then it reduces to finding the shortest path in an unweighted graph.
How do you find the shortest path in an unweighted graph ?

Solution Approach:
A knight can move to 8 positions from (x,y). 

(x, y) -> 
    (x + 2, y + 1)  
    (x + 2, y - 1)
    (x - 2, y + 1)
    (x - 2, y - 1)
    (x + 1, y + 2)
    (x + 1, y - 2)
    (x - 1, y + 2)
    (x - 1, y - 2)

Corresponding to the knight's move, we can define edges. 
(x,y) will have an edge to the 8 neighbors defined above. 

To find the shortest path, we just run a plain BFS. 
"""

from collections import deque


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : integer
    # @param F : integer
    # @return an integer
    def knight(self, A, B, C, D, E, F):
        dirxs = [(-2, -1), (-2, 1), (-1, -2), (1, -2), (2, -1), (2, 1), (-1, 2), (1, 2)]
        q = deque()
        visited = set()
        q.append((C, D, 0))
        visited.add((C, D))
        while q:
            x, y, moves = q.popleft()
            if x == E and y == F:
                return moves
            for dx, dy in dirxs:
                i, j = x + dx, y + dy
                if 1 <= i <= A and 1 <= j <= B and (i, j) not in visited:
                    visited.add((i, j))
                    q.append((i, j, moves + 1))
        return -1
