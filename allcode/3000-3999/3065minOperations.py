

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        p = bisect_left(nums, k)
        return p



so = Solution()
print(so.minOperations(nums = [2,11,10,1,3], k = 10))
print(so.minOperations(nums = [1,1,2,4,9], k = 1))
print(so.minOperations(nums = [1,1,2,4,9], k = 9))




