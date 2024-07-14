

from leetcode.allcode.competition.mypackage import *

class Solution:
    def getSmallestString(self, s: str) -> str:
        ans = list(s)
        n = len(s)
        for i in range(n - 1):
            if s[i] > s[i + 1] and (int(s[i]) - int(s[i + 1])) & 1 == 0:
                ans[i], ans[i + 1] = ans[i + 1], ans[i]
                break
        return ''.join(ans)



so = Solution()
print(so.getSmallestString("45320"))
print(so.getSmallestString("001"))
print(so.getSmallestString("45320"))




