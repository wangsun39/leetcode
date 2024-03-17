

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        pos = []
        for i, x in enumerate(s):
            if x == c:
                pos.append(i)
        m = len(pos)
        return m * (m + 1) // 2


so = Solution()
print(so.countSubstrings(s = "abada", c = "a"))
print(so.countSubstrings(s = "zzz", c = "z"))




