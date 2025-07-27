

from leetcode.allcode.competition.mypackage import *

min = lambda a, b: b if b < a else a
max = lambda a, b: b if b > a else a

class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        k = n // 3
        res = 0
        for i in range(k):
            res += nums[n - 2 * (i + 1)]
        return res


so = Solution()
print(so.maximumMedianSum([2,1,3,2,1,3]))
print(so.maximumMedianSum([1,1,10,10,10,10]))




