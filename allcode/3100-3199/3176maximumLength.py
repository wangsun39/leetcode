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
# 1 <= nums.length <= 500
# 1 <= nums[i] <= 109
# 0 <= k <= min(nums.length, 25)

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[0] * (k + 1) for _ in range(n)]  # dp[i][j]  表示前i项中，以nums[i]结尾，且相邻两项不等的个数为j的最长子序列长度
        if k > 0:
            dp[0][1] = 1
        dp[0][0] = 1
        ans = 1
        for i in range(1, n):
            for j in range(i + 1):
                if j > k: break
                cur = 0
                if j > 0:
                    for t in range(j - 1, i + 1):
                        if nums[t] != nums[i]:
                            cur = max(cur, dp[t][j - 1] + 1)
                for t in range(j, i + 1):
                    if nums[t] == nums[i]:
                        cur = max(cur, dp[t][j] + 1)
                ans = max(ans, cur)
                dp[i][j] = cur
        return ans



so = Solution()
print(so.maximumLength(nums = [1,2,1,1,3], k = 2))
print(so.maximumLength(nums = [1,2,3,4,5,1], k = 0))




