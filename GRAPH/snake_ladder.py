"""
Snake Ladder Problem!
Level : Medium
Asked In : Amazon
"""

"""
Problem Description

Rishabh takes out his Snakes and Ladders Game, stares the board and wonders: "If I can always roll the die to whatever number I want, what would be the least number of rolls to reach the destination?"

RULES:

The game is played with cubic dice of 6 faces numbered from 1 to A.
Starting from 1 , land on square 100 with the exact roll of the die. If moving the number rolled would place the player beyond square 100, no move is made.
If a player lands at the base of a ladder, the player must climb the ladder. Ladders go up only.
If a player lands at the mouth of a snake, the player must go down the snake and come out through the tail. Snakes go down only.
BOARD DESCRIPTION:

The board is always 10 x 10 with squares numbered from 1 to 100.
The board contains N ladders given in a form of 2D matrix A of size N * 2 where (A[i][0], A[i][1]) denotes a ladder that has its base on square A[i][0] and end at square A[i][1].
The board contains M snakes given in a form of 2D matrix B of size M * 2 where (B[i][0], B[i][1]) denotes a snake that has its mouth on square B[i][0] and tail at square B[i][1].


Problem Constraints
1 <= N, M <= 15

1 <= A[i][0], A[i][1], B[i][0], B[i][1] <= 100

A[i][0] < A[i][1] and B[i][0] > B[i][1]

Neither square 1 nor square 100 will be the starting point of a ladder or snake.

A square will have at most one endpoint from either a snake or a ladder.



Input Format
First argument is a 2D matrix A of size N * 2 where (A[i][0], A[i][1]) denotes a ladder that has its base on square A[i][0] and end at square A[i][1].

Second argument is a 2D matrix B of size M * 2 where (B[i][0], B[i][1]) denotes a snake that has its mouth on square B[i][0] and tail at square B[i][1].



Output Format
Return the least number of rolls to move from start to finish on a separate line. If there is no solution, return -1.



Example Input
Input 1:

 A = [  [32, 62]
        [42, 68]
        [12, 98]
     ]
 B = [  [95, 13]
        [97, 25]
        [93, 37]
        [79, 27]
        [75, 19]
        [49, 47]
        [67, 17]
Input 2:

 A = [  [8, 52]
        [6, 80]
        [26, 42]
        [2, 72]
     ]
 B = [  [51, 19]
        [39, 11]
        [37, 29]
        [81, 3]
        [59, 5]
        [79, 23]
        [53, 7]
        [43, 33]
        [77, 21] 


Example Output
Output 1:

 3
Output 2:

 5


Example Explanation
Explanation 1:

 The player can roll a 5 and a 6 to land at square 12. There is a ladder to square 98. A roll of 2 ends the traverse in 3 rolls.


Explanation 2:

 The player first rolls 5 and climbs the ladder to square 80. Three rolls of 6 get to square 98.
 A final roll of 2 lands on the target square in 5 total rolls.
 """

"""
HINT:
Let’s model the board as a graph.
Every square on the board is a node.
The source node is square 1.
The destination node is square 100.
From every square, it is possible to reach any of the 6 squares in front of it in one move.
So every square has a directed edge to the 6 squares in front of it.

Solution Approach:
Let’s model the board as a graph. Every square on the board is a node. The source node is square 1. The destination node is square 100. From every square, it is possible to reach any of the 6 squares in front of it in one move. So every square has a directed edge to the 6 squares in front of it.

For a snake starting at square i and finishing at j, we can consider that there is no node with index i in the graph. Because
reaching node i is equivalent to reaching node j since the snake at node i will immediately take us down to node j. The same
analogy goes for ladders too. To handle the snakes and ladders, let’s keep an array go_immediately_to[] and initialize it like
this.

 if(no snake or ladder starts at node i)
            go_immediately_to[i] = i.
 else
            j = ending node of the snake or the ladder starting at node i.
            go_immediately_to[i] = j.
Now let’s run a standard Breadth First Search(BFS). Whenever we reach a node i, we will consider that we have reached the node go_immediately_to[] and then continue with the BFS as usual. The distance of the destination is the solution to the problem.

Time Complexity:
The size of the board is always 10 x 10. You can consider time complexity of each BFS is constant as the number of snakes or ladders won’t have much effect.
"""

from collections import deque


class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return an integer
    def snakeLadder(self, A, B):
        q = deque()
        visited = set()
        graph = {}

        for src, dest in A:
            graph[src] = dest
        for src, dest in B:
            graph[src] = dest

        dirxs = [1, 2, 3, 4, 5, 6]
        q.append((1, 0))  # node, total_moves
        visited.add(1)
        while q:
            x, moves = q.popleft()
            if x == 100:
                print(x, q)
                return moves
            for dx in dirxs:
                new_x = graph.get(x + dx, x + dx)
                if new_x <= 100 and new_x not in visited:
                    visited.add(new_x)
                    q.append((new_x, moves + 1))
        return -1
