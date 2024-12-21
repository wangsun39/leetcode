# 给你一个整数数组 nums 和一个整数 k 。
#
# 将数组拆分成一些非空子数组。拆分的 代价 是每个子数组中的 重要性 之和。
#
# 令 trimmed(subarray) 作为子数组的一个特征，其中所有仅出现一次的数字将会被移除。
#
# 例如，trimmed([3,1,2,4,3,4]) = [3,4,3,4] 。
# 子数组的 重要性 定义为 k + trimmed(subarray).length 。
#
# 例如，如果一个子数组是 [1,2,3,3,3,4,4] ，trimmed([1,2,3,3,3,4,4]) = [3,3,3,4,4] 。这个子数组的重要性就是 k + 5 。
# 找出并返回拆分 nums 的所有可行方案中的最小代价。
#
# 子数组 是数组的一个连续 非空 元素序列。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,1,2,1,3,3], k = 2
# 输出：8
# 解释：将 nums 拆分成两个子数组：[1,2], [1,2,1,3,3]
# [1,2] 的重要性是 2 + (0) = 2 。
# [1,2,1,3,3] 的重要性是 2 + (2 + 2) = 6 。
# 拆分的代价是 2 + 6 = 8 ，可以证明这是所有可行的拆分方案中的最小代价。
# 示例 2：
#
# 输入：nums = [1,2,1,2,1], k = 2
# 输出：6
# 解释：将 nums 拆分成两个子数组：[1,2], [1,2,1] 。
# [1,2] 的重要性是 2 + (0) = 2 。
# [1,2,1] 的重要性是 2 + (2) = 4 。
# 拆分的代价是 2 + 4 = 6 ，可以证明这是所有可行的拆分方案中的最小代价。
# 示例 3：
#
# 输入：nums = [1,2,1,2,1], k = 5
# 输出：10
# 解释：将 nums 拆分成一个子数组：[1,2,1,2,1].
# [1,2,1,2,1] 的重要性是 5 + (3 + 2) = 10 。
# 拆分的代价是 10 ，可以证明这是所有可行的拆分方案中的最小代价。
#
#
# 提示：
#
# 1 <= nums.length <= 1000
# 0 <= nums[i] < nums.length
# 1 <= k <= 109

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minCost1(self, nums: List[int], k: int) -> int:
        n = len(nums)
        len_trim = [[0] * n for _ in range(n)]
        for i in range(n):
            counter = Counter()
            counter[nums[i]] = 1
            for j in range(i + 1, n):
                len_trim[i][j] = len_trim[i][j - 1]
                counter[nums[j]] += 1
                if counter[nums[j]] == 2:
                    len_trim[i][j] += 2
                elif counter[nums[j]] > 2:
                    len_trim[i][j] += 1
        # print(len_trim)
        @cache
        def dfs(i, j):   # [i, j)
            if i + 1 > j: return 0
            res = inf
            for t in range(i, j):  # [i, t]  (t, j)
                res = min(res, k + len_trim[i][t] + dfs(t + 1, j))
            # print(i, j, res)
            return res
        return dfs(0, n)

    def minCost(self, nums: List[int], k: int) -> int:
        # DP
        n = len(nums)
        dp = [inf] * (n + 1)  # dp[i] 表示 nums[:i] 的最小代价
        dp[0] = 0
        for i in range(1, n + 1):
            counter = Counter()
            s = 0
            for j in range(i - 1, -1, -1):  # 计算 nums[j + 1] ... nums[i] 这段的重要性
                counter[nums[j]] += 1
                if counter[nums[j]] == 2:
                    s += 2
                elif counter[nums[j]] > 2:
                    s += 1
                dp[i] = min(dp[i], dp[j] + k + s)  # dp[i] = min(dp[i], dp[j] + k + 子数组 nums[j: i] 的重要性
        return dp[-1]


so = Solution()
print(so.minCost(nums = [1,2,1,2,1], k = 5))  # 10
print(so.minCost(nums = [1,2,1], k = 2))  #
print(so.minCost(nums = [1,2,1,2,1], k = 2))  # 6
print(so.minCost(nums = [1,2,1,2,1,3,3], k = 2))  # 8




