# 给你一个points 数组，表示 2D 平面上的一些点，其中 points[i] = [xi, yi] 。
#
# 连接点 [xi, yi] 和点 [xj, yj] 的费用为它们之间的 曼哈顿距离 ：|xi - xj| + |yi - yj| ，其中 |val| 表示 val 的绝对值。
#
# 请你返回将所有点连接的最小总费用。只有任意两点之间 有且仅有 一条简单路径时，才认为所有点都已连接。
#
#
#
# 示例 1：
#
#
#
# 输入：points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# 输出：20
# 解释：
#
# 我们可以按照上图所示连接所有点得到最小总费用，总费用为 20 。
# 注意到任意两个点之间只有唯一一条路径互相到达。
# 示例 2：
#
# 输入：points = [[3,12],[-2,5],[-4,1]]
# 输出：18
# 示例 3：
#
# 输入：points = [[0,0],[1,1],[1,0],[-1,1]]
# 输出：4
# 示例 4：
#
# 输入：points = [[-1000000,-1000000],[1000000,1000000]]
# 输出：4000000
# 示例 5：
#
# 输入：points = [[0,0]]
# 输出：0
#
#
# 提示：
#
# 1 <= points.length <= 1000
# -106 <= xi, yi <= 106
# 所有点 (xi, yi) 两两不同。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dis = []
        n = len(points)
        for i in range(n):
            x, y = points[i]
            for j in range(i + 1, n):
                u, v = points[j]
                dis.append([abs(x - u) + abs(y - v), i, j])
        dis.sort()

        fa = list(range(n))
        def find(x):
            if x != fa[x]:
                fa[x] = find(fa[x])
            return fa[x]
        def union(x, y):
            fa[find(y)] = find(x)
        ans = 0
        for d, i, j in dis:
            if find(i) != find(j):
                union(i, j)
                ans += d
        return ans


so = Solution()
print(so.minCostConnectPoints(points = [[0,0]]))
print(so.minCostConnectPoints(points = [[0,0],[2,2],[3,10],[5,2],[7,0]]))
print(so.minCostConnectPoints(points = [[0,0],[1,1],[1,0],[-1,1]]))




