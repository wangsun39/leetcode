

from leetcode.allcode.competition.mypackage import *

class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        cnt = 0
        for x in nums:
            if x & 1 == 0:
                cnt += 1
        return cnt >= 2


so = Solution()
print(so.hasTrailingZeros([1,2,3,4,5]))
print(so.hasTrailingZeros([2,4,8,16]))
print(so.hasTrailingZeros([1,3,5,7,9]))




