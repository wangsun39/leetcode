

from leetcode.allcode.competition.mypackage import *

class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        guesses = set(tuple(x) for x in guesses)
        g = defaultdict(list)
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        n = len(edges) + 1
        fa = [-1] * n

        def dfs(node, p):
            for x in g[node]:
                if x == p: continue
                fa[x] = node
                dfs(x, node)
        dfs(0, -1)

        nc = 0  # 当前正确的guess个数
        for u, v in guesses:
            if u == fa[v]:
                nc += 1
        ans = (nc >= k)

        def chg(node, p, mc):  # 相邻两个点进行换根，从 p 换成 node，mc 表示p为根时，猜对的次数
            nonlocal ans
            if ((node, p) not in guesses and (p, node) not in guesses) or ((node, p) in guesses and (p, node) in guesses):
                pass
            elif (node, p) in guesses:
                mc += 1
            else:
                mc -= 1
            ans += (mc >= k)
            for x in g[node]:
                if x != p:
                    fa[p] = node
                    fa[node] = -1
                    chg(x, node, mc)
                    fa[p] = -1
                    fa[node] = p
        for x in g[0]:
            chg(x, 0, nc)
        return ans




so = Solution()
print(so.rootCount(edges = [[0,1],[1,2],[1,3],[4,2]], guesses = [[1,3],[0,1],[1,0],[2,4]], k = 3))
print(so.rootCount(edges = [[0,1],[1,2],[2,3],[3,4]], guesses = [[1,0],[3,4],[2,1],[3,2]], k = 1))




