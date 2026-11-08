# 给你一棵含有 n 个节点的无向 树，节点编号从 0 到 n - 1，用一个长度为 n - 1 的二维整数数组 edges 表示，其中 edges[i] = [ui, vi] 表示节点 ui 和 vi 之间存在一条无向边。
#
# 同时给你一个长度为 n 的字符串 colors，其中 colors[i] 是 'R'、'B' 或 'W' 之一，表示节点 i 的颜色。
#
# 一个被选作 根节点 的节点，在以它为起点将树定向（即从根向外定向）之后，必须同时满足以下两个 条件：
#
# 二叉树性质：每个节点最多有两个子节点。
# 分层颜色模式：处于相同深度的所有节点都具有相同的颜色。从深度 0 开始，这些颜色遵循以下三种循环序列之一：
# R → B → W → R → B → W → ...
# B → W → R → B → W → R → ...
# W → R → B → W → R → B → ...
# 返回满足这两个条件的任意根节点的 下标，如果不存在这样的根节点，则返回 -1。
#
# 树 是一个无环的连通无向图。
#
# 节点的 深度 是从根节点到该节点的路径上的边数。根节点的深度为 0。一个节点的 子节点 是指与其相邻且深度大 1 的节点。
#
# 节点的 度 是指与该节点相连的边数。
#
#
#
# 示例 1：
#
# 输入： edges = [[3,1],[3,2],[1,4],[2,0]], colors = "BRRWB"
#
# 输出： 3
#
# 解释：
#
#
#
# 以节点 3 为根节点时，每个节点最多有两个子节点，且每条边都向循环中的下一个颜色推进（W → R → B），因此返回 3。
#
# 示例 2：
#
# 输入： edges = [[0,1],[1,2],[2,3]], colors = "RBRB"
#
# 输出： -1
#
# 解释：
#
#
#
# 没有一个根节点能在每条边上都满足所需的颜色递进，因此返回 -1。
#
#
#
# 提示：
#
# 2 <= n <= 105
# edges.length == n - 1
# edges[i] = [ui, vi]
# 0 <= ui, vi < n
# colors.length == n
# colors[i] 是 'R'、'B' 或 'W' 之一。
# 输入图是一棵树，且每个节点的度最多为三。
from collections import defaultdict

from leetcode.allcode.competition.mypackage import *

class Solution:
    def findColoredRoot(self, edges: list[list[int]], colors: str) -> int:
        g = defaultdict(list)
        for x, y in edges:
            if colors[x] == colors[y]:
                return -1
            g[x].append(y)
            g[y].append(x)

        pre = {'B': 'R', 'W': 'B', 'R': 'W'}
        # 从任一点出发不断找它的前导点
        r = 0
        while True:
            p = colors[r]
            for x in g[r]:
                if colors[x] == pre[p]:
                    r = x
                    break
            if p == colors[r]:  # r 没有变化 说明 r没有前导点，它就是根节点
                break

        def check(r):
            # 检查 r 是根节点是否成立
            if len(g[r]) > 2: return False
            if colors[r] == 'R':
                st = ['R', 'B', 'W']
            elif colors[r] == 'B':
                st = ['B', 'W', 'R']
            else:
                st = ['W', 'R', 'B']

            def dfs(x, fa, lv):
                for y in g[x]:
                    if y == fa: continue
                    if st[(lv + 1) % 3] != colors[y]:
                        return False
                    if not dfs(y, x, lv + 1):
                        return False
                return True

            return dfs(r, -1, 0)

        if check(r):
            return r

        return -1



so = Solution()
print(so.findColoredRoot(edges = [[0,1],[2,1]], colors = "RWB"))
print(so.findColoredRoot(edges = [[2,4],[3,4],[0,3],[4,1]], colors = "RRRBW"))
print(so.findColoredRoot(edges = [[1,0],[0,2],[3,0]], colors = "WBRR"))
print(so.findColoredRoot(edges = [[3,1],[3,2],[1,4],[2,0]], colors = "BRRWB"))
print(so.findColoredRoot(edges = [[1,0]], colors = "BR"))
print(so.findColoredRoot(edges = [[0,1],[1,2],[2,3]], colors = "RBRB"))



