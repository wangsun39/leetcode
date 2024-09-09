# 给你一个整数数组 nums 和一个 非负 整数 k 。如果一个整数序列 seq 满足在范围下标范围 [0, seq.length - 2] 中存在 不超过 k 个下标 i 满足 seq[i] != seq[i + 1] ，那么我们称这个整数序列为 好 序列。
#
# 请你返回 nums 中 好
# 子序列
#  的最长长度
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,1,1,3], k = 2
#
# 输出：4
#
# 解释：
#
# 最长好子序列为 [1,2,1,1,3] 。
#
# 示例 2：
#
# 输入：nums = [1,2,3,4,5,1], k = 0
#
# 输出：2
#
# 解释：
#
# 最长好子序列为 [1,2,3,4,5,1] 。
#
#
#
# 提示：
#
# 1 <= nums.length <= 5 * 103
# 1 <= nums[i] <= 109
# 0 <= k <= min(50, nums.length)

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[0] * (k + 1) for _ in range(n)]  # dp[i][j] 表示以nums[i]结尾的子序列中，相邻元素不相等个数为j的最长序列长度
        z1 = defaultdict(int)  # z1[(x, j)]  表示以x结尾，不相等元素对为j的最长子序列长度
        z2 = [0] * (k + 1)  # z2[j] 表示 不相等元素对为j的，最长子序列长度
        dp[0][0] = 1
        z1[(nums[0], 0)] = z2[0] = 1
        for i in range(1, n):
            x = nums[i]
            dp[i][0] = z1[(x, 0)] = z1[(x, 0)] + 1
            z2_new = z2[:]  # 本轮会更新 z2， 但使用的必须是前一轮的z2
            z2_new[0] = max(z2_new[0], dp[i][0])
            for j in range(1, k + 1):
                v1 = z1[(x, j)] + 1
                v2 = z2[j - 1] + 1
                dp[i][j] = max(v1, v2)
                z1[(x, j)] = max(z1[(x, j)], dp[i][j])
                z2_new[j] = max(z2[j], dp[i][j])
            z2 = z2_new
        # print(dp)
        # print(z1)
        # print(z2)
        return max(z2)

so = Solution()
print(so.maximumLength(nums = [1,2,1,1,3], k = 2))  # 4
print(so.maximumLength(nums = [1,2,3,4,5,1], k = 0))  # 2




