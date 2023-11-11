

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        g = defaultdict(list)
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        @cache
        def dfs(x, fa, t):
            r1 = coins[x] // int(2 ** t) - k
            for y in g[x]:
                if y != fa:
                    r1 += dfs(y, x, t)
            r2 = r1
            if t < 16:
                t += 1
                r2 = coins[x] // int(2 ** t)
                for y in g[x]:
                    if y != fa:
                        r2 += dfs(y, x, t)
            return max(r1, r2)
        return dfs(0, -1, 0)



so = Solution()
print(so.maximumPoints([[0,1],[2,1]],[1,6,4],4))
print(so.maximumPoints(edges = [[0,1],[1,2]], coins = [10,10,3], k = 5))
print(so.maximumPoints(edges = [[0,1],[1,2],[2,3]], coins = [10,10,3,3], k = 5))
print(so.maximumPoints(edges = [[0,1],[0,2]], coins = [8,4,4], k = 0))




