
from leetcode.allcode.competition.mypackage import *

n = 10
low = [0] * n
dfn = [0] * n
dfs_clock = 0
isbridge = [False] * n
g = defaultdict(list)
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
        if not dfn[v]:  # 未曾计算过，进行DFS
            tarjan(v, u)
            low[u] = min(low[u], low[v])  #
            if low[v] > dfn[u]:
                isbridge[v] = True
                cnt_bridge += 1
        elif dfn[v] < dfn[u] and v != fa:  # v 是 u 的子节点，同时 v 是曾经访问过的点
            low[u] = min(low[u], dfn[v])

# 当 isbridge[x] 为真时，(father[x],x) 为一条割边
