# 给定数组 nums 和一个整数 k 。我们将给定的数组 nums 分成 最多 k 个相邻的非空子数组 。 分数 由每个子数组内的平均值的总和构成。
#
# 注意我们必须使用 nums 数组中的每一个数进行分组，并且分数不一定需要是整数。
#
# 返回我们所能得到的最大 分数 是多少。答案误差在 10-6 内被视为是正确的。
#
#
#
# 示例 1:
#
# 输入: nums = [9,1,2,3,9], k = 3
# 输出: 20.00000
# 解释:
# nums 的最优分组是[9], [1, 2, 3], [9]. 得到的分数是 9 + (1 + 2 + 3) / 3 + 9 = 20.
# 我们也可以把 nums 分成[9, 1], [2], [3, 9].
# 这样的分组得到的分数为 5 + 2 + 6 = 13, 但不是最大值.
# 示例 2:
#
# 输入: nums = [1,2,3,4,5,6,7], k = 4
# 输出: 20.50000
#
#
# 提示:
#
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 104
# 1 <= k <= nums.length


from typing import List
class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        dp = [[0] * n for _ in range(k)]  # dp[i][j] 表示 前j个数，分成i+1组最大的平均数之和
        s = [[0] * n for _ in range(n)]  # s[i][j] 表示 nums[i: j + 1]的和
        for i in range(n):
            ss = 0
            for j in range(i, n):
                ss += nums[j]
                s[i][j] = ss
        for i in range(n):
            dp[0][i] = s[0][i] / (i + 1)
        print(dp)
        for i in range(1, k):
            for j in range(i, n):
                ma = 0
                for t in range(j):
                    ma = max(ma, dp[i - 1][t] + s[t + 1][j] / (j - t))
                dp[i][j] = ma
        return dp[-1][-1]




so = Solution()
print(so.largestSumOfAverages(nums = [9,1,2,3,9], k = 3))
print(so.largestSumOfAverages(nums = [1,2,3,4,5,6,7], k = 4))

