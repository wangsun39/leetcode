

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        g = defaultdict(list)
        for x, y, e in edges:
            g[x].append([y, e])
            g[y].append([x, e])
        def dijkstra(g: List[List[Tuple[int]]], start: int) -> List[int]:
            dist = [inf] * n
            dist[start] = 0
            h = [(0, start)]
            while h:
                d, x = heappop(h)
                if d > dist[x]:
                    continue
                for y, wt in g[x]:
                    new_d = dist[x] + wt
                    if new_d < dist[y] and new_d < disappear[y]:
                        dist[y] = new_d
                        heappush(h, (new_d, y))
            dist = [x if x < inf else -1 for x in dist]
            return dist
        return dijkstra(g, 0)



so = Solution()
print(so.minimumTime(7,
[[1,4,3],[3,4,2],[2,5,5],[3,3,10]],
[10,1,13,1,7,1,19]))
print(so.minimumTime(n = 3, edges = [[0,1,2],[1,2,1],[0,2,4]], disappear = [1,1,5]))
print(so.minimumTime(n = 3, edges = [[0,1,2],[1,2,1],[0,2,4]], disappear = [1,3,5]))
print(so.minimumTime(n = 2, edges = [[0,1,1]], disappear = [1,1]))




