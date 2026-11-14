# 给你一个整数 n，表示一棵有 n 个节点的树，节点编号从 0 到 n - 1，并且树以节点 0 为 根节点。这棵树由一个长度为 n - 1 的二维数组 edges 表示，其中 edges[i] = [ui, vi] 表示节点 ui 和 vi 之间存在一条 无向 边。
#
# 另给你一个长度为 n 的字符串 colors，其中 colors[i] 表示节点 i 的颜色：'R' 表示红色，'B' 表示蓝色。
#
# 你可以 翻转 任意节点的颜色：从 'R' 变为 'B'，或从 'B' 变为 'R'。翻转节点 u 的代价等于以节点 u 为根的子树的大小。
#
# 你的目标是通过翻转颜色，使所有 红色 节点在树中形成 一个连通分量 。蓝色节点可以不连通。没有红色节点的配置也视为有效。
#
# 返回实现这一目标所需的 最小总代价 。
#
#
#
# 示例 1：
#
# 输入： n = 3, colors = "RBR", edges = [[0,1],[1,2]]
#
# 输出： 1
#
# 解释：
#
#
#
# 有两个红色节点（0 和 2），它们彼此不连通。
# 可以将节点 2 从 'R'（红色）翻转为 'B'（蓝色）。节点 2 的子树大小为 1，因此代价为 1。
# 翻转后，只有节点 0 仍为红色，恰好形成一个红色连通分量。
# 示例 2：
#
# 输入： n = 3, colors = "RBR", edges = [[0,1],[0,2]]
#
# 输出： 0
#
# 解释：
#
#
#
# 有两个红色节点（0 和 2），它们已经彼此连通。
# 所有红色节点已经形成一个连通分量，因此无须翻转。最小总代价为 0。
# 示例 3：
#
# 输入： n = 4, colors = "BRRR", edges = [[0,1],[0,2],[0,3]]
#
# 输出： 2
#
# 解释：
#
#
#
# 有三个红色节点（1、2 和 3），它们彼此不连通。
# 这三个红色节点都是叶节点，且互不连通。
# 为了得到一个红色连通分量，保留一个红色叶节点，并将另外两个翻转为蓝色。
# 每个叶节点的子树大小均为 1，因此翻转其中任意两个的总代价为 2。
# 示例 4：
#
# 输入： n = 3, colors = "BBB", edges = [[0,1],[1,2]]
#
# 输出： 0
#
# 解释：
#
#
#
# 所有节点均为蓝色，因此没有红色节点。
# 空的红色节点集合也视为一个连通分量，因此当前状态已经有效，代价为 0。
#
#
# 提示：
#
# 1 <= n <= 105
# n == colors.length
# colors[i] 为 'R' 或 'B'。
# edges.length == n - 1
# edges[i] = [ui, vi]
# 0 <= ui, vi <= n - 1
# 输入保证 edges 表示一棵有效的树。

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

class Solution:
    def minCost(self, n: int, colors: str, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        cost = [0] * n

        def dfs1(x, fa):
            res = 1
            for y in g[x]:
                if y == fa: continue
                res += dfs1(y, x)
            cost[x] = res
            return res

        dfs1(0, -1)

        def dfs(x, fa):
            # 返回3个值，子树全蓝， 子树根为红， 子树根蓝但有个子子树有红，
            r1 = r2 = r3 = 0
            if colors[x] == 'B':
                r2 += cost[x]
            else:
                r1 = r3 = cost[x]
            rr = []
            for y in g[x]:
                if y == fa: continue
                rr.append(dfs(y, x))

            if len(rr):
                s0 = sum(r[0] for r in rr)
                r1 += s0
                r2 += sum(MIN(r[0], r[1]) for r in rr)
                rr3 = inf
                for a, b, c in rr:
                    rr3 = MIN(rr3, s0 - a + MIN(b, c))
                r3 += rr3

            return [r1, r2, r3]

        ans = dfs(0, -1)
        return min(ans)




so = Solution()
print(so.minCost(n = 4, colors = "BRRR", edges = [[0,1],[0,2],[0,3]]))  # 2
print(so.minCost(n = 3, colors = "RBR", edges = [[0,1],[1,2]]))  # 1


