

from leetcode.allcode.competition.mypackage import *

class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        nums.sort()
        delta = set()
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                delta.add(nums[j] - nums[i])
        delta = list(delta)
        delta.sort()
        dp = [[Counter() for _ in range(k)] for _ in range(n)]
        print(dp)
        for i in range(n):
            for j in range(k):
                for t in range(i - 1):
                    d = nums[i] - nums[t]  # 子序列最后两项之差
                    for u in delta:
                        if d >= u:
                            dp[i][j][u] += dp[i - 1][j - 1][u]
                        else:
                            dp[i][j][d] += dp[i - 1][j - 1][u]



so = Solution()
print(so.sumOfPowers(nums = [1,2,3,4], k = 3))




