import queue
from collections import defaultdict, deque

class Solution:
    def valid(self, w, word):
        diff = 0
        for (x, y) in zip(w, word):
            if x != y: diff += 1

        return True if diff <= 1 else False

    def get_friends(self, word):
        return [w for w in self.wordList if self.valid(w, word)]

    def findLadders(self, beginWord, endWord, wordList):
        self.wordList = wordList + [beginWord]  # NOTE this change!
        q = queue.Queue()
        ans = []
        q.put([beginWord])

        # storing whoose friend is who, at the very start itself
        d = {}
        for word in self.wordList:
            d[word] = self.get_friends(word)  # same as before
        # storing who all we have already accounted for
        seen = set()

        while not q.empty():
            path = q.get()
            word = path[-1]
            seen.add(word)

            if word == endWord:
                # thanks to https://leetcode.com/ngzza/ for simpler and cleaner line of code
                if not ans or len(path) <= len(ans[-1]) :
                    ans.append(path)

                for w in d[word]:
                # the check, which replaces the self.wordList check
                # since the wordList check won't work
                    if w not in seen:
                        q.put(path.copy() + [w])

        return ans
if __name__ == "__main__":
    start = "hit"
    end = "cog"
    dict = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(Solution().findLadders(start,end,dict))