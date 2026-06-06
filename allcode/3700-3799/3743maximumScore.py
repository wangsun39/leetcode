# 给你一个 循环 数组 nums 和一个整数 k。
#
# 将 nums 划分 为 最多 k 个子数组。由于 nums 是循环数组，这些子数组可以从数组末尾环绕回起点。
#
# 子数组的 范围 定义为其 最大值 与 最小值 的差值。划分的 得分 是所有子数组范围的总和。
#
# 返回所有循环划分方案中可能获得的 最大得分 。
#
# 子数组 是数组中的一个连续非空的元素序列。
#
#
#
# 示例 1：
#
# 输入： nums = [1,2,3,3], k = 2
#
# 输出： 3
#
# 解释：
#
# 将 nums 划分为 [2, 3] 和 [3, 1]（环绕）。
# [2, 3] 的范围是 max(2, 3) - min(2, 3) = 3 - 2 = 1。
# [3, 1] 的范围是 max(3, 1) - min(3, 1) = 3 - 1 = 2。
# 总得分为 1 + 2 = 3。
# 示例 2：
#
# 输入： nums = [1,2,3,3], k = 1
#
# 输出： 2
#
# 解释：
#
# 将 nums 划分为 [1, 2, 3, 3]。
# [1, 2, 3, 3] 的范围是 max(1, 2, 3, 3) - min(1, 2, 3, 3) = 3 - 1 = 2。
# 总得分为 2。
# 示例 3：
#
# 输入： nums = [1,2,3,3], k = 4
#
# 输出： 3
#
# 解释：
#
# 与示例 1 相同，将 nums 划分为 [2, 3] 和 [3, 1]。注意，可以将 nums 划分为少于 k 个子数组。
#
#
#
# 提示：
#
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 109
# 1 <= k <= nums.length

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # def calc(arr):
        #     # 计算非循环数组 arr ，在题目意义下的最大值结果
        #     @cache
        #     def dfs(i, j, st):  # 前i个数，分成 j 段，当前状态为 st 时的最大值收益
        #         # st: 0 为未持有股票，1 为持有股票，2 为做空
        #         if i == -1:
        #             if st == 0: return 0
        #             return -inf
        #         if j < 0:
        #             return -inf
        #         res = dfs(i - 1, j, st)
        #         if st == 0:
        #             res = MAX(res, dfs(i - 1, j - 1, 1) + arr[i])
        #             res = MAX(res, dfs(i - 1, j - 1, 2) - arr[i])
        #         elif st == 1:
        #             res = MAX(res, dfs(i - 1, j, 0) - arr[i])
        #         else:
        #             res = MAX(res, dfs(i - 1, j, 0) + arr[i])
        #         # print(i, j, st, res)
        #         return res
        #
        #     # print(arr)
        #     ans = dfs(n - 1, k, 0)
        #     dfs.cache_clear()
        #     return ans
        def calc(arr):
            # 计算非循环数组 arr ，在题目意义下的最大值结果
            # 前i个数，分成 j 段，当前状态为 st 时的最大值收益
            # st: 0 为未持有股票，1 为持有股票，2 为做空
            dp = [[[-inf] * 3 for _ in range(k + 1)] for _ in range(n)]
            dp[0][0][1] = -arr[0]
            dp[0][0][2] = arr[0]
            for i in range(1, n):
                for j in range(k + 1):
                    if (i + 1) * 2 < j: break
                    dp[i][j] = dp[i - 1][j][:]
                    if j > 0:
                        dp[i][j][0] = MAX(dp[i][j][0], dp[i - 1][j - 1][1] + arr[i])
                        dp[i][j][0] = MAX(dp[i][j][0], dp[i - 1][j - 1][2] - arr[i])
                    else:
                        dp[i][j][2] = MAX(dp[i][j][2], arr[i])
                        dp[i][j][1] = MAX(dp[i][j][1], -arr[i])
                    dp[i][j][1] = MAX(dp[i][j][1], dp[i - 1][j][0] - arr[i])
                    dp[i][j][2] = MAX(dp[i][j][2], dp[i - 1][j][0] + arr[i])
            ans = -inf
            for j in range(k + 1):
                ans = MAX(ans, dp[-1][j][0])
            return ans

        mx = max(nums)
        idx = nums.index(mx)
        arr1 = nums[idx:] + nums[:idx]
        arr2 = nums[idx + 1:] + nums[:idx + 1]
        r1 = calc(arr1)
        r2 = calc(arr2)
        return max(r1, r2, 0)




so = Solution()
print(so.maximumScore([4,5,20,17,20,6,18], k = 3))  #
print(so.maximumScore([1], k = 1))  #
print(so.maximumScore([1,1,2,2], k = 2))  #
print(so.maximumScore([1,3,4], k = 2))  #




