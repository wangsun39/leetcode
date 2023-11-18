

from leetcode.allcode.competition.mypackage import *

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        if limit * 3 < n:
            return 0
        ans = 0
        for n1 in range(max(0, n - 2 * limit), min(n + 1, limit + 1)):
            left = n - n1
            lo = max(0, left - limit)
            hi = min(left, limit)
            ans += (hi - lo + 1)
        return ans


so = Solution()
print(so.distributeCandies(n = 5, limit = 2))
print(so.distributeCandies(n = 3, limit = 3))




