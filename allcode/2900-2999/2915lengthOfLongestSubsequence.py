# 给你一个下标从 0 开始的整数数组 nums 和一个整数 target 。
#
# 返回和为 target 的 nums 子序列中，子序列 长度的最大值 。如果不存在和为 target 的子序列，返回 -1 。
#
# 子序列 指的是从原数组中删除一些或者不删除任何元素后，剩余元素保持原来的顺序构成的数组。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3,4,5], target = 9
# 输出：3
# 解释：总共有 3 个子序列的和为 9 ：[4,5] ，[1,3,5] 和 [2,3,4] 。最长的子序列是 [1,3,5] 和 [2,3,4] 。所以答案为 3 。
# 示例 2：
#
# 输入：nums = [4,1,3,2,1,5], target = 7
# 输出：4
# 解释：总共有 5 个子序列的和为 7 ：[4,3] ，[4,1,2] ，[4,2,1] ，[1,1,5] 和 [1,3,2,1] 。最长子序列为 [1,3,2,1] 。所以答案为 4 。
# 示例 3：
#
# 输入：nums = [1,1,5,4,5], target = 3
# 输出：-1
# 解释：无法得到和为 3 的子序列。
#
#
# 提示：
#
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 1000
# 1 <= target <= 1000

from leetcode.allcode.competition.mypackage import *

class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp1 = [0] * (target + 1)  # dp[i][j] 表示前i个数，组成j的最长子序列长度
        if nums[0] < target + 1:
            dp1[nums[0]] = 1
        for i in range(1, n):
            x = nums[i]
            if x < target + 1:
                dp2 = [x for x in dp1]
                dp2[x] = max(dp1[x], 1)
                for j in range(x + 1, target + 1):
                    if dp1[j - x] or j == x:
                        dp2[j] = max(dp1[j], dp1[j - x] + 1)
                dp1 = dp2
        return dp1[-1] if dp1[-1] else -1



so = Solution()
print(so.lengthOfLongestSubsequence(nums = [1,3,3,8], target = 7))
print(so.lengthOfLongestSubsequence(nums = [1,2], target = 10))
print(so.lengthOfLongestSubsequence(nums = [1,2,3,4,5], target = 9))
print(so.lengthOfLongestSubsequence(nums = [4,1,3,2,1,5], target = 7))
print(so.lengthOfLongestSubsequence(nums = [1,1,5,4,5], target = 3))




