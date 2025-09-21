

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        mn, mx = min(nums), max(nums)
        return k * (mx - mn)


so = Solution()
print(so.removeDigit())




