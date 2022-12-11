# 给你两个长度分别 n 和 m 的整数数组 nums 和 multipliers ，其中 n >= m ，数组下标 从 1 开始 计数。
#
# 初始时，你的分数为 0 。你需要执行恰好 m 步操作。在第 i 步操作（从 1 开始 计数）中，需要：
#
# 选择数组 nums 开头处或者末尾处 的整数 x 。
# 你获得 multipliers[i] * x 分，并累加到你的分数中。
# 将 x 从数组 nums 中移除。
# 在执行 m 步操作后，返回 最大 分数。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3], multipliers = [3,2,1]
# 输出：14
# 解释：一种最优解决方案如下：
# - 选择末尾处的整数 3 ，[1,2,3] ，得 3 * 3 = 9 分，累加到分数中。
# - 选择末尾处的整数 2 ，[1,2] ，得 2 * 2 = 4 分，累加到分数中。
# - 选择末尾处的整数 1 ，[1] ，得 1 * 1 = 1 分，累加到分数中。
# 总分数为 9 + 4 + 1 = 14 。
# 示例 2：
#
# 输入：nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
# 输出：102
# 解释：一种最优解决方案如下：
# - 选择开头处的整数 -5 ，[-5,-3,-3,-2,7,1] ，得 -5 * -10 = 50 分，累加到分数中。
# - 选择开头处的整数 -3 ，[-3,-3,-2,7,1] ，得 -3 * -5 = 15 分，累加到分数中。
# - 选择开头处的整数 -3 ，[-3,-2,7,1] ，得 -3 * 3 = -9 分，累加到分数中。
# - 选择末尾处的整数 1 ，[-2,7,1] ，得 1 * 4 = 4 分，累加到分数中。
# - 选择末尾处的整数 7 ，[-2,7] ，得 7 * 6 = 42 分，累加到分数中。
# 总分数为 50 + 15 - 9 + 4 + 42 = 102 。
#
#
# 提示：
#
# n == nums.length
# m == multipliers.length
# 1 <= m <= 103
# m <= n <= 105
# -1000 <= nums[i], multipliers[i] <= 1000




from typing import List
from functools import cache


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        @cache
        def dfs(i, j):
            # i, j 分别表示当前步骤时，对应nums数组的头尾下标
            # 根据 i 和 j 就能知道是第几步操作，因为 j - i 每步减小 1
            # 第 0 步是 n - 1, 第 1 步是 n - 2...
            # 因此步数 = (n - 1) - (j - i)
            k = n - 1 - (j - i)
            if k > m - 1:
                return 0
            return max(multipliers[k] * nums[i] + dfs(i + 1, j),
                       multipliers[k] * nums[j] + dfs(i, j - 1))
        return dfs(0, n - 1)



so = Solution()
print(so.maximumScore(nums = [1,2,3], multipliers = [3,2,1]))  # 14
print(so.maximumScore(nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]))  # 102



