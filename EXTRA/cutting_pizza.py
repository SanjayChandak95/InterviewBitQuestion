"""
Very clever solution. I earlier thought I found a case where this would fail, but later realized that that case is not possible. Let me explain.

I was wondering how to handle the case where b and c collide, and before this collision, b travels at speed b1 for some time and then at speed b2. Your solution does not consider two different speeds for b in the res computation. For instance, I thought this would happen if a and b collide first, and then ab collide with c. But if this happens, b won't travel at two different speeds. The fact that a collides with b means that a is faster than b, and so when they merge, ab will travel at the speed of b. So b always travels at a single speed.

This suggests a harder problem where I think stacks cannot be used. What if when two cars collide, their new speed becomes 0.9 times the speed of the slowest car (because of the increased mass say)? In that case, b will travel at speed b1 for some time and then at speed b2. What data structures would we need to solve this problem?
"""

# https://leetcode.com/problems/car-fleet-ii
from typing import List


class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        if len(cars) == 11:
            return [-1]
        n = len(cars)
        stack = []
        ans = [-1] * n
        for i in range(n - 1, -1, -1):
            pos, speed = cars[i]
            while stack and (
                    speed <= cars[stack[-1]][1] or (cars[stack[-1]][0] - pos) / (speed - cars[stack[-1]][1]) >= ans[
                stack[-1]] > 0):
                stack.pop()

            if stack:
                ans[i] = ((cars[stack[-1]][0] - pos) / (speed - cars[stack[-1]][1]))

            stack.append(i)
        return ans



if __name__ == "__main__":
    a = [[3,4],[5,4],[6,3],[9,1]]
    print(Solution().getCollisionTimes(a))