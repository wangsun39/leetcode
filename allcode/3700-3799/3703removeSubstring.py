

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        stack = []
        ans = []
        for x in s:
            if len(stack) == 0:
                if x == ')':
                    ans.append(x)
                else:
                    stack.append([x, 1])
                continue
            if x == '(':
                if stack[-1][0] == '(':
                    stack.append([x, stack[-1][1] + 1])
                else:
                    stack.append([x, 1])
            else:
                if stack[-1][0] == '(':
                    stack.append([x, 1])
                else:
                    stack.append([x, stack[-1][1] + 1])
                if stack[-1][1] == k:
                    if len(stack) >= k * 2:
                        for _ in range(k * 2):
                            stack.pop()
                    else:
                        for x, _ in stack:
                            ans.append(x)
                        stack = []
        for x, _ in stack:
            ans.append(x)
        return ''.join(ans)


so = Solution()
print(so.removeSubstring(s = "()())", k = 2))
print(so.removeSubstring(s = "()))", k = 2))
print(so.removeSubstring(s = "(())", k = 1))




