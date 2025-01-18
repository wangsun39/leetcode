# 给你一个整数数组 nums 和一个 正 整数 k 。
#
# 定义长度为 2 * x 的序列 seq 的 值 为：
#
# (seq[0] OR seq[1] OR ... OR seq[x - 1]) XOR (seq[x] OR seq[x + 1] OR ... OR seq[2 * x - 1]).
# 请你求出 nums 中所有长度为 2 * k 的
# 子序列
#  的 最大值 。
#
#
#
# 示例 1：
#
# 输入：nums = [2,6,7], k = 1
#
# 输出：5
#
# 解释：
#
# 子序列 [2, 7] 的值最大，为 2 XOR 7 = 5 。
#
# 示例 2：
#
# 输入：nums = [4,2,5,6,7], k = 2
#
# 输出：2
#
# 解释：
#
# 子序列 [4, 5, 6, 7] 的值最大，为 (4 OR 5) XOR (6 OR 7) = 2 。
#
#
#
# 提示：
#
# 2 <= nums.length <= 400
# 1 <= nums[i] < 27
# 1 <= k <= nums.length / 2

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        MX = 2 ** 7
        dp1 = [[[0] * MX for _ in range(k)] for _ in range(n)] # dp1[i][j][t] 表示在前i个数中是否存长为j的子序列，or值为t
        dp1[0][0][nums[0]] = 1
        for i in range(1, n):
            x = nums[i]
            dp1[i][0] = dp1[i - 1][0][:]
            dp1[i][0][x] = 1
            for j in range(1, k):
                dp1[i][j] = dp1[i - 1][j][:]
                for t in range(1, MX):
                    if dp1[i - 1][j - 1][t]:
                        tt = t | x  # or 值
                        dp1[i][j][tt] = 1
        dp2 = [[[0] * MX for _ in range(k)] for _ in range(n)] # dp2[i][j][t] 表示在后i个数中是否存长为j的子序列，or值为t
        dp2[n - 1][0][nums[n - 1]] = 1
        for i in range(n - 2, -1, -1):
            x = nums[i]
            dp2[i][0] = dp2[i + 1][0][:]
            dp2[i][0][x] = 1
            for j in range(1, k):
                dp2[i][j] = dp2[i + 1][j][:]
                for t in range(1, MX):
                    if dp2[i + 1][j - 1][t]:
                        tt = t | x  # or 值
                        dp2[i][j][tt] = 1

        ans = 0
        for i in range(n - 1):
            sl = [j for j in range(MX) if dp1[i][-1][j]]
            sr = [j for j in range(MX) if dp2[i + 1][-1][j]]
            for or1 in sl:
                for or2 in sr:
                    ans = max(ans, or1 ^ or2)
        return ans

so = Solution()
print(so.maxValue(nums = [8,114,123,82], k = 1))
print(so.maxValue(nums = [4,2,5,6,7], k = 2))
print(so.maxValue(nums = [2,6,7], k = 1))




