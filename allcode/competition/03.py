

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        mx = max(nums)
        dp = [[0] * (mx + 1) for _ in range(n)]  # dp[i][j] 前i项中，满足arr1[i]为j的数量
        for i in range(nums[0] + 1):
            dp[0][i] = 1
        for i, x in enumerate(nums[1:], 1):
            for j1 in range(mx + 1):  # j1: arr1[i] 的值， j2: arr2[i] 的值
                j2 = x - j1
                # for k1 in range(min(j1 + 1, nums[i - 1] - j2 + 1)):
                #     dp[i][j1] += dp[i - 1][k1]
                #     dp[i][j1] %= MOD
                for k1 in range(j1 + 1):  # k1: arr1[i - 1] 的值,  k2: arr2[i - 1] 的值
                    k2 = nums[i - 1] - k1
                    if k2 < j2: continue
                    dp[i][j1] += dp[i - 1][k1]
                    dp[i][j1] %= MOD
        print(dp)
        return sum(dp[-1]) % MOD




so = Solution()
print(so.countOfPairs(nums = [3,21]))
print(so.countOfPairs(nums = [16,5]))
print(so.countOfPairs(nums = [2,3,2]))
print(so.countOfPairs(nums = [5,5,5,5]))




