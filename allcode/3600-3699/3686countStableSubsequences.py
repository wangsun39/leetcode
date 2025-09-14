# 给你一个整数数组 nums。
#
# 如果一个子序列中不存在连续三个元素奇偶性相同（仅考虑该子序列内），则称该子序列为稳定子序列。
#
# 请返回所有稳定子序列的数量。
#
# 由于结果可能非常大，请将答案对 109 + 7 取余数后返回。
#
# 子序列是一个从数组中通过删除某些元素（或不删除任何元素），并保持剩余元素相对顺序不变的非空数组。
#
#
#
# 示例 1：
#
# 输入： nums = [1,3,5]
#
# 输出： 6
#
# 解释：
#
# 稳定子序列为：[1], [3], [5], [1, 3], [1, 5], 和 [3, 5]。
# 子序列 [1, 3, 5] 不稳定，因为它包含三个连续的奇数。因此答案是 6。
# 示例 2：
#
# 输入： nums = [2,3,4,2]
#
# 输出： 14
#
# 解释：
#
# 唯一一个不稳定子序列是 [2, 4, 2]，因为它包含三个连续的偶数。
# 所有其他子序列都是稳定子序列。因此答案是 14。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105

from leetcode.allcode.competition.mypackage import *


class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        dp = [[0] * 3 for _ in range(n)]  # dp[i][j] 以 nums[i] 结尾，最后连续j个相同奇偶性的序列个数
        dp0 = [[0] * 3 for _ in range(n)]  # dp[i][j] 前i个元素，最后连续j个偶数的序列个数
        dp1 = [[0] * 3 for _ in range(n)]  # dp[i][j] 前i个元素，最后连续j个奇数的序列个数
        dp[0] = [0, 1, 0]
        if nums[0] & 1: dp1[0] = dp[0]
        else: dp0[0] = dp[0]
        for i in range(1, n):
            dp1[i] = dp1[i - 1]
            dp0[i] = dp0[i - 1]
            if nums[i] & 1:
                dp[i][1] = dp0[i - 1][1] + dp0[i - 1][2] + 1
                dp[i][2] = dp1[i - 1][1]
                dp1[i][1] += dp[i][1]
                dp1[i][2] += dp[i][2]
            else:
                dp[i][1] = dp1[i - 1][1] + dp1[i - 1][2] + 1
                dp[i][2] = dp0[i - 1][1]
                dp0[i][1] += dp[i][1]
                dp0[i][2] += dp[i][2]
            for j in range(1, 3):
                dp[i][j] %= MOD
                dp[i][j] %= MOD
                dp1[i][j] %= MOD
                dp1[i][j] %= MOD
                dp0[i][j] %= MOD
                dp0[i][j] %= MOD
        return (sum(dp0[-1]) + sum(dp1[-1])) % MOD


so = Solution()
print(so.countStableSubsequences([1,3,5]))




