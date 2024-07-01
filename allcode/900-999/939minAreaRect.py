# 给定在 xy 平面上的一组点，确定由这些点组成的矩形的最小面积，其中矩形的边平行于 x 轴和 y 轴。
#
# 如果没有任何矩形，就返回 0。
#
#
#
# 示例 1：
#
# 输入：[[1,1],[1,3],[3,1],[3,3],[2,2]]
# 输出：4
# 示例 2：
#
# 输入：[[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
# 输出：2
#
#
# 提示：
#
# 1 <= points.length <= 500
# 0 <= points[i][0] <= 40000
# 0 <= points[i][1] <= 40000
# 所有的点都是不同的。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points.sort()
        n = len(points)
        row = defaultdict(list)
        col = defaultdict(list)
        s = set()
        ans = inf
        for x, y in points:
            col[x].append(y)
            row[y].append(x)
            s.add((y, x))
        for i in range(n):
            x, y = points[i]
            p1 = bisect_right(row[y], x)
            if p1 >= len(row[y]): continue
            p2 = bisect_right(col[x], y)
            if p2 >= len(col[x]): continue
            for j in range(p1, len(row[y])):
                for k in range(p2, len(col[x])):
                    u, v = row[y][j], col[x][k]
                    if (v, u) in s:
                        ans = min(ans, (u - x) * (v - y))
        if ans == inf:
            return 0
        return ans



so = Solution()
print(so.minAreaRect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]))  # 2
print(so.minAreaRect([[0,1],[1,3],[3,3],[4,4],[1,4],[2,3],[1,0],[3,4]]))
print(so.minAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2]]))  # 4




