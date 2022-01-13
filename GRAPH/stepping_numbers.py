"""
Stepping NUmbers
Level : Medium
Asked : Epic System
"""
"""
Problem Description

Given A and B you have to find all stepping numbers in range A to B.

The stepping number:

A number is called as a stepping number if the adjacent digits have a difference of 1.

e.g. 123 is stepping number, but 358 is not a stepping number



Input Format
First argument is an integer A.

Second argument is an integer B.



Output Format
Return a integer array sorted in ascending order denoting the stepping numbers between A and B.



Example Input
Input 1:

 A = 10
 B = 20


Example Output
Output 1:

 [10, 12]


Example Explanation
Explanation 1:

 All stepping numbers are 10 , 12 
"""

"""
Hint:
Assume that we have a graph where the starting node is 0 and we need to traverse it from the start node to all the reachable nodes.

With the restrictions given in the graph about the stepping numbers, what do you think should be the restrictions defining the next transitions in the graph.
"""

class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of integers
    def stepnum(self, A, B):
        ans = set()

        def helper(min_val, max_val, curr_val):

            if min_val <= curr_val <= max_val:
                ans.add(curr_val)
            if curr_val > max_val:
                return

            unit_place = curr_val % 10
            if unit_place != 0:
                helper(min_val, max_val, curr_val * 10 + (unit_place - 1))
            if unit_place != 9:
                helper(min_val, max_val, curr_val * 10 + (unit_place + 1))

        for i in range(10):
            helper(A, B, 0)
        return sorted(list(ans))


if __name__ == "__main__":
    print(Solution().stepnum(0, 89))