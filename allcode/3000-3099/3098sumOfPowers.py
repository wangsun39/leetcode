# 给你一个长度为 n 的整数数组 nums 和一个 正 整数 k 。
#
# 一个子序列的 能量 定义为子序列中 任意 两个元素的差值绝对值的 最小值 。
#
# 请你返回 nums 中长度 等于 k 的 所有 子序列的 能量和 。
#
# 由于答案可能会很大，将答案对 109 + 7 取余 后返回。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3,4], k = 3
#
# 输出：4
#
# 解释：
#
# nums 中总共有 4 个长度为 3 的子序列：[1,2,3] ，[1,3,4] ，[1,2,4] 和 [2,3,4] 。能量和为 |2 - 3| + |3 - 4| + |2 - 1| + |3 - 4| = 4 。
#
# 示例 2：
#
# 输入：nums = [2,2], k = 2
#
# 输出：0
#
# 解释：
#
# nums 中唯一一个长度为 2 的子序列是 [2,2] 。能量和为 |2 - 2| = 0 。
#
# 示例 3：
#
# 输入：nums = [4,3,-1], k = 2
#
# 输出：10
#
# 解释：
#
# nums 总共有 3 个长度为 2 的子序列：[4,3] ，[4,-1] 和 [3,-1] 。能量和为 |4 - 3| + |4 - (-1)| + |3 - (-1)| = 10 。
#
#
#
# 提示：
#
# 2 <= n == nums.length <= 50
# -108 <= nums[i] <= 108
# 2 <= k <= n

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
        m = len(delta)
        dp = [[Counter() for _ in range(k)] for _ in range(n)]
        # 每个dp[i][j] 是一个Counter，dp[i][j][t] 表示前i个数中，以i结尾长度为j的子序列中，能量为t的子序列个数
        print(dp)
        for i in range(n):
            for j in range(min(i, k)):  # 对于 i<j, dp[i][j][*]==0
                for kk in range(m - 1, -1, -1):
                    vk = delta[kk]
                    # dp[i][j][vk]

                for u in range(j - 1, i, -1):
                    s = 0
                    x = nums[i] - nums[u]
                    for v in range(m - 1, -1, -1):
                        vv = delta[v]
                        if x > vv:
                            dp[u]
                            s += dp[u][j - 1][v]






so = Solution()
print(so.sumOfPowers(nums = [1,2,3,4], k = 3))




