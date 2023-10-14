# 现有一棵由 n 个节点组成的无向树，节点按从 0 到 n - 1 编号。给你一个整数 n 和一个长度为 n - 1 的二维整数数组 edges ，其中 edges[i] = [ui, vi, wi] 表示树中存在一条位于节点 ui 和节点 vi 之间、权重为 wi 的边。
#
# 另给你一个长度为 m 的二维整数数组 queries ，其中 queries[i] = [ai, bi] 。对于每条查询，请你找出使从 ai 到 bi 路径上每条边的权重相等所需的 最小操作次数 。在一次操作中，你可以选择树上的任意一条边，并将其权重更改为任意值。
#
# 注意：
#
# 查询之间 相互独立 的，这意味着每条新的查询时，树都会回到 初始状态 。
# 从 ai 到 bi的路径是一个由 不同 节点组成的序列，从节点 ai 开始，到节点 bi 结束，且序列中相邻的两个节点在树中共享一条边。
# 返回一个长度为 m 的数组 answer ，其中 answer[i] 是第 i 条查询的答案。
#
#
#
# 示例 1：
#
#
# 输入：n = 7, edges = [[0,1,1],[1,2,1],[2,3,1],[3,4,2],[4,5,2],[5,6,2]], queries = [[0,3],[3,6],[2,6],[0,6]]
# 输出：[0,0,1,3]
# 解释：第 1 条查询，从节点 0 到节点 3 的路径中的所有边的权重都是 1 。因此，答案为 0 。
# 第 2 条查询，从节点 3 到节点 6 的路径中的所有边的权重都是 2 。因此，答案为 0 。
# 第 3 条查询，将边 [2,3] 的权重变更为 2 。在这次操作之后，从节点 2 到节点 6 的路径中的所有边的权重都是 2 。因此，答案为 1 。
# 第 4 条查询，将边 [0,1]、[1,2]、[2,3] 的权重变更为 2 。在这次操作之后，从节点 0 到节点 6 的路径中的所有边的权重都是 2 。因此，答案为 3 。
# 对于每条查询 queries[i] ，可以证明 answer[i] 是使从 ai 到 bi 的路径中的所有边的权重相等的最小操作次数。
# 示例 2：
#
#
# 输入：n = 8, edges = [[1,2,6],[1,3,4],[2,4,6],[2,5,3],[3,6,6],[3,0,8],[7,0,2]], queries = [[4,6],[0,4],[6,5],[7,4]]
# 输出：[1,2,2,3]
# 解释：第 1 条查询，将边 [1,3] 的权重变更为 6 。在这次操作之后，从节点 4 到节点 6 的路径中的所有边的权重都是 6 。因此，答案为 1 。
# 第 2 条查询，将边 [0,3]、[3,1] 的权重变更为 6 。在这次操作之后，从节点 0 到节点 4 的路径中的所有边的权重都是 6 。因此，答案为 2 。
# 第 3 条查询，将边 [1,3]、[5,2] 的权重变更为 6 。在这次操作之后，从节点 6 到节点 5 的路径中的所有边的权重都是 6 。因此，答案为 2 。
# 第 4 条查询，将边 [0,7]、[0,3]、[1,3] 的权重变更为 6 。在这次操作之后，从节点 7 到节点 4 的路径中的所有边的权重都是 6 。因此，答案为 3 。
# 对于每条查询 queries[i] ，可以证明 answer[i] 是使从 ai 到 bi 的路径中的所有边的权重相等的最小操作次数。
#
#
# 提示：
#
# 1 <= n <= 104
# edges.length == n - 1
# edges[i].length == 3
# 0 <= ui, vi < n
# 1 <= wi <= 26
# 生成的输入满足 edges 表示一棵有效的树
# 1 <= queries.length == m <= 2 * 104
# queries[i].length == 2
# 0 <= ai, bi < n
import math
from leetcode.allcode.competition.mypackage import *

class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        w = {}
        for x, y, z in edges:
            g[x].append(y)
            g[y].append(x)
            w[(x, y)] = w[(y, x)] = z - 1
        dep = [0] * n  # 节点深度

        m = int(math.log(n, 2)) + 1
        ac = [[0] * m for _ in range(n)] # ac[i][j] 表示第i个节点的2^j个祖先
        cnt = [[[0] * 26 for _ in range(m)] for _ in range(n)]  # cnt[i][j][k]  第i个点到它的第2^i个祖先之间权重为k出现的次数

        def dfs(x, p):
            for y in g[x]:
                if y == p: continue
                dep[y] = dep[x] + 1
                ac[y][0] = x
                cnt[y][0][w[(x, y)]] = 1
                dfs(y, x)
        dfs(0, -1)

        for j in range(1, m):
            for i in range(n):
                f = ac[i][j - 1]  # i的第2^(j-1)个祖先
                if f == 0: continue
                ac[i][j] = ac[f][j - 1]
                for k in range(26):
                    cnt[i][j][k] = cnt[i][j - 1][k] + cnt[f][j - 1][k]

        def lca(x0, y0):
            if dep[x0] > dep[y0]:
                x0, y0 = y0, x0
            x, y = x0, y0
            counter = [0] * 26
            diff = dep[y] - dep[x]
            i = 0
            while diff:
                if diff & 1:
                    for j in range(26):
                        counter[j] += cnt[y][i][j]
                    y = ac[y][i]
                i += 1
                diff >>= 1
            if x == y:
                t = x
            else:
                for i in range(m - 1, -1, -1):
                    if ac[x][i] == ac[y][i]:
                        continue
                    for j in range(26):
                        counter[j] += (cnt[x][i][j] + cnt[y][i][j])
                    x, y = ac[x][i], ac[y][i]
                t = ac[x][0]  # lca 节点
                wx, wy = w[(x, ac[x][0])], w[(y, ac[y][0])]
                counter[wx] += cnt[x][0][wx]
                counter[wy] += cnt[y][0][wy]
            dxy = dep[x0] + dep[y0] - dep[t] * 2  # x,y 的距离
            return dxy - max(counter)

        ans = [0] * len(queries)
        for i, [x, y] in enumerate(queries):
            ans[i] = lca(x, y)

        return ans


so = Solution()
print(so.minOperationsQueries(n = 6, edges = [[4,3,2],[5,3,2],[1,4,5],[0,4,2],[2,1,1]], queries = [[5,2],[0,4],[2,1],[5,4],[2,0],[4,2],[4,5],[3,3],[5,0],[3,5]]))
print(so.minOperationsQueries(n = 8, edges = [[1,2,6],[1,3,4],[2,4,6],[2,5,3],[3,6,6],[3,0,8],[7,0,2]], queries = [[4,6],[0,4],[6,5],[7,4]]))
print(so.minOperationsQueries(n = 7, edges = [[0,1,1],[1,2,1],[2,3,1],[3,4,2],[4,5,2],[5,6,2]], queries = [[0,3],[3,6],[2,6],[0,6]]))




