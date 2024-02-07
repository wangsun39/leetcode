

from leetcode.allcode.competition.mypackage import *

class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        ans = 0
        even = sum(1 for x in range(1, m + 1) if x & 1 == 0)
        odds = sum(1 for x in range(1, m + 1) if x & 1 != 0)
        for i in range(1, n + 1):
            if i & 1:
                ans += even
            else:
                ans += odds
        return ans


so = Solution()
print(so.flowerGame(n = 3, m = 2))
print(so.flowerGame(n = 1, m = 1))




