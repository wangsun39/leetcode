from collections import defaultdict
from typing import List
class Solution:
    def longestValidParentheses1(self, s: str) -> int:
        eInfo = {}  # idx -> maxLen
        stack = []
        min_valid_idx = 0
        res = 0
        for idx, e in enumerate(s):
            if '(' == e:
                stack.append(idx)
                eInfo[idx] = 0
            else:
                if 0 == len(stack):
                    for i in range(min_valid_idx, idx):
                        if i in eInfo:
                            del(eInfo[i])  # 前面的isValid置为无效
                    min_valid_idx = idx
                    continue
                pre = stack.pop()
                eInfo[pre] = idx - pre + 1
                res = max(res, eInfo[pre])

                start = max(min_valid_idx, stack[-1]+1) if len(stack) > 0 else min_valid_idx
                for i in range(start, pre+1):
                    if i in eInfo:
                        eInfo[i] = idx - i + 1  # 更新maxLen, 仅更新最前一个下标的
                        res = max(res, eInfo[i])
                        break
        return res

    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        res = 0
        for idx, e in enumerate(s):
            if '(' == e:
                stack.append(idx)
            else:
                stack.pop()
                if 0 == len(stack):
                    stack.append(idx)
                else:
                    res = max(res, idx - stack[-1])
        return res


so = Solution()
#print(so.findSubstring("barfoothefoobarman", ["foo","bar"]))
print(so.longestValidParentheses('(()'))
print(so.longestValidParentheses(")()())"))


