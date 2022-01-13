# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int, mid=1) -> List[Optional[TreeNode]]:
        if n+1-mid <= 0:
            return [None]

        ans = []
        for i in range(mid, n + 1):
            left = self.generateTrees(i - 1, mid)
            right = self.generateTrees(n, i + 1)
            for left_node in left:
                for right_node in right:
                    node = TreeNode(i)
                    node.left = left_node
                    node.right = right_node
                    ans.append(node)
        return ans

if __name__ == "__main__":
    print(Solution().generateTrees(3))
