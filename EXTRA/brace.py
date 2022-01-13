import collections
import itertools
from typing import List


class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        final_set = set()
        stacks = [[]]
        n = len(expression)
        i=0
        while i<n:
            char = expression[i]
            if char == "{":
                open_brac = 1
                j=i+1
                while j<n and open_brac != 0:
                    if expression[j] == "{":
                        open_brac += 1
                    elif expression[j] == "}":
                        open_brac -= 1
                    j+=1
                stacks[-1].append(self.braceExpansionII(expression[i+1:j-1]))
                i = j-1
            elif char == ",":
                stacks.append([])
            else:
                stacks[-1].append(char)
            i+=1

        for stack in stacks:
            final_set |= set(map(''.join, itertools.product(*stack)))
        return sorted(final_set)


if __name__ == "__main__":
    exp = "{a,b}{c,{d,e}}"
    print(f"input : {exp}")
    print(Solution().braceExpansionII(exp))

    # exp = "{{a,z},a{b,c},{ab,z}}"
    # print(f"input : {exp}")
    # print(Solution().braceExpansionII(exp))
