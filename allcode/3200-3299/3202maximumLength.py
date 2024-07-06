

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[1] * k for _ in range(n)]  # 以nums[i]结尾，相邻元素和模k为j的序列最大长度
        ans = 1
        for i in range(1, n):
            for t in range(i):
                mod = (nums[i] + nums[t]) % k
                dp[i][mod] = dp[t][mod] + 1
            ans = max(ans, max(dp[i]))
        # print(dp)
        return ans


so = Solution()
print(so.maximumLength(nums = [1,2,3,10,2], k = 6))
print(so.maximumLength(nums = [3,7,6], k = 2))
print(so.maximumLength(nums = [1,2,3,4,5], k = 2))
print(so.maximumLength(nums = [1,4,2,3,1,4], k = 3))




