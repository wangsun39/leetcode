# 给你一个有 n 个节点的无向加权图，节点编号从 0 到 n - 1。
#
# 该图由一个二维整数数组 edges 表示，其中每条边 edges[i] = [ui, vi, wi] 表示节点 ui 和 vi 之间存在一条权重为 wi 的无向边。
#
# 另外给你整数 source、target 和 k。
#
# threshold 的值决定了一条边被认为是 轻的 还是 重的 ：
#
# 如果一条边的权重 小于 或 等于 threshold，则该边是 轻的 。
#
# 如果一条边的权重 大于 threshold，则该边是 重的 。
#
# 如果从 source 到 target 的路径包含 至多 k 条重边，则该路径是 有效的 。
#
# 返回使 source 到 target 之间 至少 存在一条 有效 路径的 最小整数 threshold。如果不存在这样的路径，则返回 -1。
#
#
#
# 示例 1：
#
#
#
# 输入： n = 6, edges = [[0,1,5],[1,2,3],[3,4,4],[4,5,1],[1,4,2]], source = 0, target = 3, k = 1
#
# 输出： 4
#
# 解释：
#
# 使得从节点 0 到节点 3 的路径最多使用 1 条重边的最小 threshold 为 4。
#
# 轻边：[1, 2, 3], [3, 4, 4], [4, 5, 1], [1, 4, 2]
#
# 重边：[0, 1, 5]
#
# 一条有效路径是 0 → 1 → 4 → 3。它只使用了 1 条重边（[0, 1, 5]），满足限制 k = 1。
#
# 任何更小的 threshold 都会导致无法在不超过 1 条重边的情况下到达节点 3。
#
# 示例 2：
#
#
#
# 输入： n = 6, edges = [[0,1,3],[1,2,4],[3,4,5],[4,5,6]], source = 0, target = 4, k = 1
#
# 输出： -1
#
# 解释：
#
# 从节点 0 到节点 4 没有路径。由于无法到达目标节点，因此输出为 -1。
#
# 示例 3：
#
#
#
# 输入： n = 4, edges = [[0,1,2],[1,2,2],[2,3,2],[3,0,2]], source = 0, target = 0, k = 0
#
# 输出： 0
#
# 解释：
#
# 源节点和目标节点是同一个节点。不需要遍历任何边，因此最小的 threshold 是 0。
#
#
#
# 提示：
#
# 1 <= n <= 103
# 0 <= edges.length <= 103
# edges[i] = [ui, vi, wi]
# 0 <= ui, vi <= n - 1
# 1 <= wi <= 109
# 0 <= source, target <= n - 1
# 0 <= k <= edges.length

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumThreshold(self, n: int, edges: List[List[int]], source: int, target: int, k: int) -> int:

        def check(val):
            g = defaultdict(list)
            for x, y, w in edges:
                if w <= val:
                    g[x].append([y, 0])
                    g[y].append([x, 0])
                else:
                    g[x].append([y, 1])
                    g[y].append([x, 1])

            def dijkstra(g: List[List[Tuple[int]]], start: int, n: int) -> List[int]:
                # dist = [inf] * len(g)   # 注意这个地方可能要替换成 n
                dist = [inf] * n
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

            dis = dijkstra(g, source, n)
            return dis[target] <= k

        if len(edges) == 0:
            if source == target:
                return 0
            return -1
        mx = max(x for _, _, x in edges)
        if not check(mx):
            return -1
        lo, hi = -1, mx
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid
        return hi


so = Solution()
print(so.minimumThreshold(n = 6, edges = [[0,1,5],[1,2,3],[3,4,4],[4,5,1],[1,4,2]], source = 0, target = 3, k = 1))



