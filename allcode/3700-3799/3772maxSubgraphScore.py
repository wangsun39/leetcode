

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxSubgraphScore(self, n: int, edges: List[List[int]], good: List[int]) -> List[int]:
        g = defaultdict(list)
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        sons = [0] * n  # sons[i] 以i为根的子树中，包含i的连通集中最大的得分
        ans = [0] * n

        def dfs1(x, fa):
            vx = 1 if good[x] == 1 else -1
            res = 0
            for y in g[x]:
                if y == fa: continue
                vys = dfs1(y, x)
                if vys > 0:
                    res += vys
            if res > 0:
                res += vx
            else:
                res = vx
            sons[x] = res
            return res

        def dfs2(x, fa):
            up = 0  # 从 fa 到 x 这条路可能产生的最大得分
            if ans[fa] > 0:
                if sons[x] < 0:
                    up = ans[fa]
                elif sons[x] < ans[fa]:
                    up = ans[fa] - sons[x]
                else:
                    up = 0

            ans[x] = sons[x] + up
            for y in g[x]:
                if y == fa: continue
                dfs2(y, x)

        dfs1(0, -1)
        ans[0] = sons[0]
        for x in g[0]:
            dfs2(x, 0)
        return ans


so = Solution()
print(so.maxSubgraphScore(n = 5, edges = [[1,0],[1,2],[1,3],[3,4]], good = [0,1,0,1,1]))
print(so.maxSubgraphScore(n = 3, edges = [[0,1],[1,2]], good = [1,0,1]))




