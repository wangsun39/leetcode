
from leetcode.allcode.competition.mypackage import *


class Solution:
    def addMinimum(self, word: str) -> int:
        n = len(word)
        s = 1
        for i in range(n - 1):
            if ord(word[i]) >= ord(word[i + 1]):
                s += 1
        return s * 3 - n


so = Solution()
print(so.addMinimum("b"))
print(so.addMinimum("aaa"))
print(so.addMinimum("abc"))




