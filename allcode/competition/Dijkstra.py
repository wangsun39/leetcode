
from leetcode.allcode.competition.mypackage import *


class Solution:

    # Dijkstra 算法模板
    # g[x] = [y, w]
    # 返回从 start 到每个点的最短路
    def dijkstra(g: List[List[Tuple[int]]], start: int) -> List[int]:
        dist = [inf] * len(g)
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
        return dist

so = Solution()




