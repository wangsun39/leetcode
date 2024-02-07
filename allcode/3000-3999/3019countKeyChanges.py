

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countKeyChanges(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i in range(1, n):
            if s[i].upper() != s[i - 1].upper():
                ans += 1
        return ans


so = Solution()
print(so.countKeyChanges("aAbBcC"))
print(so.countKeyChanges("AaAaAaaA"))




