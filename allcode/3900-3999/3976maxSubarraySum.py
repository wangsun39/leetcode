# 给你一个整数数组 nums 和一个正整数 k。
#
# 你必须选择 nums 的一个 子数组 并执行以下操作之一：
#
# 将所选子数组中的每个数字乘以 k。
# 将所选子数组中的每个数字除以 k。
# 当正数除以 k 时，除法结果 向下取整。
# 当负数除以 k 时，除法结果 向上取整。
# 返回结果数组中 非空 子数组的 最大 可能和。
#
# 注意，用于执行操作的 子数组 与用于求和的 子数组 可以是 不同 的。
#
# 子数组 是数组中一段连续的 非空 元素序列。
#
#
#
# 示例 1：
#
# 输入： nums = [1,-2,3,4,-5], k = 2
#
# 输出： 14
#
# 解释：
#
# 将子数组 [3, 4] 中的每个数字乘以 2。
# 结果为 nums = [1, -2, 6, 8, -5]。
# 和最大的子数组是 [6, 8]，因此输出为 6 + 8 = 14。
# 示例 2：
#
# 输入： nums = [-5,-4,-3], k = 2
#
# 输出： -1
#
# 解释：
#
# 将子数组 [-3] 中的每个数字除以 2。
# 结果为 nums = [-5, -4, -1]。
# 和最大的子数组是 [-1]，因此输出为 -1。
#
#
# 提示：
#
# 1 <= nums.length <= 105
# -105 <= nums[i] <= 105
# 1 <= k <= 105

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:

        def divk(a):
            if a > 0:
                return a // k
            return -(abs(a)//k)
        n = len(nums)
        # 状态： 0 原始， 1 开始进入选为最终子数组范围， 2 进入*k范围， 3 进入/k 范围
        #       4 离开 *k和/k范围，但在最终子数组范围， 5 离开最终子数组范围
        dp = [[-inf] * 6 for _ in range(n)]  # 第i个数处于j状态时，选择的
        dp[0][1] = nums[0]
        dp[0][2] = nums[0] * k
        dp[0][3] = divk(nums[0])
        for i in range(1, n):
            dp[i][1] = max(nums[i], dp[i - 1][1] + nums[i])
            dp[i][2] = max(nums[i] * k, dp[i - 1][1] + nums[i] * k, dp[i - 1][2] + nums[i] * k)
            dp[i][3] = max(divk(nums[i]), dp[i - 1][1] + divk(nums[i]), dp[i - 1][3] + divk(nums[i]))
            dp[i][4] = max(dp[i - 1][2], dp[i - 1][3], dp[i - 1][4]) + nums[i]
            dp[i][5] = max(dp[i - 1][2], dp[i - 1][3], dp[i - 1][4], dp[i - 1][5])
        return max(dp[-1])




so = Solution()
print(so.maxSubarraySum(nums = [6,-9,3], k = 2))
print(so.maxSubarraySum(nums = [-5,-4,-3], k = 2))
print(so.maxSubarraySum(nums = [1,-2,3,4,-5], k = 2))




