# 给你一个整数数组 nums 和一个整数 target 。
#
# 向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
#
# 例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
# 返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。
#
#  
#
# 示例 1：
#
# 输入：nums = [1,1,1,1,1], target = 3
# 输出：5
# 解释：一共有 5 种方法让最终目标和为 3 。
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
# 示例 2：
#
# 输入：nums = [1], target = 1
# 输出：1
#  
#
# 提示：
#
# 1 <= nums.length <= 20
# 0 <= nums[i] <= 1000
# 0 <= sum(nums[i]) <= 1000
# -1000 <= target <= 1000



from typing import List
import bisect
class Solution:
    def findTargetSumWays1(self, nums: List[int], target: int) -> int:
        N = len(nums)
        upper = sum(nums[:-1])  # 剩余数的上界
        dp1 = {target: 1}
        dp2 = {}
        for i in range(N - 1, 0, -1):
            for key in dp1:
                if abs(key - nums[i]) <= upper:
                    if key - nums[i] in dp2:
                        dp2[key - nums[i]] += dp1[key]
                    else:
                        dp2[key - nums[i]] = dp1[key]
                if abs(key + nums[i]) <= upper:
                    if key + nums[i] in dp2:
                        dp2[key + nums[i]] += dp1[key]
                    else:
                        dp2[key + nums[i]] = dp1[key]
            upper -= nums[i - 1]
            dp1, dp2 = dp2, {}
            print(dp1)

        res = 0
        if nums[0] in dp1:
            res = dp1[nums[0]]
        if -nums[0] in dp1:
            res += dp1[-nums[0]]
        return res


    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 0-1 背包 20235/20
        s = sum(nums)
        # 目标求 nums 的一个子集，其元素之和为(s + target) // 2
        if (s + target) & 1 or (s + target < 0): return 0
        t = (s + target) // 2
        n = len(nums)
        dp = [[0] * (t + 1) for _ in range(n)]  # dp[i][j] 前 i 个数的所有子集元素和为j的个数
        dp[0][0] = 1
        if nums[0] <= t:
            dp[0][nums[0]] += 1
        for i in range(1, n):
            for j in range(t + 1):
                dp[i][j] += dp[i-1][j]
                x = j + nums[i]
                if x > t: continue
                dp[i][x] += dp[i - 1][j]
        print(dp)
        return dp[-1][t]

so = Solution()
print(so.findTargetSumWays([0,1], 1))   # 256
print(so.findTargetSumWays([0,0,0,0,0,0,0,0,1], 1))   # 256
print(so.findTargetSumWays([1000], 1000))   # 5
print(so.findTargetSumWays([1,1,1,1,1], 3))   # 5
print(so.findTargetSumWays([1], 1))  # 1

