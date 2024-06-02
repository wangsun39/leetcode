

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumChairs(self, s: str) -> int:
        ans = 0
        cur = 0
        for x in s:
            if x == 'E':
                cur += 1
            else:
                cur -= 1
            ans = max(ans, cur)
        return ans


so = Solution()
print(so.minimumChairs("EEEEEEE"))
print(so.minimumChairs("ELELEEL"))
print(so.minimumChairs("ELEELEELLL"))




