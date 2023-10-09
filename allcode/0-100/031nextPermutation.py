from collections import defaultdict
from typing import List
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        eInfo = {}  # idx -> [isValid, maxLen]
        stack = []
        min_valid_idx = 0
        for idx, e in enumerate(s):
            if '(' == e:
                stack.append(idx)
                eInfo[idx] = [1, 0]
            else:
                if len(stack) == 0:
                    for i in range(min_valid_idx, idx):
                        if i in eInfo:
                            eInfo[i][0] = 0  # 前面的isValid置为无效
                    min_valid_idx = idx
                pre = stack.p



so = Solution()
#print(so.findSubstring("barfoothefoobarman", ["foo","bar"]))
print(so.nextPermutation([1,2,3]))
print(so.nextPermutation([1,3,3]))
print(so.nextPermutation([3,3,1]))