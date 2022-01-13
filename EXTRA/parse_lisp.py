import collections


def operatin_and_activate(activate, op):
    if op == "let":
        activate[0] = True
        return True
    elif op == "add":
        activate[1] = True
        return True
    elif op == "mult":
        activate[2] = True
        return True
    return False


def do_op(stack, activate, heap, op):
    if activate[0]:
        if stack:
            heap[stack.pop()] = int(op)
        else:
            stack.append(op)
    elif activate[1]:
        if stack:
            stack.append(stack.pop() + heap[op])
        else:
            stack.append(heap[op])
    elif activate[2]:
        if stack:
            stack.append(stack.pop() * heap[op])
        else:
            stack.append(heap[op])


class Solution:
    def evaluate(self, expression: str, heap: dict = dict()) -> int:
        i = 0
        n = len(expression)
        stack = collections.deque()
        activate = [False, False, False]
        while i < n:
            if expression[i] == "(":
                open_brac = 1
                j = i + 1
                while j < n and open_brac != 0:
                    if expression[i] == "(":
                        open_brac += 1
                    elif expression[i] == ")":
                        open_brac -= 1
                    j += 1
                ans = self.evaluate(expression[i + 1:j - 1], heap.copy())
                do_op(stack, activate, heap, ans)
                i = j - 1

            j = i
            while j < n and expression[j] not in  (" ",")"):
                j += 1

            op = expression[i:j]
            i = j
            if not operatin_and_activate(activate, op):
                do_op(stack, activate, heap, op)
            i += 1
        return stack[-1]



if __name__ == "__main__":
    expression = "(let x 2 (mult x (let x 3 y 4 (add x y))))"
    print(Solution().evaluate(expression))