

from leetcode.allcode.competition.mypackage import *

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        dp = 0
        for i, x in enumerate(nums):
            if x != 0:
                dp = 0
                continue
            dp += 1
            ans += dp
        return ans


so = Solution()
print(so.zeroFilledSubarray([1,3,0,0,2,0,0,4]))




