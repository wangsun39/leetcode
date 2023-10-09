from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens:
            if x.isdigit() or len(x) > 1:
                stack.append(int(x))
                continue
            b = stack.pop()
            a = stack.pop()
            if '+' == x:
                stack.append(a + b)
            elif '-' == x:
                stack.append(a - b)
            elif '*' == x:
                stack.append(a * b)
            else:
                stack.append(int(a / b))
        return stack[0]

so = Solution()
print(so.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
print(so.evalRPN(["2", "1", "+", "3", "*"]))

