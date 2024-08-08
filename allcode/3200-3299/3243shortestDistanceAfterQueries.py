# 给你一个整数 n 和一个二维整数数组 queries。
#
# 有 n 个城市，编号从 0 到 n - 1。初始时，每个城市 i 都有一条单向道路通往城市 i + 1（ 0 <= i < n - 1）。
#
# queries[i] = [ui, vi] 表示新建一条从城市 ui 到城市 vi 的单向道路。每次查询后，你需要找到从城市 0 到城市 n - 1 的最短路径的长度。
#
# 返回一个数组 answer，对于范围 [0, queries.length - 1] 中的每个 i，answer[i] 是处理完前 i + 1 个查询后，从城市 0 到城市 n - 1 的最短路径的长度。
#
#
#
# 示例 1：
#
# 输入： n = 5, queries = [[2, 4], [0, 2], [0, 4]]
#
# 输出： [3, 2, 1]
#
# 解释：
#
#
#
# 新增一条从 2 到 4 的道路后，从 0 到 4 的最短路径长度为 3。
#
#
#
# 新增一条从 0 到 2 的道路后，从 0 到 4 的最短路径长度为 2。
#
#
#
# 新增一条从 0 到 4 的道路后，从 0 到 4 的最短路径长度为 1。
#
# 示例 2：
#
# 输入： n = 4, queries = [[0, 3], [0, 2]]
#
# 输出： [1, 1]
#
# 解释：
#
#
#
# 新增一条从 0 到 3 的道路后，从 0 到 3 的最短路径长度为 1。
#
#
#
# 新增一条从 0 到 2 的道路后，从 0 到 3 的最短路径长度仍为 1。
#
#
#
# 提示：
#
# 3 <= n <= 500
# 1 <= queries.length <= 500
# queries[i].length == 2
# 0 <= queries[i][0] < queries[i][1] < n
# 1 < queries[i][1] - queries[i][0]
# 查询中没有重复的道路。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        def dijkstra(g: List[List[Tuple[int]]], start: int) -> List[int]:
            dist = [inf] * n  # 注意这个地方可能要替换成 n
            dist[start] = 0
            h = [(0, start)]
            while h:
                d, x = heappop(h)
                if d > dist[x]:
                    continue
                for y, wt in g[x]:
                    new_d = dist[x] + wt
                    if new_d < dist[y]:
                        dist[y] = new_d
                        heappush(h, (new_d, y))
            return dist

        g = defaultdict(list)
        for i in range(n - 1):
            g[i].append([i + 1, 1])
        ans = []
        for u, v in queries:
            g[u].append([v, 1])
            dist = dijkstra(g, 0)
            ans.append(dist[n - 1])
        return ans


so = Solution()
print(so.shortestDistanceAfterQueries(n = 5, queries = [[2, 4], [0, 2], [0, 4]]))
print(so.shortestDistanceAfterQueries(n = 4, queries = [[0, 3], [0, 2]]))




