# 给你一个大小为 4 的整数数组 a 和一个大小 至少为 4 的整数数组 b。
#
# 你需要从数组 b 中选择四个下标 i0, i1, i2, 和 i3，并满足 i0 < i1 < i2 < i3。你的得分将是 a[0] * b[i0] + a[1] * b[i1] + a[2] * b[i2] + a[3] * b[i3] 的值。
#
# 返回你能够获得的 最大 得分。
#
#
#
# 示例 1：
#
# 输入： a = [3,2,5,6], b = [2,-6,4,-5,-3,2,-7]
#
# 输出： 26
#
# 解释：
# 选择下标 0, 1, 2 和 5。得分为 3 * 2 + 2 * (-6) + 5 * 4 + 6 * 2 = 26。
#
# 示例 2：
#
# 输入： a = [-1,4,5,-2], b = [-5,-1,-3,-2,-4]
#
# 输出： -1
#
# 解释：
# 选择下标 0, 1, 3 和 4。得分为 (-1) * (-5) + 4 * (-1) + 5 * (-2) + (-2) * (-4) = -1。
#
#
#
# 提示：
#
# a.length == 4
# 4 <= b.length <= 105
# -105 <= a[i], b[i] <= 105

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        n = len(b)
        dp = [[-inf] * 4 for _ in range(n)]  # dp[i][j] 前i个数，长度为j的最大值
        dp[0][0] = a[0] * b[0]
        for i in range(1, n):
            for j in range(4):
                if j == 0:
                    dp[i][j] = max(dp[i - 1][j], a[j] * b[i])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + a[j] * b[i])
        return dp[-1][-1]



so = Solution()
print(so.maxScore(a = [-1,4,5,-2], b = [-5,-1,-3,-2,-4]))
print(so.maxScore(a = [3,2,5,6], b = [2,-6,4,-5,-3,2,-7]))




