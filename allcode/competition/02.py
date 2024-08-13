

from leetcode.allcode.competition.mypackage import *

class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        ans = 0

        def dfs(node, fa):
            nonlocal ans
            cnt = 0  # 子节点数
            sub0 = -1
            judge = True
            for y in g[node]:
                if y == fa: continue
                sub = dfs(y, node)
                if sub0 == -1:
                    sub0 = sub
                elif sub != sub0:
                    judge = False
                cnt += sub  # 子节点数
            if judge:
                ans += 1
            return cnt + 1
        dfs(0, -1)
        return ans


so = Solution()
print(so.countGoodNodes(edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]))
print(so.countGoodNodes(edges = [[0,1],[1,2],[2,3],[3,4],[0,5],[1,6],[2,7],[3,8]]))
print(so.countGoodNodes(edges = [[0,1],[1,2],[1,3],[1,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[9,12],[10,11]]))




