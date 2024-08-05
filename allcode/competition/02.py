

from leetcode.allcode.competition.mypackage import *

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        def dijkstra(g: List[List[Tuple[int]]], start: int) -> List[int]:
            dist = [inf] * n  # 注意这个地方可能要替换成 n
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

        g = defaultdict(list)
        for i in range(n - 1):
            g[i].append([i + 1, 1])
        ans = []
        for u, v in queries:
            g[u].append([v, 1])
            dist = dijkstra(g, 0)
            ans.append(dist[n - 1])
        return ans


so = Solution()
print(so.shortestDistanceAfterQueries(n = 5, queries = [[2, 4], [0, 2], [0, 4]]))
print(so.shortestDistanceAfterQueries(n = 4, queries = [[0, 3], [0, 2]]))




