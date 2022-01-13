class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        # C = [(val,index) for index, val in enumerate(B)]
        # C.sort()

        # for
        ans = []

        def check(src, dest):
            # print("---->", src, dest)
            if not src:
                return dest[:]
            elif len(src) < len(dest):
                return dest[:]
            elif len(src) == len(dest):
                n = len(src)
                for i in range(n):
                    if src[i] < dest[i]:
                        return src[:]
                    if src[i] > dest[i]:
                        return dest[:]
            return src[:]
        DP = [[] for i in range(A+1)]
        for i in range(1, A+1):
            for index, val in enumerate(B):
                if i >= val:
                    # if i == 5:
                    #     print(sorted(DP[i-val]+[index]))
                    DP[i] = check(DP[i], sorted(DP[i-val]+[index]))
        return DP[-1]


if __name__ == "__main__":
    A= 12459686
    B= [2756, 1743, 1627, 1346, 1825]

    print(Solution().solve(A, B))
