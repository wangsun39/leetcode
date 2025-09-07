# 现有一个含 n 个顶点的 双向 图，每个顶点按从 0 到 n - 1 标记。图中的边由二维整数数组 edges 表示，其中 edges[i] = [ui, vi] 表示顶点 ui 和 vi 之间存在一条边。每对顶点最多通过一条边连接，并且不存在与自身相连的顶点。
#
# 返回图中 最短 环的长度。如果不存在环，则返回 -1 。
#
# 环 是指以同一节点开始和结束，并且路径中的每条边仅使用一次。
#
#
#
# 示例 1：
#
#
# 输入：n = 7, edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]
# 输出：3
# 解释：长度最小的循环是：0 -> 1 -> 2 -> 0
# 示例 2：
#
#
# 输入：n = 4, edges = [[0,1],[0,2]]
# 输出：-1
# 解释：图中不存在循环
#
#
# 提示：
#
# 2 <= n <= 1000
# 1 <= edges.length <= 1000
# edges[i].length == 2
# 0 <= ui, vi < n
# ui != vi
# 不存在重复的边

from leetcode.allcode.competition.mypackage import *


class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        ans = inf

        def bfs(x0):
            nonlocal ans
            distance = {x0: 0}
            dq1 = deque([[x0, -1]])
            dep = 0
            while dq1:
                dq2 = deque()
                while dq1:
                    x, fa = dq1.popleft()
                    for y in g[x]:
                        if y == fa: continue
                        if y in distance:
                            ans = min(ans, distance[y] + dep + 1)
                        else:
                            distance[y] = dep + 1
                            dq2.append([y, x])
                dq1 = dq2
                dep += 1

        for i in range(n):
            bfs(i)

        return ans if ans != inf else -1




so = Solution()
print(so.findShortestCycle(n = 7, edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]))  # 3
print(so.findShortestCycle(n = 10, edges = [[4,5],[1,6],[6,4],[5,3],[3,6],[0,2],[5,8],[0,6],[3,0],[6,8],[2,8],[1,2],[9,4]]))  # 3




