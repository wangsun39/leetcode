# 给你一个有 n 个节点的 有向 加权图，节点编号从 0 到 n - 1。
#
# 该图由一个二维整数数组 edges 表示，其中 edges[i] = [ui, vi, ti] 表示一条从节点 ui 到节点 vi 的有向边，通过该边需要花费 ti 秒。
#
# 同时给你一个整数 power 表示初始可用电量，以及一个长度为 n 的整数数组 cost，其中 cost[u] 表示从节点 u 通过 任意 一条 出 边转发信号所需的电量。
#
# 给你两个整数 source 和 target。
#
# 信号在时间 0 从 source 出发，拥有 power 单位的电量，并遵循以下规则：
#
# 只有当剩余电量 至少 为 cost[u] 时，信号才能遍历从节点 u 出发的有向边。
# 信号到达一个节点时不消耗任何电量，除非它稍后通过另一条边离开该节点。
# 当信号从节点 u 转发时，剩余电量将 减少 cost[u] 个单位。
# 遍历一条边 edges[i] = [ui, vi, ti] 会使总时间 增加 ti 秒。
# 返回一个大小为 2 的整数数组 answer，其中：
#
# answer[0] 是信号到达节点 target 所需的 最小 时间。
# answer[1] 是所有实现 answer[0] 的路径中 最大 的剩余电量。
# 如果信号无法到达 target，则返回 [-1, -1]。
#
#
#
# 示例 1：
#
#
#
# 输入： n = 5, edges = [[0,1,1],[1,4,1],[0,2,1],[2,3,1],[3,4,1]], power = 4, cost = [2,3,1,1,1], source = 0, target = 4
#
# 输出： [3,0]
#
# 解释：
#
# 信号从节点 0 出发，拥有 4 个单位的电量。
# 路径 0 -> 1 -> 4 无效，因为离开节点 0 后，信号剩余 2 个单位的电量，这小于 cost[1] = 3。
# 有效路径 0 -> 2 -> 3 -> 4 总共花费时间为 3。
# 沿着这条路径消耗的总电量为 cost[0] + cost[2] + cost[3] = 4，剩余电量为 0。
# 因此，答案为 [3, 0]。
# 示例 2：
#
#
#
# 输入： n = 3, edges = [[0,1,2],[1,2,2],[2,0,2]], power = 3, cost = [1,1,1], source = 1, target = 1
#
# 输出： [0,3]
#
# 解释：
#
# 由于 source 和 target 是同一个节点，不需要通过任何节点。
# 因此，花费的最小总时间为 0，并且不消耗电量。
# 因此，答案为 [0, 3]。
# 示例 3：
#
#
#
# 输入： n = 4, edges = [[0,1,3],[2,3,4]], power = 3, cost = [1,1,1,1], source = 0, target = 3
#
# 输出： [-1,-1]
#
# 解释：
#
# 没有从 source 到 target 的有效路径，因此返回 [-1, -1]。
#
#
#
# 提示：
#
# 1 <= n <= 1000
# 0 <= edges.length <= 1000
# edges[i] = [ui, vi, ti]
# 0 <= ui, vi <= n - 1
# 1 <= ti <= 109
# 1 <= power <= 1000
# cost.length == n
# 1 <= cost[i] <= 2000
# 0 <= source, target <= n - 1

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minTimeMaxPower(self, n: int, edges: List[List[int]], power: int, cost: List[int], source: int, target: int) -> List[int]:

        def dijkstra(g: List[List[Tuple[int]]], start: int, n: int) -> List[List[int]]:
            # dist = [inf] * len(g)   # 注意这个地方可能要替换成 n
            dist = [[inf] * (power + 1) for _ in range(n)]  # 到达 i 时，剩余电量为j的的最短路径为 dist[i][j]
            dist[start][power] = 0
            h = [(0, start, power)]  # 最短路长度，到达的点，剩余电量
            while h:
                d, x, left = heappop(h)
                if d > dist[x][left] or left < cost[x]:
                    continue
                for y, wt in g[x]:
                    new_d = d + wt
                    if new_d < dist[y][left - cost[x]]:
                        dist[y][left - cost[x]] = new_d
                        heappush(h, (new_d, y, left - cost[x]))
            return dist

        g = defaultdict(list)
        for x, y, t in edges:
            g[x].append([y, t])

        dist = dijkstra(g, source, n)
        mn, left = inf, -1
        for i in range(power, -1, -1):
            if dist[target][i] < mn:
                mn, left = dist[target][i], i
        if mn == inf:
            return [-1, -1]
        return [mn, left]




so = Solution()
print(so.minTimeMaxPower(n = 5, edges = [[0,1,1],[1,4,1],[0,2,1],[2,3,1],[3,4,1]], power = 4, cost = [2,3,1,1,1], source = 0, target = 4))




