

from leetcode.allcode.competition.mypackage import *

class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n - 1):
            ans += abs(ord(s[i]) - ord(s[i + 1]))
        return ans

so = Solution()
print(so.scoreOfString("hello"))
print(so.scoreOfString("zaz"))




