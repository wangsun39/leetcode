

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
            s = 0
            for j1 in range(x + 1):
                j2 = x - j1
                # for k1 in range(min(j1 + 1, nums[i - 1] - j2 + 1)):
                #     dp[i][j1] += dp[i - 1][k1]
                #     dp[i][j1] %= MOD
                # 将以上循环改成前缀和
                # 新增只考虑 i - 1 项的 arr1[i - 1] == j1 的值，其他值都从前缀和累计
                if nums[i - 1] < j2: continue  # arr2[i - 1] 无法选择
                k1 = min(j1, nums[i - 1] - j2)  # 最新一项的 arr1 的下标
                # kk1 = min(j1 - 1, nums[i - 1] - (x - (j1 - 1)))  # j1 = j1 - 1时，最新一项的 arr1 的下标
                # if k1 != kk1:  # 表示最新的一项是新增的
                #     s += dp[i - 1][k1]
                #     s %= MOD
                # 以上注释的代码，表示此轮循环最新项，在上一轮循环中没有出现才会被加入前缀和
                # 不过由于下面的等式，说明k1在每轮循环中都是递增的，因此不需要判断 k1 != kk1
                # k1 == min(j1, nums[i - 1] - (x - j1)) == min(j1, j1 + nums[i - 1] - x))
                s += dp[i - 1][k1]
                s %= MOD

                dp[i][j1] = s
        # print(dp)
        return sum(dp[-1]) % MOD


so = Solution()
print(so.countOfPairs(nums = [3,21]))
print(so.countOfPairs(nums = [16,5]))
print(so.countOfPairs(nums = [2,3,2]))
print(so.countOfPairs(nums = [5,5,5,5]))




