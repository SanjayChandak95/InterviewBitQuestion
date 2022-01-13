# we need to find : find(), union(), rank()
# find(a) -> part of which segment
# union(a,b) -> merge a and b to one segment
# rank(a) -> how many values inside segment a

class DSU:
    def __init__(self):
        self._segment = {}
        self.size = {}

    def find(self, a):
        if self._segment[a] == a:
            return a
        self._segment[a] = self.find(self._segment[a])
        return self._segment[a]

    def set_segment(self,a):
        self._segment[a] = a
        self.size[a] = 1

    def union(self, a,b):
        a = self.find(a)
        b = self.find(b)
        if a!=b:
            if self.size[a] < self.size[b]:
                a,b = b,a
            self._segment[b] = a
            self.size[a] += self.size[b]

    def rank(self,a):
        a = self.find(a)
        return self.size[a]


if __name__ == "__main__":
    dsu = DSU()
    dsu.set_segment(1)
    dsu.set_segment(4)
    dsu.set_segment(3)
    dsu.set_segment(9)

    dsu.union(1,4)
    # dsu.union(1,3)
    dsu.union(1,9)
    print("----DSU Find---")
    print(dsu.find(1))
    print(dsu.find(4))
    print(dsu.find(3))
    print(dsu.find(9))
    print("----Rank-----")
    print(dsu.rank(1))
    print(dsu.rank(4))
    print(dsu.rank(3))
    print(dsu.rank(9))