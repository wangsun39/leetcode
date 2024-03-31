# 力扣数据中心有 n 台服务器，分别按从 0 到 n-1 的方式进行了编号。它们之间以 服务器到服务器 的形式相互连接组成了一个内部集群，连接是无向的。用  connections 表示集群网络，connections[i] = [a, b] 表示服务器 a 和 b 之间形成连接。任何服务器都可以直接或者间接地通过网络到达任何其他服务器。
#
# 关键连接 是在该集群中的重要连接，假如我们将它移除，便会导致某些服务器无法访问其他服务器。
#
# 请你以任意顺序返回该集群内的所有 关键连接 。
#
#
#
# 示例 1：
#
#
#
# 输入：n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# 输出：[[1,3]]
# 解释：[[3,1]] 也是正确的。
# 示例 2:
#
# 输入：n = 2, connections = [[0,1]]
# 输出：[[0,1]]
#
#
# 提示：
#
# 2 <= n <= 105
# n - 1 <= connections.length <= 105
# 0 <= ai, bi <= n - 1
# ai != bi
# 不存在重复的连接

from leetcode.allcode.competition.mypackage import *

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        low = [0] * n
        dfn = [0] * n
        dfs_clock = 0
        isbridge = [False] * n
        g = defaultdict(list)
        for x, y in connections:
            g[x].append(y)
            g[y].append(x)
        cnt_bridge = 0
        dfs_clock = 0
        father = [0] * n

        # 割边
        def tarjan(u, fa):
            nonlocal dfs_clock, cnt_bridge
            father[u] = fa
            low[u] = dfn[u] = dfs_clock
            dfs_clock += 1
            for v in g[u]:
                if not dfn[v]:
                    tarjan(v, u)
                    low[u] = min(low[u], low[v])
                    if low[v] > dfn[u]:
                        isbridge[v] = True
                        cnt_bridge += 1
                elif dfn[v] < dfn[u] and v != fa:
                    low[u] = min(low[u], dfn[v])
        tarjan(0, -1)
        return [[x, father[x]] for x in range(n) if isbridge[x]]


so = Solution()
print(so.criticalConnections(n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]))
print(so.criticalConnections(n = 2, connections = [[0,1]]))




