

from leetcode.allcode.competition.mypackage import *

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n - 1):
            if (nums[i] + nums[i + 1]) & 1:
                continue
            else:
                return False
        return True


so = Solution()
print(so.isArraySpecial([1]))
print(so.isArraySpecial( [2,1,4]))
print(so.isArraySpecial([4,3,1,6]))




