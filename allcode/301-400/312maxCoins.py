# 有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
#
# 现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得 nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。 这里的 i - 1 和 i + 1 代表和 i 相邻的两个气球的序号。如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。
#
# 求所能获得硬币的最大数量。
#
#  
#
# 示例 1：
# 输入：nums = [3,1,5,8]
# 输出：167
# 解释：
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
# 示例 2：
#
# 输入：nums = [1,5]
# 输出：10
#  
#
# 提示：
#
# n == nums.length
# 1 <= n <= 500
# 0 <= nums[i] <= 100

from typing import List
from functools import lru_cache

import time
class Solution:
    def maxCoins1(self, nums: List[int]) -> int:  # 性能不够
        @lru_cache(None)
        def helper(nums):
            if nums == (1, 1):
                return 0
            N = len(nums) - 2

            res = 0
            for i in range(1, N + 1):
                seg = nums[:i] + nums[i + 1:]
                res = max(res, helper(seg) + (nums[i - 1] * nums[i] * nums[i + 1]))
            return res

        nums.insert(0, 1)
        nums.append(1)
        return helper(tuple(nums))
    def maxCoins2(self, nums: List[int]) -> int:  # 可以通过
        @lru_cache(None)
        def helper(start, end):
            if start + 1 == end:
                return 0
            res = 0
            for i in range(start + 1, end):
                res = max(res, nums[start] * nums[i] * nums[end] + helper(start, i) + helper(i, end))
            # print(start, end, res)
            return res

        N = len(nums)
        nums.insert(0, 1)
        nums.append(1)
        return helper(0, N + 1)

    def maxCoins(self, nums: List[int]) -> int:
        N = len(nums)
        nums = [1] + nums + [1]
        dp = [[0 for _ in range(N+2)] for _ in range(N+2)]

        for i in range(1, N + 2):
            for j in range(N + 2 - i):
                if i == 1:
                    dp[j][j + i] = 0
                else:
                    res = 0
                    for k in range(1, i):
                        res = max(res, dp[j][j + k] + nums[j] * nums[j + k] * nums[j + i] + dp[j + k][j + i])
                    dp[j][j + i] = res

        print(dp)
        return dp[0][N + 1]



so = Solution()
print(so.maxCoins([3,1,5,8]))
print(so.maxCoins([1,5]))

