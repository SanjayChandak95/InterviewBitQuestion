"""
Russian Doll Envelopes
Algorithms
Hard
Accepted Rate
26%

DescriptionSolutionNotesDiscussLeaderboard
Description
Give a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.
Find the maximum number of nested layers of envelopes.

Example
Example 1:

Input：[[5,4],[6,4],[6,7],[2,3]]
Output：3
Explanation：
the maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
Example 2:

Input：[[4,5],[4,6],[6,7],[2,3],[1,1]]
Output：4
Explanation：
the maximum number of envelopes you can Russian doll is 4 ([1,1] => [2,3] => [4,5] / [4,6] => [6,7]).

"""

import bisect


class Solution:
    """
    @param envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """

    def maxEnvelopes(self, envelopes):
        # write your code here
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        n = len(envelopes)
        dp = []
        ans = 0

        for i, envelope in enumerate(envelopes):
            index = bisect.bisect_left(dp, envelope[1])
            if index == len(dp):
                dp.append(envelope[1])
            else:
                dp[index] = envelope[1]
        return len(dp)
