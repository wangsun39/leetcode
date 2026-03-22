

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

class Solution:
    def minRemovals(self, nums: List[int], target: int) -> int:
        n = len(nums)
        m = 1 << 14
        dp = [-inf] * m
        dp[0] = 0

        for a in nums:
            new_dp = dp[:]
            for x in range(m):
                if dp[x] != -inf:
                    if dp[x] + 1 > new_dp[x ^ a]:
                        new_dp[x ^ a] = dp[x] + 1
            dp = new_dp

        kept = dp[target]
        if kept < 0:
            return -1
        return n - kept



so = Solution()
print(so.minRemovals())




