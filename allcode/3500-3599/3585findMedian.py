

from leetcode.allcode.competition.mypackage import *


class Solution:
    def findMedian(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        order = n.bit_length() + 1
        p = [[-1] * order for _ in range(n)]  # 记录每个节点的2 ^ i的祖
        dep = [-1] * n
        dis = [-1] * n
        g = defaultdict(list)
        for x, y, w in edges:
            g[x].append([y, w])
            g[y].append([x, w])


        def dfs(node, fa, lv, d):
            dep[node] = lv
            dis[node] = d
            for y, w in g[node]:
                if y == fa: continue
                p[y][0] = node
                dfs(y, node, lv + 1, d + w)

        dfs(0, -1, 0, 0)

        for j in range(order):
            for i in range(n):
                if p[i][j - 1] == -1: continue
                p[i][j] = p[p[i][j - 1]][j - 1]

        @cache
        def lca(x, y):
            if dep[x] > dep[y]:
                x, y = y, x
            for i in range(dep[y] - dep[x]):
                y = p[y][0]
            # x, y 在同一层
            if x == y: return x
            for i in range(order - 1, -1, -1):
                if p[x][i] == p[y][i]:
                    continue
                x, y = p[x][i], p[y][i]
            return p[x][0]

        @cache
        def find(x, u):
            # 返回x的第u个祖先
            res = x
            for i in range(order):
                if u & (1 << i):
                    res = p[res][i]
            return res

        ans = []
        for x, y in queries:
            z = lca(x, y)
            wx = dis[x] - dis[z]
            wy = dis[y] - dis[z]
            wt = wx + wy
            if wx >= wy:
                # 在 x 侧找
                target = (wt + 1) // 2
                lo, hi = 0, dep[x] - dep[z]
                while lo + 1 < hi:
                    mid = (lo + hi) // 2  # 第 mid 级祖先
                    midx = find(x, mid)  # 祖先的节点值
                    if dis[x] - dis[midx] >= target:
                        hi = mid
                    else:
                        lo = mid
                ans.append(find(x, hi))
            else:
                target = wt // 2
                lo, hi = 0, dep[y] - dep[z]
                while lo + 1 < hi:
                    mid = (lo + hi) // 2
                    midy = find(y, mid)
                    if dis[y] - dis[midy] <= target:
                        lo = mid
                    else:
                        hi = mid
                ans.append(find(y, lo))
        return ans


so = Solution()
print(so.findMedian(n = 4, edges = [[0,1,15],[1,2,7],[0,3,16]], queries = [[2,0],[3,1]]))
print(so.findMedian(n = 2, edges = [[0,1,7]], queries = [[1,0],[0,1]]))




