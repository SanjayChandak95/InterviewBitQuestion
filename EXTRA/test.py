class WordGraph:
    def __init__(self, val=None):
        self.val = val
        self.children = {}
        self.end = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = WordGraph()

    def addWord(self, word: str) -> None:
        temp = self.trie
        n = len(word)
        for i, w in enumerate(word):
            c = temp.children[w] = temp.children.get(w, WordGraph(w))
            if i == n - 1:
                c.end = True
            temp = c

    def search(self, word: str) -> bool:
        temp = self.trie
        n = len(word)
        from collections import deque
        q = deque()
        q.append((0, temp))
        ans = False
        while q:
            level, node = q.popleft()
            if word[level] == ".":
                c = node.children.values()
            else:
                c = node.children.get(word[level])
                c = [c] if c else []
            for x in c:
                if level == n - 1:
                    if (x.end == True):
                        return True
                if level+1<n:
                    q.append((level + 1, x))
        return ans

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
if __name__ == "__main__":
    x = WordDictionary()
    x.addWord("bad")
    x.addWord("pad")
    print(x.search("tad"))