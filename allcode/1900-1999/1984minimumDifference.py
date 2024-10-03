

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        return min(nums[i + k - 1] - nums[i] for i in range(n - k + 1))



so = Solution()
print(so.minimumDifference(nums = [90], k = 1))




