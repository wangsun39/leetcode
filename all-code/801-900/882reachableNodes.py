# 给你一个无向图（原始图），图中有 n 个节点，编号从 0 到 n - 1 。你决定将图中的每条边 细分 为一条节点链，每条边之间的新节点数各不相同。
#
# 图用由边组成的二维数组 edges 表示，其中 edges[i] = [ui, vi, cnti] 表示原始图中节点 ui 和 vi 之间存在一条边，cnti 是将边 细分 后的新节点总数。注意，cnti == 0 表示边不可细分。
#
# 要 细分 边 [ui, vi] ，需要将其替换为 (cnti + 1) 条新边，和 cnti 个新节点。新节点为 x1, x2, ..., xcnti ，新边为 [ui, x1], [x1, x2], [x2, x3], ..., [xcnti+1, xcnti], [xcnti, vi] 。
#
# 现在得到一个 新的细分图 ，请你计算从节点 0 出发，可以到达多少个节点？如果节点间距离是 maxMoves 或更少，则视为 可以到达 。
#
# 给你原始图和 maxMoves ，返回 新的细分图中从节点 0 出发 可到达的节点数 。
#
#
#
# 示例 1：
#
#
# 输入：edges = [[0,1,10],[0,2,1],[1,2,2]], maxMoves = 6, n = 3
# 输出：13
# 解释：边的细分情况如上图所示。
# 可以到达的节点已经用黄色标注出来。
# 示例 2：
#
# 输入：edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], maxMoves = 10, n = 4
# 输出：23
# 示例 3：
#
# 输入：edges = [[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]], maxMoves = 17, n = 5
# 输出：1
# 解释：节点 0 与图的其余部分没有连通，所以只有节点 0 可以到达。
#
#
# 提示：
#
# 0 <= edges.length <= min(n * (n - 1) / 2, 104)
# edges[i].length == 3
# 0 <= ui < vi < n
# 图中 不存在平行边
# 0 <= cnti <= 104
# 0 <= maxMoves <= 109
# 1 <= n <= 3000


from typing import List, Tuple
import math
from collections import defaultdict
from functools import cache
import heapq
from math import *
class Solution:
    def reachableNodes1(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        g = defaultdict(list)   # 图
        e = defaultdict(int)    # 边 [u, v] 上未被覆盖的点
        for u, v, c in edges:
            g[u].append(v)
            g[v].append(u)
            e[(u, v)] = c
            e[(v, u)] = c
        hq = [[-maxMoves - 1, 0]]
        ans = 0
        used = set()   # 走到过的点
        while len(hq):
            s, u = heapq.heappop(hq)
            s = -s
            if u in used:
                continue
            ans += 1
            s -= 1
            used.add(u)
            if s == 0: continue
            for v in g[u]:
                if e[(u, v)] >= s:
                    ans += s
                    # e[(u, v)] -= s
                    e[(v, u)] -= s  # 只需要把返回的路径减掉对应的值就行，因为(u,v)这条路径后面不会再走了
                    continue
                ans += e[(u, v)]
                left = s - e[(u, v)]
                # e[(u, v)] = 0
                e[(v, u)] = 0
                if v in used:
                    continue
                heapq.heappush(hq, [-left, v])
        return ans

    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        # 2023/3/11  Dijkstra 算法
        ans = 0
        adj = defaultdict(list)  # 相邻节点
        dis = {i: inf for i in range(n)}  # 距离 0 的最短距离
        hq = [[0, 0]]  # 记录未计算出dis[i]的点，距离 0 距离的排序堆  [x, y] x: 距离， y: id
        for x, y, z in edges:
            adj[x].append([y, z + 1])
            adj[y].append([x, z + 1])

        while len(hq):
            d, x = heapq.heappop(hq)
            if d > maxMoves: break
            if d >= dis[x]: continue
            dis[x] = d
            ans += 1
            for y, dxy in adj[x]:
                if dis[y] > dis[x] + dxy:
                    # dis[y] = dis[x] + dxy
                    heapq.heappush(hq, [dis[x] + dxy, y])

        print(dis)

        for x, y, z in edges:
            if dis[x] < maxMoves and dis[y] < maxMoves:
                ans += min(maxMoves - dis[x] + maxMoves - dis[y], z)
            elif dis[x] < maxMoves:
                ans += min(maxMoves - dis[x], z)
            elif dis[y] < maxMoves:
                ans += min(maxMoves - dis[y], z)
        return ans



so = Solution()
print(so.reachableNodes(edges = [[0,3,8],[0,1,4],[2,4,3],[1,2,0],[1,3,9],[0,4,7],[3,4,9],[1,4,4],[0,2,7],[2,3,1]], maxMoves = 8, n = 5))  # 40
print(so.reachableNodes(edges = [[0,1,10],[0,2,1],[1,2,2]], maxMoves = 6, n = 3))  # 13
print(so.reachableNodes(edges = [[1,3,23],[3,5,19],[3,6,17],[1,5,14],[6,7,20],[1,4,10],[1,6,0],[3,4,20],[1,7,4],[0,4,10],[0,7,9],[2,3,3],[3,7,9],[5,7,4],[4,5,16],[0,1,16],[2,6,0],[4,7,11],[2,5,14],[5,6,22],[4,6,12],[0,6,2],[0,2,1],[2,4,22],[2,7,20]], maxMoves = 19, n = 8))  # 301
print(so.reachableNodes(edges = [[2,4,2],[3,4,5],[2,3,1],[0,2,1],[0,3,5]], maxMoves = 14, n = 5))  # 18
print(so.reachableNodes(edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], maxMoves = 10, n = 4))  # 23
print(so.reachableNodes(edges = [[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]], maxMoves = 17, n = 5))  # 1


