# 给你一个披萨，它由 3n 块不同大小的部分组成，现在你和你的朋友们需要按照如下规则来分披萨：
#
# 你挑选 任意 一块披萨。
# Alice 将会挑选你所选择的披萨逆时针方向的下一块披萨。
# Bob 将会挑选你所选择的披萨顺时针方向的下一块披萨。
# 重复上述过程直到没有披萨剩下。
# 每一块披萨的大小按顺时针方向由循环数组 slices 表示。
#
# 请你返回你可以获得的披萨大小总和的最大值。
#
#
#
# 示例 1：
#
#
#
# 输入：slices = [1,2,3,4,5,6]
# 输出：10
# 解释：选择大小为 4 的披萨，Alice 和 Bob 分别挑选大小为 3 和 5 的披萨。然后你选择大小为 6 的披萨，Alice 和 Bob 分别挑选大小为 2 和 1 的披萨。你获得的披萨总大小为 4 + 6 = 10 。
# 示例 2：
#
#
#
# 输入：slices = [8,9,8,6,1,1]
# 输出：16
# 解释：两轮都选大小为 8 的披萨。如果你选择大小为 9 的披萨，你的朋友们就会选择大小为 8 的披萨，这种情况下你的总和不是最大的。
#
#
# 提示：
#
# 1 <= slices.length <= 500
# slices.length % 3 == 0
# 1 <= slices[i] <= 1000
from cmath import inf
from leetcode.allcode.competition.mypackage import *


class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        n = len(slices)
        m = n // 3
        dp1 = [[0] * (m + 1) for _ in range(n)]  # dp1[i][j] 表示 slices[:i + 1] 中取 j 块，且不取第0块，不取第i块的最大总和
        dp2 = [[0] * (m + 1) for _ in range(n)]  # dp1[i][j] 表示 slices[:i + 1] 中取 j 块，且取第0块，不取第i块的最大总和
        dp3 = [[0] * (m + 1) for _ in range(n)]  # dp1[i][j] 表示 slices[:i + 1] 中取 j 块，且不取第0块，取第i块的最大总和
        dp4 = [[0] * (m + 1) for _ in range(n)]  # dp1[i][j] 表示 slices[:i + 1] 中取 j 块，且取第0块，取第i块的最大总和
        dp2[0][0] = -inf
        dp3[0][0] = -inf  # 表示做不到
        dp4[0][1] = slices[0]
        for i in range(1, n):
            if i == n - 1:
                dp1[i][m] = max(dp1[i - 1][m], dp3[i - 1][m])
                dp3[i][m] = dp1[i - 1][m - 1] + slices[i]
                dp2[i][m] = max(dp2[i - 1][m], dp4[i - 1][m])
                dp4[i][m] = -inf  # 不允许
                break
            for j in range(1, n // 3 + 1):
                dp1[i][j] = max(dp1[i - 1][j], dp3[i - 1][j])
                dp3[i][j] = dp1[i - 1][j - 1] + slices[i]
                dp2[i][j] = max(dp2[i - 1][j], dp4[i - 1][j])
                dp4[i][j] = dp2[i - 1][j - 1] + slices[i]
        return max(dp1[-1][m], dp2[-1][m], dp3[-1][m])



so = Solution()
print(so.maxSizeSlices(slices = [8,9,8,6,1,1]))
print(so.maxSizeSlices(slices = [1,2,3,4,5,6]))

