# 给你一个由 n 个节点（下标从 0 开始）组成的无向加权图，该图由一个描述边的列表组成，其中 edges[i] = [a, b] 表示连接节点 a 和 b 的一条无向边，且该边遍历成功的概率为 succProb[i] 。
#
# 指定两个节点分别作为起点 start 和终点 end ，请你找出从起点到终点成功概率最大的路径，并返回其成功概率。
#
# 如果不存在从 start 到 end 的路径，请 返回 0 。只要答案与标准答案的误差不超过 1e-5 ，就会被视作正确答案。
#
#
#
# 示例 1：
#
#
#
# 输入：n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
# 输出：0.25000
# 解释：从起点到终点有两条路径，其中一条的成功概率为 0.2 ，而另一条为 0.5 * 0.5 = 0.25
# 示例 2：
#
#
#
# 输入：n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
# 输出：0.30000
# 示例 3：
#
#
#
# 输入：n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
# 输出：0.00000
# 解释：节点 0 和 节点 2 之间不存在路径
#
#
# 提示：
#
# 2 <= n <= 10^4
# 0 <= start, end < n
# start != end
# 0 <= a, b < n
# a != b
# 0 <= succProb.length == edges.length <= 2*10^4
# 0 <= succProb[i] <= 1
# 每两个节点之间最多有一条边

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        def dijkstra(g: List[List[Tuple[int]]], start: int) -> List[int]:
            dist = [0] * n   # 注意这个地方可能要替换成 n
            dist[start] = 1
            h = [(-1, start)]
            while h:
                d, x = heappop(h)
                if -d < dist[x]:
                    continue
                for y, wt in g[x]:
                    new_d = dist[x] * wt
                    if new_d > dist[y]:
                        dist[y] = new_d
                        heappush(h, (-new_d, y))
            return dist

        g = defaultdict(list)
        m = len(edges)
        for i in range(m):
            x, y = edges[i]
            w = succProb[i]
            g[x].append([y, w])
            g[y].append([x, w])

        dist = dijkstra(g, start_node)
        return dist[end_node]

so = Solution()
print(so.maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start_node = 0, end_node = 2))
print(so.maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start_node = 0, end_node = 2))




