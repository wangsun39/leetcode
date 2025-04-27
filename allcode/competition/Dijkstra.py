
from leetcode.allcode.competition.mypackage import *

# https://leetcode.cn/problems/network-delay-time/solutions/2668220/liang-chong-dijkstra-xie-fa-fu-ti-dan-py-ooe8/

class Solution:

    # Dijkstra 算法模板
    # g[x] = [y, w]
    # 返回从 start 到每个点的最短路
    def dijkstra(g: List[List[Tuple[int]]], start: int, n: int) -> List[int]:
        # dist = [inf] * len(g)   # 注意这个地方可能要替换成 n
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
        return dist

    def dijkstra1(g, start: int) -> List[int]:
        # 路径长度是节点的值，边的值为0
        dist = [inf] * len(g)  # 注意这个地方可能要替换成 n
        dist[start] = start
        h = [(0, start)]
        while h:
            d, x = heappop(h)
            if d > dist[x]:
                continue
            for y in g[x]:
                new_d = dist[x] + y
                if new_d < dist[y]:
                    dist[y] = new_d
                    heappush(h, (new_d, y))
        return dist

so = Solution()




