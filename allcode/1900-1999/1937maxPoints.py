# 给你一个 m x n 的整数矩阵 points （下标从 0 开始）。一开始你的得分为 0 ，你想最大化从矩阵中得到的分数。
#
# 你的得分方式为：每一行 中选取一个格子，选中坐标为 (r, c) 的格子会给你的总得分 增加 points[r][c] 。
#
# 然而，相邻行之间被选中的格子如果隔得太远，你会失去一些得分。对于相邻行 r 和 r + 1 （其中 0 <= r < m - 1），选中坐标为 (r, c1) 和 (r + 1, c2) 的格子，你的总得分 减少 abs(c1 - c2) 。
#
# 请你返回你能得到的 最大 得分。
#
# abs(x) 定义为：
#
# 如果 x >= 0 ，那么值为 x 。
# 如果 x < 0 ，那么值为 -x 。
#
#
# 示例 1：
#
#
# 输入：points = [[1,2,3],[1,5,1],[3,1,1]]
# 输出：9
# 解释：
# 蓝色格子是最优方案选中的格子，坐标分别为 (0, 2)，(1, 1) 和 (2, 0) 。
# 你的总得分增加 3 + 5 + 3 = 11 。
# 但是你的总得分需要扣除 abs(2 - 1) + abs(1 - 0) = 2 。
# 你的最终得分为 11 - 2 = 9 。
# 示例 2：
#
#
# 输入：points = [[1,5],[2,3],[4,2]]
# 输出：11
# 解释：
# 蓝色格子是最优方案选中的格子，坐标分别为 (0, 1)，(1, 1) 和 (2, 0) 。
# 你的总得分增加 5 + 3 + 4 = 12 。
# 但是你的总得分需要扣除 abs(1 - 1) + abs(1 - 0) = 1 。
# 你的最终得分为 12 - 1 = 11 。
#
#
# 提示：
#
# m == points.length
# n == points[r].length
# 1 <= m, n <= 105
# 1 <= m * n <= 105
# 0 <= points[r][c] <= 105

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        r, c = len(points), len(points[0])
        dp1, dp2 = points[0], [0] * c
        for p in points[1:]:
            left, right = [0] * c, [c - 1] * c  # 左右的最大值
            mx_i = 0
            for i in range(1, c):
                if dp1[mx_i] - (i - mx_i) < dp1[i - 1] - 1:
                    mx_i = i - 1
                left[i] = mx_i  # p[i] 左侧能产生最大值的下标
            mx_i = c - 1
            for i in range(c - 2, -1, -1):
                if dp1[mx_i] - (mx_i - i) < dp1[i + 1] - 1:
                    mx_i = i + 1
                right[i] = mx_i
            for i in range(c):
                l, r = left[i], right[i]
                dp2[i] = max(dp1[l] - (i - l), dp1[r] - (r - i), dp1[i]) + p[i]
            dp1, dp2 = dp2, [0] * c
        return max(dp1)



so = Solution()
print(so.maxPoints([[0,3,0,4,2],[5,4,2,4,1],[5,0,0,5,1],[2,0,1,0,3]]))
print(so.maxPoints([[2,2],[2,2],[2,2]]))
print(so.maxPoints([[1,5],[2,3],[4,2]]))
print(so.maxPoints([[1,2,3],[1,5,1],[3,1,1]]))




