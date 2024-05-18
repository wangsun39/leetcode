# 给你一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。求最多有多少个点在同一条直线上。
#
#
#
# 示例 1：
#
#
# 输入：points = [[1,1],[2,2],[3,3]]
# 输出：3
# 示例 2：
#
#
# 输入：points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# 输出：4
#
#
# 提示：
#
# 1 <= points.length <= 300
# points[i].length == 2
# -104 <= xi, yi <= 104
# points 中的所有点 互不相同

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # 避免直接计算斜率的方法
        n = len(points)
        if n <= 2: return n
        ans = 0
        for i, (x0, y0) in enumerate(points):
            for j in range(i + 1, n):
                cnt = 2
                x1, y1 = points[j]
                dy, dx = y1 - y0, x1 - x0
                for k in range(j + 1, n):
                    x2, y2 = points[k]
                    if (y2 - y1) * dx == (x2 - x1) * dy:
                        cnt += 1
                ans = max(ans, cnt)
        return ans


so = Solution()
print(so.sortList(z))
