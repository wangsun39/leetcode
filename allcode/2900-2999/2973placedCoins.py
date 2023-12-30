# 给你一棵 n 个节点的 无向 树，节点编号为 0 到 n - 1 ，树的根节点在节点 0 处。同时给你一个长度为 n - 1 的二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间有一条边。
#
# 给你一个长度为 n 下标从 0 开始的整数数组 cost ，其中 cost[i] 是第 i 个节点的 开销 。
#
# 你需要在树中每个节点都放置金币，在节点 i 处的金币数目计算方法如下：
#
# 如果节点 i 对应的子树中的节点数目小于 3 ，那么放 1 个金币。
# 否则，计算节点 i 对应的子树内 3 个不同节点的开销乘积的 最大值 ，并在节点 i 处放置对应数目的金币。如果最大乘积是 负数 ，那么放置 0 个金币。
# 请你返回一个长度为 n 的数组 coin ，coin[i]是节点 i 处的金币数目。
#
#
#
# 示例 1：
#
#
#
# 输入：edges = [[0,1],[0,2],[0,3],[0,4],[0,5]], cost = [1,2,3,4,5,6]
# 输出：[120,1,1,1,1,1]
# 解释：在节点 0 处放置 6 * 5 * 4 = 120 个金币。所有其他节点都是叶子节点，子树中只有 1 个节点，所以其他每个节点都放 1 个金币。
# 示例 2：
#
#
#
# 输入：edges = [[0,1],[0,2],[1,3],[1,4],[1,5],[2,6],[2,7],[2,8]], cost = [1,4,2,3,5,7,8,-4,2]
# 输出：[280,140,32,1,1,1,1,1,1]
# 解释：每个节点放置的金币数分别为：
# - 节点 0 处放置 8 * 7 * 5 = 280 个金币。
# - 节点 1 处放置 7 * 5 * 4 = 140 个金币。
# - 节点 2 处放置 8 * 2 * 2 = 32 个金币。
# - 其他节点都是叶子节点，子树内节点数目为 1 ，所以其他每个节点都放 1 个金币。
# 示例 3：
#
#
#
# 输入：edges = [[0,1],[0,2]], cost = [1,2,-2]
# 输出：[0,1,1]
# 解释：节点 1 和 2 都是叶子节点，子树内节点数目为 1 ，各放置 1 个金币。节点 0 处唯一的开销乘积是 2 * 1 * -2 = -4 。所以在节点 0 处放置 0 个金币。
#
#
# 提示：
#
# 2 <= n <= 2 * 104
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ai, bi < n
# cost.length == n
# 1 <= |cost[i]| <= 104
# edges 一定是一棵合法的树。

from leetcode.allcode.competition.mypackage import *

class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        g = defaultdict(list)
        n = len(edges) + 1
        coin = [0] * n
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        def dfs(x, fa):  # 子树的节点数，和正负各三个最大的开销值
            pl, nl = [], []
            if cost[x] > 0:
                pl.append(cost[x])
            else:
                nl.append(cost[x])
            for y in g[x]:
                if y == fa:
                    continue
                po, ne = dfs(y, x)
                pl += po
                nl += ne
                pl.sort(reverse=True)
                nl.sort()
                if len(pl) > 3:
                    pl = pl[:3]
                if len(nl) > 3:
                    nl = nl[:3]

            if len(pl) + len(nl) < 3:
                coin[x] = 1
            elif len(pl) == 0 or (len(pl) == 2 and len(nl) == 1):
                coin[x] = 0
            elif len(pl) == 1:
                coin[x] = pl[0] * nl[0] * nl[1]
            elif len(pl) == 2:
                coin[x] = pl[0] * nl[0] * nl[1]
            else:
                coin[x] = pl[0] * pl[1] * pl[2]
                if len(nl) >= 2:
                    coin[x] = max(coin[x], pl[0] * nl[0] * nl[1])

            return pl, nl
        dfs(0, -1)
        return coin




so = Solution()
print(so.placedCoins([[0,1],[0,2],[2,3]], [10000,-10000,10000,-10000]))
print(so.placedCoins(edges = [[0,1],[0,2],[0,3],[0,4],[0,5]], cost = [1,2,3,4,5,6]))
print(so.placedCoins(edges = [[0,1],[0,2]], cost = [1,2,-2]))
print(so.placedCoins(edges = [[0,1],[0,2],[1,3],[1,4],[1,5],[2,6],[2,7],[2,8]], cost = [1,4,2,3,5,7,8,-4,2]))




