# 给你一个数组 points，其中 points[i] = [xi, yi] 表示无限平面上一点的坐标。
#
# 你的任务是找出满足以下条件的矩形可能的 最大 面积：
#
# 矩形的四个顶点必须是数组中的 四个 点。
# 矩形的内部或边界上 不能 包含任何其他点。
# 矩形的边与坐标轴 平行 。
# 返回可以获得的 最大面积 ，如果无法形成这样的矩形，则返回 -1。
#
#
#
# 示例 1：
#
# 输入： points = [[1,1],[1,3],[3,1],[3,3]]
#
# 输出：4
#
# 解释：
#
# 示例 1 图示
#
# 我们可以用这 4 个点作为顶点构成一个矩形，并且矩形内部或边界上没有其他点。因此，最大面积为 4 。
#
# 示例 2：
#
# 输入： points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
#
# 输出：-1
#
# 解释：
#
# 示例 2 图示
#
# 唯一一组可能构成矩形的点为 [1,1], [1,3], [3,1] 和 [3,3]，但点 [2,2] 总是位于矩形内部。因此，返回 -1 。
#
# 示例 3：
#
# 输入： points = [[1,1],[1,3],[3,1],[3,3],[1,2],[3,2]]
#
# 输出：2
#
# 解释：
#
# 示例 3 图示
#
# 点 [1,3], [1,2], [3,2], [3,3] 可以构成面积最大的矩形，面积为 2。此外，点 [1,1], [1,2], [3,1], [3,2] 也可以构成一个符合题目要求的矩形，面积相同。
#
#
#
# 提示：
#
# 1 <= points.length <= 10
# points[i].length == 2
# 0 <= xi, yi <= 100
# 给定的所有点都是 唯一 的。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        s = set((x, y) for x, y in points)
        n = len(points)
        def check(i, j, k):
            x1, y1 = points[i]
            x2, y2 = points[j]
            x3, y3 = points[k]
            if x1 != x2 != x3 != x1 or y1 != y2 != y3 != y1: return None
            if x1 == x2 == x3 or y1 == y2 == y3: return None
            if x1 == x3:
                x2, x3 = x3, x2
                y2, y3 = y3, y2
            if x2 == x3:
                x1, x3 = x3, x1
                y1, y3 = y3, y1
            if y2 == y3:
                x1, x2 = x2, x1
                y1, y2 = y2, y1
            return x1, y1, x2, y2, x3, y3

        def check2(x1, y1, x4, y4):
            mnx, mny = min(x1, x4), min(y1, y4)
            mxx, mxy = max(x1, x4), max(y1, y4)
            for x, y in points:
                if x in (x1, x4) and y in (y1, y4): continue
                if mnx <= x <= mxx and mny <= y <= mxy: return False
            return True

        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    res = check(i, j, k)
                    if res is None: continue
                    x1, y1, x2, y2, x3, y3 = res
                    x4, y4 = x3, y2
                    if (x4, y4) not in s: continue
                    if check2(x1, y1, x4, y4):
                        ans = max(ans, abs(x1 - x4) * abs(y1 - y4))
        if ans == 0:
            return -1
        return ans




so = Solution()
print(so.maxRectangleArea([[1,1],[1,3],[3,1],[3,3]]))
print(so.maxRectangleArea([[1,1],[1,3],[3,1],[3,3]]))




