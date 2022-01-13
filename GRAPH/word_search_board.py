"""
Word Search Board
Level: Hard
Asked In: Epic System, Amazon
"""

"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The cell itself does not count as an adjacent cell. 

The same letter cell may be used more than once.

Example :

Given board =

[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
word = "ABCCED", -> returns 1,
word = "SEE", -> returns 1,
word = "ABCB", -> returns 1,
word = "ABFSAB" -> returns 1
word = "ABCD" -> returns 0
Note that 1 corresponds to true, and 0 corresponds to false.
"""

"""
Hint1:
Think recursively.

Say the given word is [1…..N]. If you can match [2…..N] starting at every position of board how it can help you to compute the current answers for every position.

Solution Approach:
Lets look at the bruteforce approach.
You iterate over every cell of the matrix to explore if it could be the starting point. Then for every neighboring character which has the same character as the next character in the string, we explore if rest of the string can be formed using that neighbor cell as the starting point.

To sum it up,
exist(board, word, i , j) is true if for any neighbor (k,l) of (i,j)
exist(board, word[1:], k, l) is true

Now note that we could memoize the answer for exist(board, word suffix length, i, j).
"""


# DFS
def is_exist(x, y, curr_index, A, B, visited):
    n, m = len(A), len(A[0])
    k = len(B)
    if curr_index == k - 1:
        return True
    ans = False
    visited.add((x, y))
    dxns = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for dx, dy in dxns:
        i, j = x + dx, y + dy
        if 0 <= i < n and 0 <= j < m and A[i][j] == B[curr_index + 1] and A[i][j] not in visited:
            if is_exist(i, j, curr_index + 1, A, B, visited):
                return True
    return ans


class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    def exist(self, A, B):
        root = []

        n, m = len(A), len(A[0])
        for i in range(n):
            for j in range(m):
                if A[i][j] == B[0]:
                    root.append((i, j))

        for x, y in root:
            if is_exist(x, y, 0, A, B, set()):
                return 1
        return 0
