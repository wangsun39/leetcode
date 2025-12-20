# 给你一个 无向带权 树，共有 n 个节点，编号从 0 到 n - 1。这棵树由一个二维整数数组 edges 表示，长度为 n - 1，其中 edges[i] = [ui, vi, wi] 表示存在一条连接节点 ui 和 vi 的边，权重为 wi。
#
# 此外，给你一个二维整数数组 queries，其中 queries[j] = [src1j, src2j, destj]。
#
# 返回一个长度等于 queries.length 的数组 answer，其中 answer[j] 表示一个子树的 最小总权重 ，使用该子树的边可以从 src1j 和 src2j 到达 destj 。
#
# 这里的 子树 是指原树中任意节点和边组成的连通子集形成的一棵有效树。
#
#
#
# 示例 1：
#
# 输入： edges = [[0,1,2],[1,2,3],[1,3,5],[1,4,4],[2,5,6]], queries = [[2,3,4],[0,2,5]]
#
# 输出： [12,11]
#
# 解释：
#
# 蓝色边表示可以得到最优答案的子树之一。
#
#
#
# answer[0]：在选出的子树中，从 src1 = 2 和 src2 = 3 到 dest = 4 的路径总权重为 3 + 5 + 4 = 12。
#
# answer[1]：在选出的子树中，从 src1 = 0 和 src2 = 2 到 dest = 5 的路径总权重为 2 + 3 + 6 = 11。
#
# 示例 2：
#
# 输入： edges = [[1,0,8],[0,2,7]], queries = [[0,1,2]]
#
# 输出： [15]
#
# 解释：
#
#
#
# answer[0]：选出的子树中，从 src1 = 0 和 src2 = 1 到 dest = 2 的路径总权重为 8 + 7 = 15。
#
#
# 提示：
#
# 3 <= n <= 105
# edges.length == n - 1
# edges[i].length == 3
# 0 <= ui, vi < n
# 1 <= wi <= 104
# 1 <= queries.length <= 105
# queries[j].length == 3
# 0 <= src1j, src2j, destj < n
# src1j、src2j 和 destj 互不不同。
# 输入数据保证 edges 表示的是一棵有效的树。

from leetcode.allcode.competition.mypackage import *

class TreeAncestor:
    def __init__(self, edges: List[List[int]]):
        n = len(edges) + 1
        m = n.bit_length()
        g = [[] for _ in range(n)]
        for x, y, _ in edges:  # 节点编号从 0 开始
            g[x].append(y)
            g[y].append(x)

        depth = [0] * n
        pa = [[-1] * m for _ in range(n)]
        def dfs(x: int, fa: int) -> None:
            pa[x][0] = fa
            for y in g[x]:
                if y != fa:
                    depth[y] = depth[x] + 1
                    dfs(y, x)
        dfs(0, -1)

        for i in range(m - 1):
            for x in range(n):
                if (p := pa[x][i]) != -1:
                    pa[x][i + 1] = pa[p][i]
        self.depth = depth
        self.pa = pa

    def get_kth_ancestor(self, node: int, k: int) -> int:
        for i in range(k.bit_length()):
            if k >> i & 1:  # k 二进制从低到高第 i 位是 1
                node = self.pa[node][i]
        return node

    # 返回 x 和 y 的最近公共祖先（节点编号从 0 开始）
    def get_lca(self, x: int, y: int) -> int:
        if self.depth[x] > self.depth[y]:
            x, y = y, x
        # 使 y 和 x 在同一深度
        y = self.get_kth_ancestor(y, self.depth[y] - self.depth[x])
        if y == x:
            return x
        for i in range(len(self.pa[x]) - 1, -1, -1):
            px, py = self.pa[x][i], self.pa[y][i]
            if px != py:
                x, y = px, py  # 同时往上跳 2**i 步
        return self.pa[x][0]

class Solution:
    def minimumWeight(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        ta = TreeAncestor(edges)
        n = len(edges) + 1
        g = defaultdict(list)
        for x, y, w in edges:
            g[x].append([y, w])
            g[y].append([x, w])

        s = [0] * n  # 到 0 的权重和

        def dfs(x, fa):
            for y, w in g[x]:
                if y != fa:
                    s[y] += s[x] + w
                    dfs(y, x)

        dfs(0, -1)  # 计数各点权重和

        ans = []
        for x, y, z in queries:
            # x, y, z = sorted([x, y, z], key=lambda x: ta.depth[x])
            a, b, c = ta.get_lca(x, y), ta.get_lca(y, z), ta.get_lca(x, z)
            ha, hb, hc = ta.depth[a], ta.depth[b], ta.depth[c]
            mx = max(ha, hb, hc)
            if ha == mx:
                x, y, z = z, x, y
            elif hc == mx:
                x, y, z = y, x, z

            u = ta.get_lca(y, z)
            if u in (y, z):
                r1 = abs(s[y] - s[z])
            else:
                r1 = s[y] - s[u] + s[z] - s[u]
            v = ta.get_lca(u, x)
            if v == x:
                r2 = s[u] - s[v]
            elif v == u:
                if ta.get_lca(y, x) == x or ta.get_lca(z, x) == x:
                    r2 = 0
                else:
                    r2 = s[x] - s[v]
            else:
                r2 = s[u] - s[v] + s[x] - s[v]
            ans.append(r1 + r2)


        return ans





so = Solution()
print(so.minimumWeight(edges = [[2,4,6],[4,5,6],[4,0,3],[0,3,4],[1,3,10],[1,6,7]], queries = [[2,1,5]]))   # [29]
print(so.minimumWeight(edges = [[0,1,10],[2,0,2],[3,2,8]], queries = [[1,3,2],[2,1,3],[2,3,1],[1,3,0]]))   # [20,20,20,20]
print(so.minimumWeight(edges = [[0,1,2],[1,2,3],[1,3,5],[1,4,4],[2,5,6]], queries = [[2,3,4],[0,2,5]]))   #




