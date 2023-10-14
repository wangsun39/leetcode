# 给你一个正整数数组 nums 。
#
# 如果数组 nums 的子集中的元素乘积是一个 无平方因子数 ，则认为该子集是一个 无平方 子集。
#
# 无平方因子数 是无法被除 1 之外任何平方数整除的数字。
#
# 返回数组 nums 中 无平方 且 非空 的子集数目。因为答案可能很大，返回对 109 + 7 取余的结果。
#
# nums 的 非空子集 是可以由删除 nums 中一些元素（可以不删除，但不能全部删除）得到的一个数组。如果构成两个子集时选择删除的下标不同，则认为这两个子集不同。
#
#
#
# 示例 1：
#
# 输入：nums = [3,4,4,5]
# 输出：3
# 解释：示例中有 3 个无平方子集：
# - 由第 0 个元素 [3] 组成的子集。其元素的乘积是 3 ，这是一个无平方因子数。
# - 由第 3 个元素 [5] 组成的子集。其元素的乘积是 5 ，这是一个无平方因子数。
# - 由第 0 个和第 3 个元素 [3,5] 组成的子集。其元素的乘积是 15 ，这是一个无平方因子数。
# 可以证明给定数组中不存在超过 3 个无平方子集。
# 示例 2：
#
# 输入：nums = [1]
# 输出：1
# 解释：示例中有 1 个无平方子集：
# - 由第 0 个元素 [1] 组成的子集。其元素的乘积是 1 ，这是一个无平方因子数。
# 可以证明给定数组中不存在超过 1 个无平方子集。
#
#
# 提示：
#
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 30

from leetcode.allcode.competition.mypackage import *

class Solution:

    def squareFreeSubsets(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        primes = [2,3,5,7,11,13,17,19,23,29]
        m = 1024
        nums = [x for x in nums if x % 4 and x % 9 and x % 16 and x % 25]
        # print(nums)
        n = len(nums)
        if n == 0: return 0
        bi = [0] * n
        for i, x in enumerate(nums):
            bb = 0
            for j, p in enumerate(primes):
                if x % p == 0:
                    bb |= (1 << j)
            bi[i] = bb
        # print(bi)
        dp = [[0] * m for _ in range(n)]  # 前 i 个数中，乘积为 j 的子数组数量
        for i in range(n):
            dp[i][bi[i]] = 1
        # print(dp)
        for i in range(1, n):
            for j in range(m):
                dp[i][j] += dp[i - 1][j]
                dp[i][j] %= MOD
            for j in range(m):
                if bi[i] & j == 0:
                    dp[i][bi[i] | j] += dp[i - 1][j]
                    dp[i][bi[i] | j] %= MOD
        ans = 0
        for i in range(m):
            # print(i)
            ans += dp[-1][i]
        return ans % MOD




so = Solution()
print(so.squareFreeSubsets([1,23,25,1,2,1]))  # 31
print(so.squareFreeSubsets([14,5,21,22,20,21,22]))  # 19
print(so.squareFreeSubsets([16,25,4,4,25,16,9,4,4,16,9,4,16,4,9,25,9,4,25,25,25,16,25,9,9,4,25,25,4,16,9,9,16,25,25,25,4,4,4,25,9,9,16,4,4,25,16,16,4,4,9,9,4,16,25,16,25,4,9,25,4,9,25,9,16,4,16,16,9,9,4,9,25,9,9,9,4,16,25,4,25,9,4,25,16,4,25,25,16,16,16,9,16,9,25,25,4,9,4,25]))
print(so.squareFreeSubsets([14,5,21,22,20,21,22,29,25,22,18,13,8,6,2,1,23,25,1,2,1,14,24,1,4,22,12,26,12,12,16,23,14,27,1,14,10,24,25,10,8,8,26,26,10,15,11,3,29,29,19,26,10,5,15,29,15,9,27,20,14,29,22,28,1,4,11,21,30,30,26,19,14,11,29,12,24,18,9,23,15,18,9,11,1,18,8,10,13,3,17,22,1,10,22,11]))
print(so.squareFreeSubsets([3,4,4,5]))
print(so.squareFreeSubsets([1]))




