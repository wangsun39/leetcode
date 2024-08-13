# 给你一个长度为 n 的 正 整数数组 nums 。
#
# 如果两个 非负 整数数组 (arr1, arr2) 满足以下条件，我们称它们是 单调 数组对：
#
# 两个数组的长度都是 n 。
# arr1 是单调 非递减 的，换句话说 arr1[0] <= arr1[1] <= ... <= arr1[n - 1] 。
# arr2 是单调 非递增 的，换句话说 arr2[0] >= arr2[1] >= ... >= arr2[n - 1] 。
# 对于所有的 0 <= i <= n - 1 都有 arr1[i] + arr2[i] == nums[i] 。
# 请你返回所有 单调 数组对的数目。
#
# 由于答案可能很大，请你将它对 109 + 7 取余 后返回。
#
#
#
# 示例 1：
#
# 输入：nums = [2,3,2]
#
# 输出：4
#
# 解释：
#
# 单调数组对包括：
#
# ([0, 1, 1], [2, 2, 1])
# ([0, 1, 2], [2, 2, 0])
# ([0, 2, 2], [2, 1, 0])
# ([1, 2, 2], [1, 1, 0])
# 示例 2：
#
# 输入：nums = [5,5,5,5]
#
# 输出：126
#
#
#
# 提示：
#
# 1 <= n == nums.length <= 2000
# 1 <= nums[i] <= 50

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        mx = max(nums)
        dp = [[0] * (mx + 1) for _ in range(n)]  # dp[i][j] 前i项中，满足arr1[i]为j的数量
        for i in range(nums[0] + 1):
            dp[0][i] = 1
        for i, x in enumerate(nums[1:], 1):
            for j1 in range(mx + 1):  # j1: arr1[i] 的值， j2: arr2[i] 的值
                j2 = x - j1
                # for k1 in range(min(j1 + 1, nums[i - 1] - j2 + 1)):
                #     dp[i][j1] += dp[i - 1][k1]
                #     dp[i][j1] %= MOD
                for k1 in range(j1 + 1):  # k1: arr1[i - 1] 的值,  k2: arr2[i - 1] 的值
                    k2 = nums[i - 1] - k1
                    if k2 < j2: continue
                    dp[i][j1] += dp[i - 1][k1]
                    dp[i][j1] %= MOD
        print(dp)
        return sum(dp[-1]) % MOD




so = Solution()
print(so.countOfPairs(nums = [3,21]))
print(so.countOfPairs(nums = [16,5]))
print(so.countOfPairs(nums = [2,3,2]))
print(so.countOfPairs(nums = [5,5,5,5]))




