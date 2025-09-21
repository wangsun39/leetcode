

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            if (x & 1) == 0:
                ans |= x
        return ans


so = Solution()
print(so.evenNumberBitwiseORs())




