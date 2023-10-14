

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1
        def check(a, b):
            sa, sb = sorted(list(str(a)))[-1], sorted(list(str(b)))[-1]
            return sa == sb

        for i in range(n):
            for j in range(i + 1, n):
                if check(nums[i], nums[j]):
                    ans = max(ans, nums[i] + nums[j])
        return ans


so = Solution()
print(so.maxSum([51,71,17,24,42]))
print(so.maxSum(nums = [1,2,3,4]))




