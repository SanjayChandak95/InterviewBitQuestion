"""
Level Order
Level: Easy
Asked In : Facebook, GroupOn, Goldman Sachs
"""

"""
Problem Description

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).



Input Format
First and only argument is root node of the binary tree, A.



Output Format
Return a 2D integer array denoting the zigzag level order traversal of the given binary tree.



Example Input
Input 1:

    3
   / \
  9  20
    /  \
   15   7
Input 2:

   1
  / \
 6   2
    /
   3


Example Output
Output 1:

 [
   [3],
   [9, 20],
   [15, 7]
 ]
Output 2:

 [ 
   [1]
   [6, 2]
   [3]
 ]


Example Explanation
Explanation 1:

 Return the 2D array. Each row denotes the traversal of each level.
 """

"""
HINT:
Can you maintain depth of a node while traversing the tree. How can it help you after the tree traversal?

Solution Approach:
There are 2 ways to solve this problem.

Approach 1: Maintain a vector of size ‘depth’ of the tree. Do any kind of tree traversal keeping track of the current depth. Append the current element to vector[currentDepth]. Since we need stuff left to right, make sure left subtree is visited before the right subtree ( Any of traditional pre/post/inorder traversal should suffice ).

Approach 2: This is important. A lot of times, you’d be asked to do a traditional level order traversal. Or to put in formal words, a traversal where the extra memory used should be proportional to the nodes on a level rather than the depth of the tree. To do that, you need to make sure you are accessing all the nodes on a level before accessing the nodes on next. This is a typical breadth first search problem. Queue FTW.
"""

from collections import defaultdict, deque


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, A):
        ans = defaultdict(list)
        q = deque()

        q.append((A, 0))
        while q:
            temp, level = q.popleft()
            ans[level].append(temp.val)
            if temp.left:
                q.append((temp.left, level + 1))
            if temp.right:
                q.append((temp.right, level + 1))
        return [ans[key] for key in sorted(ans.keys())]
