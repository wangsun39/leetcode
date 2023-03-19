# 现有一个加权无向连通图。给你一个正整数 n ，表示图中有 n 个节点，并按从 1 到 n 给节点编号；另给你一个数组 edges ，其中每个 edges[i] = [ui, vi, weighti] 表示存在一条位于节点 ui 和 vi 之间的边，这条边的权重为 weighti 。
#
# 从节点 start 出发到节点 end 的路径是一个形如 [z0, z1, z2, ..., zk] 的节点序列，满足 z0 = start 、zk = end 且在所有符合 0 <= i <= k-1 的节点 zi 和 zi+1 之间存在一条边。
#
# 路径的距离定义为这条路径上所有边的权重总和。用 distanceToLastNode(x) 表示节点 n 和 x 之间路径的最短距离。受限路径 为满足 distanceToLastNode(zi) > distanceToLastNode(zi+1) 的一条路径，其中 0 <= i <= k-1 。
#
# 返回从节点 1 出发到节点 n 的 受限路径数 。由于数字可能很大，请返回对 109 + 7 取余 的结果。
#
#
#
# 示例 1：
#
#
# 输入：n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
# 输出：3
# 解释：每个圆包含黑色的节点编号和蓝色的 distanceToLastNode 值。三条受限路径分别是：
# 1) 1 --> 2 --> 5
# 2) 1 --> 2 --> 3 --> 5
# 3) 1 --> 3 --> 5
# 示例 2：
#
#
# 输入：n = 7, edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]
# 输出：1
# 解释：每个圆包含黑色的节点编号和蓝色的 distanceToLastNode 值。唯一一条受限路径是：1 --> 3 --> 7 。
#
#
# 提示：
#
# 1 <= n <= 2 * 104
# n - 1 <= edges.length <= 4 * 104
# edges[i].length == 3
# 1 <= ui, vi <= n
# ui != vi
# 1 <= weighti <= 105
# 任意两个节点之间至多存在一条边
# 任意两个节点之间至少存在一条路径
from collections import defaultdict, deque
from typing import List, Tuple
from math import *
from heapq import *


class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for x, y, w in edges:
            g[x - 1].append([y - 1, w])
            g[y - 1].append([x - 1, w])

        dist = [inf] * len(g)
        def dijkstra(start: int) -> List[int]:
            dist[start] = 0
            h = [(0, start)]
            while h:
                d, x = heappop(h)
                if d > dist[x]:
                    continue
                for y, wt in g[x]:
                    new_d = dist[x] + wt
                    if new_d < dist[y]:
                        dist[y] = new_d
                        heappush(h, (new_d, y))
            return

        dijkstra(n - 1)
        # print(dist)
        MOD = 10 ** 9 + 7

        tree = defaultdict(set)
        pre_num = [0] * n
        for x, y, _ in edges:
            if dist[x - 1] > dist[y - 1]:
                tree[x - 1].add(y - 1)
                pre_num[y - 1] += 1
            elif dist[y - 1] > dist[x - 1]:
                tree[y - 1].add(x - 1)
                pre_num[x - 1] += 1
        vis = [0] * n  # 从 0 到 i 的受限路径数
        vis[0] = 1  #
        queue = deque([i for i in range(n) if pre_num[i] == 0])  # deque 在操作大数组时，性能比 list 好很多
        # ans = []
        while len(queue):
            q = queue.popleft()
            # ans.append(q)
            for x in tree[q]:
                pre_num[x] -= 1
                vis[x] += vis[q]
                vis[x] %= MOD
                if pre_num[x] == 0:
                    queue.append(x)
        return vis[n - 1]






so = Solution()

print(so.countRestrictedPaths(n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]))  # 3
print(so.countRestrictedPaths(n = 7, edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]))  # 1




