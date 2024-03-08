

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        g = defaultdict(list)
        n = len(edges) + 1
        for x, y, w in edges:
            g[x].append([y, w])
            g[y].append([x, w])

        def calc(start):
            res = 0

            def dfs(x, v, fa):
                res = 0
                if v % signalSpeed == 0:
                    res += 1
                for y, w in g[x]:
                    if y == fa: continue
                    res += dfs(y, v + w, x)
                return res
            part = []
            for y, w in g[start]:
                z = dfs(y, w, start)
                if z:
                    part.append(z)

            s = sum(part)
            for v in part:
                res += (s - v) * v
            return res // 2
        ans = [calc(i) for i in range(n)]
        return ans



so = Solution()
print(so.countPairsOfConnectableServers(edges = [[0,1,1],[1,2,5]], signalSpeed = 1))
print(so.countPairsOfConnectableServers(edges = [[0,1,1],[1,2,5],[2,3,13],[3,4,9],[4,5,2]], signalSpeed = 1))
print(so.countPairsOfConnectableServers(edges = [[0,6,3],[6,5,3],[0,3,1],[3,2,7],[3,1,6],[3,4,2]], signalSpeed = 3))




