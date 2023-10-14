
from leetcode.allcode.competition.mypackage import *


class Solution:
    def runeReserve(self, runes: List[int]) -> int:
        runes.sort()
        ans = 0
        cur = 1
        for i, x in enumerate(runes[1:], 1):
            if (x - runes[i - 1]) <= 1:
                cur += 1
                ans = max(ans, cur)
            else:
                cur = 1
        return ans



so = Solution()
print(so.runeReserve([1,3,5,4,1,7]))
print(so.runeReserve([1,1,3,3,2,4]))




