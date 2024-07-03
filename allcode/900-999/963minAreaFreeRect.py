# 给定在 xy 平面上的一组点，确定由这些点组成的任何矩形的最小面积，其中矩形的边不一定平行于 x 轴和 y 轴。
#
# 如果没有任何矩形，就返回 0。
#
#
#
# 示例 1：
#
#
#
# 输入：[[1,2],[2,1],[1,0],[0,1]]
# 输出：2.00000
# 解释：最小面积的矩形出现在 [1,2],[2,1],[1,0],[0,1] 处，面积为 2。
# 示例 2：
#
#
#
# 输入：[[0,1],[2,1],[1,1],[1,0],[2,0]]
# 输出：1.00000
# 解释：最小面积的矩形出现在 [1,0],[1,1],[2,1],[2,0] 处，面积为 1。
# 示例 3：
#
#
#
# 输入：[[0,3],[1,2],[3,1],[1,3],[2,1]]
# 输出：0
# 解释：没法从这些点中组成任何矩形。
# 示例 4：
#
#
#
# 输入：[[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
# 输出：2.00000
# 解释：最小面积的矩形出现在 [2,1],[2,3],[3,3],[3,1] 处，面积为 2。
#
#
# 提示：
#
# 1 <= points.length <= 50
# 0 <= points[i][0] <= 40000
# 0 <= points[i][1] <= 40000
# 所有的点都是不同的。
# 与真实值误差不超过 10^-5 的答案将视为正确结果。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        n = len(points)
        s = set()
        for x, y in points:
            s.add((x, y))
        def check(x1, y1, x2, y2, x3, y3):
            # 检测 (x1, y1) 和 (x2, y2) 作为对角线
            x4, y4 = x1 + x2 - x3, y1 + y2 - y3
            if (x3, y3) != (x4, y4) and (x4, y4) in s and (y1 - y3) * (y2 - y3) == -(x1 - x3) * (x2 - x3):
                return (((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5) * (((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5)
            return inf

        ans = inf
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                for k in range(j + 1, n):
                    x3, y3 = points[k]
                    ans = min(ans, check(x1, y1, x3, y3, x2, y2))
                    ans = min(ans, check(x1, y1, x2, y2, x3, y3))
                    ans = min(ans, check(x2, y2, x3, y3, x1, y1))
        return ans if ans < inf else 0

so = Solution()
print(so.minAreaFreeRect([[0,3],[1,2],[3,1],[1,3],[2,1]]))
print(so.minAreaFreeRect([[1,2],[2,1],[1,0],[0,1]]))




