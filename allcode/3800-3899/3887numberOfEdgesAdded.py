# 给你一个正整数 n。
#
# 有一个由 n 个节点组成的 无向图，节点的编号从 0 到 n - 1。最初，这个图没有任何边。
#
# 你还得到一个二维整数数组 edges，其中 edges[i] = [ui, vi, wi] 表示一条连接节点 ui 和 vi 的边，边的权重为 wi。权重 wi 要么是 0，要么是 1。
#
# 按照给定顺序处理 edges 中的每一条边。对于每条边，如果将其添加到图中后，图中的 每个环 的边权和依然是 偶数，那么将这条边添加到图中。
#
# 返回一个整数，表示最终成功添加到图中的边的数量。
#
#
#
# 示例 1：
#
# 输入： n = 3, edges = [[0,1,1],[1,2,1],[0,2,1]]
#
# 输出： 2
#
# 解释：
#
#
#
# [0, 1, 1]：添加节点 0 和节点 1 之间的边，权重为 1。
# [1, 2, 1]：添加节点 1 和节点 2 之间的边，权重为 1。
# [0, 2, 1]：节点 0 和节点 2 之间的边（图中的虚线）不被添加，因为环 0 - 1 - 2 - 0 的边权和为 1 + 1 + 1 = 3（奇数）。
# 示例 2：
#
# 输入： n = 3, edges = [[0,1,1],[1,2,1],[0,2,0]]
#
# 输出： 3
#
# 解释：
#
#
#
# [0, 1, 1]：添加节点 0 和节点 1 之间的边，权重为 1。
# [1, 2, 1]：添加节点 1 和节点 2 之间的边，权重为 1。
# [0, 2, 0]：添加节点 0 和节点 2 之间的边，权重为 0。
# 注意，环 0 - 1 - 2 - 0 的边权和为 1 + 1 + 0 = 2（偶数）。
#
#
# 提示：
#
# 3 <= n <= 5 * 104
# 1 <= edges.length <= 5 * 104
# edges[i] = [ui, vi, wi]
# 0 <= ui < vi < n
# 所有边都是唯一的。
# wi = 0 或 wi = 1

from leetcode.allcode.competition.mypackage import *

class Solution:
    def numberOfEdgesAdded(self, n: int, edges: List[List[int]]) -> int:
        fa = list(range(n))
        dist = [0] * n

        def find(x: int) -> int:
            if fa[x] != x:
                px = fa[x]
                root = find(px)
                dist[x] ^= dist[px]
                fa[x] = root
            return fa[x]

        def union(u: int, v: int, w: int) -> bool:
            pu = find(u)
            pv = find(v)
            du = dist[u]
            dv = dist[v]
            if pu == pv:
                return (du ^ dv) == w

            val = du ^ dv ^ w
            fa[pu] = pv
            dist[pu] = val
            return True

        cnt = 0
        for u, v, w in edges:
            if union(u, v, w):
                cnt += 1
        return cnt

so = Solution()
print(so.numberOfEdgesAdded(3, [[0,1,1],[1,2,1],[0,2,1]]))




