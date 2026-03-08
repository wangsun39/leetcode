# 给你一个整数数组 nums 。
#
# 你的任务是找到 nums 中的 最长 子序列 seq ，这个子序列中相邻元素的 绝对差 构成一个 非递增 整数序列。换句话说，nums 中的序列 seq0, seq1, seq2, ..., seqm 满足 |seq1 - seq0| >= |seq2 - seq1| >= ... >= |seqm - seqm - 1| 。
#
# 请你返回这个子序列的长度。
#
#
#
# 示例 1：
#
# 输入：nums = [16,6,3]
#
# 输出：3
#
# 解释：
#
# 最长子序列是 [16, 6, 3] ，相邻绝对差值为 [10, 3] 。
#
# 示例 2：
#
# 输入：nums = [6,5,3,4,2,1]
#
# 输出：4
#
# 解释：
#
# 最长子序列是 [6, 4, 2, 1] ，相邻绝对差值为 [2, 2, 1] 。
#
# 示例 3：
#
# 输入：nums = [10,20,10,19,10,20]
#
# 输出：5
#
# 解释：
#
# 最长子序列是 [10, 20, 10, 19, 10] ，相邻绝对差值为 [10, 10, 9, 9] 。
#
#
#
# 提示：
#
# 2 <= nums.length <= 104
# 1 <= nums[i] <= 300

from leetcode.allcode.competition.mypackage import *

MAX = lambda a, b: b if b > a else a

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        mn, mx = min(nums), max(nums)
        n = len(nums)
        dp = [[1] * (mx -  mn + 1) for _ in range(n)]  # dp[i][j]: 以nums[i] 结尾，最后一项差值>=j的最长序列长度
        last = {}  # 元素x上一个位置
        ans = 2
        for i, x in enumerate(nums):
            for j in range(mx - mn, -1, -1):  # 倒序枚举
                # dp[i][j] = 1
                if i == 0:
                    continue
                if j < mx - mn:
                    dp[i][j] = dp[i][j + 1]
                y1, y2 = x - j, x + j  # x 的前一个元素有两个可能
                if y1 in last:
                    dp[i][j] = MAX(dp[i][j], dp[last[y1]][j] + 1)
                if y2 in last:
                    dp[i][j] = MAX(dp[i][j], dp[last[y2]][j] + 1)
                ans = MAX(ans, dp[i][j])
            last[x] = i
        print(dp)
        return ans



so = Solution()
print(so.longestSubsequence(nums = [4,4,9,10,7]))  # 3
print(so.longestSubsequence(nums = [10,20,10,19,10,20]))  # 5
print(so.longestSubsequence(nums = [16,6,3]))  # 3




