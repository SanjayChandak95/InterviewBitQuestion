"""
Word Ladder I
Level : Hard
Asked In : Google, Microsoft, Ebay
"""
"""
Given two words A and B, and a dictionary, C, find the length of shortest transformation sequence from A to B, such that:

You must change exactly one character in every transformation.
Each intermediate word must exist in the dictionary.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.


Input Format:

The first argument of input contains a string, A.
The second argument of input contains a string, B.
The third argument of input contains an array of strings, C.
Output Format:

Return an integer representing the minimum number of steps required to change string A to string B.
Constraints:

1 <= length(A), length(B), length(C[i]) <= 25
1 <= length(C) <= 5e3
Example :

Input 1:
    A = "hit"
    B = "cog"
    C = ["hot", "dot", "dog", "lot", "log"]

Output 1:
    5

Explanation 1:
    "hit" -> "hot" -> "dot" -> "dog" -> "cog"
"""
"""
HINT:
Think in terms of a graph.

When can you do the transition from one word to another ? Does it mean it can indicate a graph edge between those 2 words ? How can this graph help you to achieve the purpose?

Solution Approach:
This is a classic shortest path problem.
Think in terms of a graph. You basically need to add an edge between two words which can be converted into one another. Resulting graph will be unweighted and undirected.
Which graph traversal algorithm can now help you in computing the shortest path in undirected, unweighted graph?
"""

from collections import defaultdict, deque
class Solution:
    # @param A : string
    # @param B : string
    # @param C : list of strings
    # @return an integer
    def solve(self, A, B, C):
        if A== B:
            return 0
        n = len(A)
        graph = defaultdict(list)
        for x in C:
            for i in range(n):
                key = x[:i]+"_"+x[i+1:]
                graph[key].append(x)
        for i in range(n):
            key = B[:i]+"_"+B[i+1:]
            graph[key].append(B)
        q = deque()
        v = set()
        q.append((A,0))
        while q:
            curr, moves = q.popleft()
            if curr == B:
                return moves+1
            for i in range(n):
                key = curr[:i]+"_"+curr[i+1:]
                for x in graph[key]:
                    if x not in v:
                        v.add(x)
                        q.append((x,moves+1))
        return -1
