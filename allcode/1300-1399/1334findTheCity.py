

from cmath import inf
from collections import defaultdict
from functools import cache
from heapq import *
from typing import List, Tuple


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        g = defaultdict(list)
        for x, y, w in edges:
            g[x].append(tuple([y, w]))
            g[y].append(tuple([x, w]))

        def dijkstra(start: int) -> int:
            dist = [inf] * n
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
            return len([x for x in dist if x <= distanceThreshold]) - 1
        mi = inf
        idx = -1
        for i in range(n):
            cnt = dijkstra(i)
            if cnt <= mi:
                idx = i
                mi = cnt
        return idx


so = Solution()
print(so.findTheCity(6,[[0,3,7],[2,4,1],[0,1,5],[2,3,10],[1,3,6],[1,2,1]],417))
print(so.findTheCity(n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2))
print(so.findTheCity(n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4))



