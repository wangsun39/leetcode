# 给你一个长度为 n 下标从 0 开始的整数数组 nums 和一个 正奇数 整数 k 。
#
# x 个子数组的能量值定义为 strength = sum[1] * x - sum[2] * (x - 1) + sum[3] * (x - 2) - sum[4] * (x - 3) + ... + sum[x] * 1 ，其中 sum[i] 是第 i 个子数组的和。更正式的，能量值是满足 1 <= i <= x 的所有 i 对应的 (-1)i+1 * sum[i] * (x - i + 1) 之和。
#
# 你需要在 nums 中选择 k 个 不相交子数组 ，使得 能量值最大 。
#
# 请你返回可以得到的 最大能量值 。
#
# 注意，选出来的所有子数组 不 需要覆盖整个数组。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3,-1,2], k = 3
# 输出：22
# 解释：选择 3 个子数组的最好方式是选择：nums[0..2] ，nums[3..3] 和 nums[4..4] 。能量值为 (1 + 2 + 3) * 3 - (-1) * 2 + 2 * 1 = 22 。
# 示例 2：
#
# 输入：nums = [12,-2,-2,-2,-2], k = 5
# 输出：64
# 解释：唯一一种选 5 个不相交子数组的方案是：nums[0..0] ，nums[1..1] ，nums[2..2] ，nums[3..3] 和 nums[4..4] 。能量值为 12 * 5 - (-2) * 4 + (-2) * 3 - (-2) * 2 + (-2) * 1 = 64 。
# 示例 3：
#
# 输入：nums = [-1,-2,-3], k = 1
# 输出：-1
# 解释：选择 1 个子数组的最优方案是：nums[0..0] 。能量值为 -1 。
#
#
# 提示：
#
# 1 <= n <= 104
# -109 <= nums[i] <= 109
# 1 <= k <= n
# 1 <= n * k <= 106
# k 是奇数。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maximumStrength1(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = list(accumulate(nums, initial=0))
        dp = [[-inf] * k for _ in range(n)]  # dp[i][j]  前i个数，分成j段对应的最大能量值（注意公式中的x恒等于k）
        # i < j 时 dp[i][j] 都为0
        dp[0][0] = nums[0] * k
        for i in range(1, n):
            for j in range(min(i + 1, k)):
                sign = -1 if j & 1 else 1
                dp[i][j] = dp[i - 1][j]
                if j == 0:
                    for L in range(j - 1, i):
                        dp[i][j] = max(dp[i][j], (s[i + 1] - s[L + 1]) * sign * (k - j))
                    continue
                for L in range(j - 1, i):
                    dp[i][j] = max(dp[i][j], dp[L][j - 1] + (s[i + 1] - s[L + 1]) * sign * (k - j))

        print(dp)
        return dp[-1][-1]

    def maximumStrength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = list(accumulate(nums, initial=0))
        dp = [[-inf] * k for _ in range(n)]  # dp[i][j]  前i个数，分成j段对应的最大能量值（注意公式中的x恒等于k）
        # i < j 时 dp[i][j] 都为0
        dp[0][0] = nums[0] * k
        for i in range(1, n):
            mx = -inf
            for j in range(min(i + 1, k)):
                sign = -1 if j & 1 else 1
                dp[i][j] = dp[i - 1][j]
                if j == 0:
                    for L in range(j - 1, i):
                        dp[i][j] = max(dp[i][j], (s[i + 1] - s[L + 1]) * sign * (k - j))
                    continue
                if j == 1:
                    for L in range(j - 1, i):
                        # t = dp[L][j - 1] + (s[i + 1] - s[L + 1]) * sign * (k - j)
                        mx = max(mx, dp[L][j - 1] - s[L + 1] * sign * (k - j))
                    t = mx + s[i + 1] * sign * (k - j)
                    if t > dp[i][j]:
                        dp[i][j] = t
                    continue

                # j > 1:
                L = j - 2
                mx -= dp[L][j - 1] - s[L + 1] * (-sign) * (k - j)
                t = s[i + 1] * sign * (k - j) * (i - j + 1) + mx
                if t > dp[i][j]:
                    dp[i][j] = t

        print(dp)
        return dp[-1][-1]




so = Solution()
print(so.maximumStrength(nums = [1,2,3,-1,2], k = 3))  # 22
print(so.maximumStrength([7,-70,75], 1))   # 75
print(so.maximumStrength(nums = [12,-2,-2,-2,-2], k = 5))  # 64
print(so.maximumStrength([-50,-24], 1))   # -24
print(so.maximumStrength([-99,85], 1))  # 85
print(so.maximumStrength(nums = [-1,-2,-3], k = 1))  # -1




