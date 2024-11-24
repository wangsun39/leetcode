

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        ans = inf
        for i in range(n):
            if i + l - 1 > n - 1: break
            s = sum(nums[i: i + l])
            if 0 < s < ans:
                ans = s
            for j in range(r - l):
                if i + l + j >= n: break
                s += nums[i + l + j]
                if 0 < s < ans:
                    ans = s
        if ans < inf:
            return ans
        return -1


so = Solution()
print(so.minimumSumSubarray(nums = [-2, 2, -3, 1], l = 2, r = 3))
print(so.minimumSumSubarray(nums = [3, -2, 1, 4], l = 2, r = 3))




