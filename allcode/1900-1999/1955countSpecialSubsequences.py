# 特殊序列 是由 正整数 个 0 ，紧接着 正整数 个 1 ，最后 正整数 个 2 组成的序列。
#
# 比方说，[0,1,2] 和 [0,0,1,1,1,2] 是特殊序列。
# 相反，[2,1,0] ，[1] 和 [0,1,2,0] 就不是特殊序列。
# 给你一个数组 nums （仅 包含整数 0，1 和 2），请你返回 不同特殊子序列的数目 。由于答案可能很大，请你将它对 109 + 7 取余 后返回。
#
# 一个数组的 子序列 是从原数组中删除零个或者若干个元素后，剩下元素不改变顺序得到的序列。如果两个子序列的 下标集合 不同，那么这两个子序列是 不同的 。
#
#
#
# 示例 1：
#
# 输入：nums = [0,1,2,2]
# 输出：3
# 解释：特殊子序列为 [0,1,2,2]，[0,1,2,2] 和 [0,1,2,2] 。
# 示例 2：
#
# 输入：nums = [2,2,0,0]
# 输出：0
# 解释：数组 [2,2,0,0] 中没有特殊子序列。
# 示例 3：
#
# 输入：nums = [0,1,2,0,1,2]
# 输出：7
# 解释：特殊子序列包括：
# - [0,1,2,0,1,2]
# - [0,1,2,0,1,2]
# - [0,1,2,0,1,2]
# - [0,1,2,0,1,2]
# - [0,1,2,0,1,2]
# - [0,1,2,0,1,2]
# - [0,1,2,0,1,2]
#
#
# 提示：
#
# 1 <= nums.length <= 105
# 0 <= nums[i] <= 2




from leetcode.allcode.competition.mypackage import *
class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        dp = [0, 0, 0]
        for i, x in enumerate(nums, 1):
            if x == 0:
                dp[0] = (dp[0] * 2 + 1) % MOD
            if x == 1:
                dp[1] *= 2
                dp[1] = (dp[1] + dp[0]) % MOD
            if x == 2:
                dp[2] *= 2
                dp[2] = (dp[1] + dp[2]) % MOD
            # print(dp)
        return dp[2]


so = Solution()
print(so.countSpecialSubsequences([0,1,2,0,1,2]))   # 7
print(so.countSpecialSubsequences([0,1,2,2]))   # 3
print(so.countSpecialSubsequences([2,2,0,0]))   # 0




