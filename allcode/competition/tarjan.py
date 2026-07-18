
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


# 点双连通分量模板
class BiconnectedComponents:
    def __init__(self, n, graph):
        self.n = n
        self.graph = graph
        self.dfn = [0] * n
        self.low = [0] * n
        self.time = 0
        self.stack = []
        self.bccs = []  # 所有点双连通分量
        self.articulation_points = set()  # 所有割点

    def find_bcc(self):
        for i in range(self.n):
            if self.dfn[i] == 0:
                self._tarjan(i, i)

    def _tarjan(self, u, fa):
        self.time += 1
        self.dfn[u] = self.low[u] = self.time
        self.stack.append(u)

        child_count = 0
        for v in self.graph[u]:
            if v == fa and fa != u:
                continue

            if self.dfn[v] == 0:
                child_count += 1
                self._tarjan(v, u)
                self.low[u] = min(self.low[u], self.low[v])

                if self.low[v] >= self.dfn[u]:
                    # 记录割点
                    if fa != u or child_count > 1:
                        self.articulation_points.add(u)

                    # 弹栈，形成一个点双连通分量
                    bcc = []
                    while True:
                        top = self.stack.pop()
                        bcc.append(top)
                        if top == v:
                            break
                    bcc.append(u)
                    self.bccs.append(bcc)
            else:
                self.low[u] = min(self.low[u], self.dfn[v])

        # 处理孤立点
        if fa == u and child_count == 0:
            self.stack.pop()
            self.bccs.append([u])
