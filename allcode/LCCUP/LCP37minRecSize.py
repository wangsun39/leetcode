# 二维平面上有 N 条直线，形式为 y = kx + b，其中 k、b为整数 且 k > 0。所有直线以 [k,b] 的形式存于二维数组 lines 中，不存在重合的两条直线。两两直线之间可能存在一个交点，最多会有 C (N,2)
#
#   个交点。我们用一个平行于坐标轴的矩形覆盖所有的交点，请问这个矩形最小面积是多少。若直线之间无交点、仅有一个交点或所有交点均在同一条平行坐标轴的直线上，则返回0。
#
# 注意：返回结果是浮点数，与标准答案 绝对误差或相对误差 在 10^-4 以内的结果都被视为正确结果
#
# 示例 1：
#
# 输入：lines = [[2,3],[3,0],[4,1]]
#
# 输出：48.00000
#
# 解释：三条直线的三个交点为 (3, 9) (1, 5) 和 (-1, -3)。最小覆盖矩形左下角为 (-1, -3) 右上角为 (3,9)，面积为 48
#
# 示例 2：
#
# 输入：lines = [[1,1],[2,3]]
#
# 输出：0.00000
#
# 解释：仅有一个交点 (-2，-1）
#
# 限制：
#
# 1 <= lines.length <= 10^5 且 lines[i].length == 2
# 1 <= lines[0] <= 10000
# -10000 <= lines[1] <= 10000
# 与标准答案绝对误差或相对误差在 10^-4 以内的结果都被视为正确结果

from leetcode.allcode.competition.mypackage import *

MAX = lambda a, b: b if b > a else a
MIN = lambda a, b: b if b < a else a

class Solution:
    def minRecSize(self, lines: List[List[int]]) -> float:
        if all(x == lines[0][0] for x, _ in lines):
            return 0

        def calc(pair):  # 根据一组(k,b) 对，计算在k,b坐标系下，负斜率最大和最小值的差（负斜率是交点的x坐标）
            group = defaultdict(list)
            for k, b in pair:
                group[k].append(b)
            group = sorted([k, arr] for k, arr in group.items())
            n = len(group)
            for i in range(n):
                group[i][1].sort()
            mn, mx = inf, -inf  # 计算点对的最大最小值，只会出现在相邻的k中
            for i in range(n - 1):
                mx = MAX(mx, -(group[i][1][-1] - group[i + 1][1][0]) / (group[i][0] - group[i + 1][0]))
                mn = MIN(mn, -(group[i][1][0] - group[i + 1][1][-1]) / (group[i][0] - group[i + 1][0]))

            return mn, mx


        lines2 = [[1/k, -b/k] for k, b in lines if k]  # 计算y轴对应的(k,b)坐标系

        x0, x1 = calc(lines)
        y0, y1 = calc(lines2)
        for k, b in lines:  # 特殊处理一下k为0的直线，交点的y坐标在b
            if k == 0:
                y0 = MIN(y0, b)
                y1 = MAX(y1, b)
        return (x1 - x0) * (y1 - y0)




so = Solution()
print(so.minRecSize(lines = [[2,3],[3,0],[4,1]]))




