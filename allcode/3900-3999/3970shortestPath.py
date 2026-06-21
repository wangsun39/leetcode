# 给你一个整数 n，表示一个 有向加权 图中的节点数量，节点编号从 0 到 n - 1。该图由二维数组 edges 表示，其中 edges[i] = [ui, vi, wi] 表示一条从节点 ui 指向节点 vi、权重为 wi 的有向边。
#
# 另给定一个长度为 n 的字符串 labels，其中 labels[i] 是分配给节点 i 的字符，以及一个整数 k。
#
# 返回一条从节点 0 到节点 n - 1 的路径的 最小总边权 ，并要求该路径上所有节点标签按顺序 拼接 后，最多包含 k 个 连续相同 字符。如果不存在有效路径，返回 -1。
#
#
#
# 示例 1：
#
# 输入： n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 1
#
# 输出： 3
#
# 解释：
#
# 从节点 0 到节点 2 的最优有效路径如下：
#
# 使用 edges[2] = [0, 2, 3] 到达节点 2，边权 wi = 3。
# 对应的标签拼接结果为 "ab"，满足最多有 k = 1 个连续相同字符。因此答案为 3。
#
# 示例 2：
#
# 输入： n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 2
#
# 输出： 2
#
# 解释：
#
# 从节点 0 到节点 2 的最优有效路径如下：
#
# 使用 edges[0] = [0, 1, 1] 到达节点 1，边权 wi = 1。
# 使用 edges[1] = [1, 2, 1] 到达节点 2，边权 wi = 1。
# 对应的标签拼接结果为 "aab"，满足最多有 k = 2 个连续相同字符。因此答案为 2。
#
# 示例 3：
#
# 输入： n = 3, edges = [[0,1,1],[1,2,1]], labels = "aaa", k = 2
#
# 输出： -1
#
# 解释：
#
# 不存在从节点 0 到节点 2 的有效路径，使其满足最多有 k = 2 个连续相同字符。因此答案为 -1。
#
#
#
# 提示：
#
# 1 <= n == labels.length <= 5 * 104
# 0 <= edges.length <= 5 * 104
# edges[i] == [ui, vi, wi]
# 0 <= ui, vi <= n - 1
# ui != vi
# 1 <= wi <= 104
# labels 由小写英文字母组成
# 1 <= k <= 50

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        g = defaultdict(list)
        for x, y, w in edges:
            g[x].append([y, w])

        def dijkstra(g: List[List[Tuple[int]]], start: int) -> List[int]:
            dist = [[inf] * k for _ in range(n)]  # 到达 i 后有连续 j个labels[i]的最短路径为 dist[i][j]
            dist[start][0] = 0
            h = [(0, start, 0)]
            while h:
                d, x, t = heappop(h)
                if d > dist[x][t]:
                    continue
                for y, wt in g[x]:
                    new_d = dist[x][t] + wt
                    if labels[y] != labels[x]:
                        if new_d < dist[y][0]:
                            dist[y][0] = new_d
                            heappush(h, (new_d, y, 0))
                    else:
                        if t < k - 1:
                            if new_d < dist[y][t + 1]:
                                dist[y][t + 1] = new_d
                                heappush(h, (new_d, y, t + 1))
            return dist

        d = dijkstra(g, 0)
        ans = min(d[n - 1])
        if ans == inf:
            return -1
        return ans


so = Solution()
print(so.shortestPath(n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 1))




