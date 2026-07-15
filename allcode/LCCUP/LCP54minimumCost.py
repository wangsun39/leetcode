# 欢迎各位勇者来到力扣城，本次试炼主题为「夺回据点」。
#
# 魔物了占领若干据点，这些据点被若干条道路相连接，roads[i] = [x, y] 表示编号 x、y 的两个据点通过一条道路连接。
#
# 现在勇者要将按照以下原则将这些据点逐一夺回：
#
# 在开始的时候，勇者可以花费资源先夺回一些据点，初始夺回第 j 个据点所需消耗的资源数量为 cost[j]
#
# 接下来，勇者在不消耗资源情况下，每次可以夺回一个和「已夺回据点」相连接的魔物据点，并对其进行夺回
#
# 注：为了防止魔物暴动，勇者在每一次夺回据点后（包括花费资源夺回据点后），需要保证剩余的所有魔物据点之间是相连通的（不经过「已夺回据点」）。
#
# 请返回勇者夺回所有据点需要消耗的最少资源数量。
#
# 注意：
#
# 输入保证初始所有据点都是连通的，且不存在重边和自环
# 示例 1：
#
# 输入： cost = [1,2,3,4,5,6] roads = [[0,1],[0,2],[1,3],[2,3],[1,2],[2,4],[2,5]]
#
# 输出：6
#
# 解释： 勇者消耗资源 6 夺回据点 0 和 4，魔物据点 1、2、3、5 相连通； 第一次夺回据点 1，魔物据点 2、3、5 相连通； 第二次夺回据点 3，魔物据点 2、5 相连通； 第三次夺回据点 2，剩余魔物据点 5； 第四次夺回据点 5，无剩余魔物据点； 因此最少需要消耗资源为 6，可占领所有据点。image.png
#
# 示例 2：
#
# 输入： cost = [3,2,1,4] roads = [[0,2],[2,3],[3,1]]
#
# 输出：2
#
# 解释： 勇者消耗资源 2 夺回据点 1，魔物据点 0、2、3 相连通； 第一次夺回据点 3，魔物据点 2、0 相连通； 第二次夺回据点 2，剩余魔物据点 0； 第三次夺回据点 0，无剩余魔物据点； 因此最少需要消耗资源为 2，可占领所有据点。image.png
#
# 提示：
#
# 1 <= roads.length, cost.length <= 10^5
# 0 <= roads[i][0], roads[i][1] < cost.length
# 1 <= cost[i] <= 10^9

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

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

class Solution:
    def minimumCost(self, cost: List[int], roads: List[List[int]]) -> int:
        n = len(cost)
        g = defaultdict(list)
        for x, y in roads:
            g[x].append(y)
            g[y].append(x)
        bcc = BiconnectedComponents(n, g)
        bcc.find_bcc()
        cut = set(bcc.articulation_points)
        s = 0  # 统计边缘连通分量中的非割点最小值之和
        mx = 0  # 统计边缘连通分量的非割点最小值的最大值
        if len(bcc.bccs) == 1:
            return min(cost)
        for b in bcc.bccs:
            mn = inf
            ncut = 0
            for x in b:
                if x in cut:
                    ncut += 1
                    if ncut > 1:
                        break
                else:
                    mn = MIN(mn, cost[x])
            if ncut > 1:  # 非边缘连通分量
                continue
            s += mn
            mx = MAX(mx, mn)

        return s - mx







so = Solution()
print(so.minimumCost(cost = [1,2,3,4,5,6], roads = [[0,1],[0,2],[1,3],[2,3],[1,2],[2,4],[2,5]]))  # 6

