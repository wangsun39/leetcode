
from leetcode.allcode.competition.mypackage import *


class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        g = defaultdict(list)
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        counter = [0] * n


        def find(u, v):
            def f(u0, p):
                for v0 in g[u0]:
                    if p == v0: continue
                    if v0 == v:
                        return [True, [u0, v]]
                    r1, r2 = f(v0, u0)
                    if r1:
                        return [True, [u0] + r2]
                return [False, []]
            if u == v:
                counter[u] += 1
                return
            l1, l2 = f(u, -1)
            # print(l1, l2)
            for x in l2:
                counter[x] += 1

        for t1, t2 in trips:
            find(t1, t2)

        print(g)
        # print(counter)
        ans = inf
        @cache
        def dfs(x, p, half):
            self_val = counter[x] * price[x]
            cur = 0
            for y in g[x]:
                if y == p: continue
                cur += dfs(y, x, True)
            res = self_val + cur
            if half:
                cur = 0
                self_val //= 2
                for y in g[x]:
                    if y == p: continue
                    cur += dfs(y, x, False)
                if res > cur + self_val:
                    res = cur + self_val
            return res

        for i in range(n):
            if counter[i] == 0: continue
            res = dfs(i, -1, True)
            if res < ans:
                ans = res

        return ans






so = Solution()
print(so.minimumTotalPrice(6,[[0,3],[3,2],[2,1],[1,4],[4,5]],[8,22,8,32,18,26],[[2,3],[1,4],[2,1],[3,1]]))
print(so.minimumTotalPrice(49,
[[1,22],[4,39],[5,34],[7,12],[8,17],[12,30],[17,26],[18,16],[19,16],[21,45],[22,43],[25,16],[16,44],[26,15],[30,2],[32,20],[20,43],[34,33],[33,44],[36,6],[37,28],[28,13],[13,11],[11,43],[40,35],[35,29],[29,15],[15,0],[0,42],[41,46],[42,2],[43,9],[9,44],[44,27],[27,24],[24,23],[46,38],[47,23],[23,39],[39,6],[6,3],[3,38],[38,31],[31,45],[45,10],[10,14],[14,2],[2,48]],
[100,86,28,4,42,76,62,4,50,84,38,84,38,26,92,52,88,14,26,36,90,14,68,30,62,78,64,90,68,44,40,84,12,34,42,36,84,2,48,76,88,22,20,30,66,52,4,100,74],
[[16,17],[42,41],[9,39],[0,15],[29,21],[15,2],[21,13],[23,32],[43,37],[25,33],[46,10],[20,42],[46,40],[36,19],[28,44],[45,7],[19,15],[48,6],[34,0],[27,26],[33,46],[12,1],[35,37],[27,19],[16,41],[48,31],[32,15],[32,30],[39,31],[21,35],[1,26],[14,20],[19,40],[40,7],[31,10],[41,48],[17,43],[47,39],[40,37],[12,6],[3,30],[14,25],[12,16],[9,27],[4,19],[9,13],[38,16],[7,18],[27,22],[19,16],[7,22],[10,10],[41,39],[33,10],[39,40],[48,24],[6,18],[35,5],[18,48],[30,8],[48,18],[9,3]]))
print(so.minimumTotalPrice(n = 4, edges = [[0,1],[1,2],[1,3]], price = [2,2,10,6], trips = [[0,3],[2,1],[2,3]]))
print(so.minimumTotalPrice(n = 2, edges = [[0,1]], price = [2,2], trips = [[0,0]]))
print(so.minimumTotalPrice(9,
[[2,5],[3,4],[4,1],[1,7],[6,7],[7,0],[0,5],[5,8]],
[4,4,6,4,2,4,2,14,8],
[[1,5],[2,7],[4,3],[1,8],[2,8],[4,3],[1,5],[1,4],[2,1],[6,0],[0,7],[8,6],[4,0],[7,5],[7,5],[6,0],[5,1],[1,1],[7,5],[1,7],[8,7],[2,3],[4,1],[3,5],[2,5],[3,7],[0,1],[5,8],[5,3],[5,2]]))





