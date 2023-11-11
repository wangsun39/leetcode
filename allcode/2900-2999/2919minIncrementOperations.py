

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp1 = max(0, k - nums[2])
        dp2 = max(0, k - nums[1])
        dp3 = max(0, k - nums[0])
        # dp4 = inf if max(nums[:3]) < k else 0
        # ndp1 = ndp2 = ndp3 = ndp4 = 0
        for i in range(3, n):
            x = nums[i]
            if x >= k:
                ndp1, ndp2, ndp3 = min(dp1, dp2, dp3), dp1, dp2
            else:
                ndp1, ndp2, ndp3 = min(dp1, dp2, dp3) + k - x, dp1, dp2
            dp1, dp2, dp3 = ndp1, ndp2, ndp3
            # print(dp1, dp2, dp3)
        return min(dp1, dp2, dp3)


so = Solution()
print(so.minIncrementOperations([4,0,10,2,10,6], 8))
print(so.minIncrementOperations(nums = [2,3,0,0,2], k = 4))
print(so.minIncrementOperations(nums = [0,1,3,3], k = 5))
print(so.minIncrementOperations(nums = [1,1,2], k = 1))




