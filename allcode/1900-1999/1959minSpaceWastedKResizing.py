# 你正在设计一个动态数组。给你一个下标从 0 开始的整数数组 nums ，其中 nums[i] 是 i 时刻数组中的元素数目。除此以外，你还有一个整数 k ，表示你可以 调整 数组大小的 最多 次数（每次都可以调整成 任意 大小）。
#
# t 时刻数组的大小 sizet 必须大于等于 nums[t] ，因为数组需要有足够的空间容纳所有元素。t 时刻 浪费的空间 为 sizet - nums[t] ，总 浪费空间为满足 0 <= t < nums.length 的每一个时刻 t 浪费的空间 之和 。
#
# 在调整数组大小不超过 k 次的前提下，请你返回 最小总浪费空间 。
#
# 注意：数组最开始时可以为 任意大小 ，且 不计入 调整大小的操作次数。
#
#
#
# 示例 1：
#
# 输入：nums = [10,20], k = 0
# 输出：10
# 解释：size = [20,20].
# 我们可以让数组初始大小为 20 。
# 总浪费空间为 (20 - 10) + (20 - 20) = 10 。
# 示例 2：
#
# 输入：nums = [10,20,30], k = 1
# 输出：10
# 解释：size = [20,20,30].
# 我们可以让数组初始大小为 20 ，然后时刻 2 调整大小为 30 。
# 总浪费空间为 (20 - 10) + (20 - 20) + (30 - 30) = 10 。
# 示例 3：
#
# 输入：nums = [10,20,15,30,20], k = 2
# 输出：15
# 解释：size = [10,20,20,30,30].
# 我们可以让数组初始大小为 10 ，时刻 1 调整大小为 20 ，时刻 3 调整大小为 30 。
# 总浪费空间为 (10 - 10) + (20 - 20) + (20 - 15) + (30 - 30) + (30 - 20) = 15 。
#
#
# 提示：
#
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 106
# 0 <= k <= nums.length - 1


from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a

class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # s = list(set(nums))
        # s.sort()
        # map = {x: i for i, x in enumerate(s)}
        # nums = [map[x] for x in nums]  # 离散化
        # m = len(s)
        # dp = [[[inf] * m for _ in range(k + 1)] for _ in range(n + 1)]  # dp[i][j][t]  前i项，调整j次，最终值为t的最小浪费空间

        dp = [[inf] * (k + 1) for _ in range(n)]  # 前i项，调整j次的最小浪费空间
        s = list(accumulate(nums, initial=0))
        # mn[i][j]  区间[i, j] 作为一段时，最小浪费空间
        mn = [[inf] * n for _ in range(n)]
        for i in range(n):  # 预处理 mn
            mx = nums[i]
            for j in range(i, n):
                mx = max(mx, nums[j])
                mn[i][j] = mx * (j - i + 1) - (s[j + 1] - s[i])
        for i in range(n):
            dp[i][0] = mn[0][i]

        for i in range(n):
            for j in range(1, k + 1):
                for t in range(i - 1, -1, -1):
                    # 枚举最后一段是 [t + 1, i]
                    if t + 1 < j - 1: break
                    dp[i][j] = MIN(dp[i][j], dp[t][j - 1] + mn[t + 1][i])
        return min(dp[-1])


so = Solution()
print(so.minSpaceWastedKResizing(nums = [10,20,15,30,20], k = 2))
print(so.minSpaceWastedKResizing(nums = [2,48,18,16,15,9,48,7,44,48], k = 1))
print(so.minSpaceWastedKResizing(nums = [10,20,30], k = 1))
print(so.minSpaceWastedKResizing(nums = [10,20], k = 0))



