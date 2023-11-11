

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        d = defaultdict(list)
        for x, y in edges:
            d[x].append(y)
            d[y].append(x)
        n = len(edges) + 1
        s = [0] * n  #  子树values和

        def dfsS(x, fa):
            res = 0
            for y in d[x]:
                if y == fa: continue
                res += values[y] + dfsS(y, x)
            s[x] = res
            return res
        dfsS(0, -1)

        def dfs(x, fa):
            if x != 0 and len(d[x]) == 1:  # 叶子节点
                return 0
            r1 = s[x]  # 保留 x，则x的子树都能选
            # 剩余就是选x
            res = 0
            for y in d[x]:
                if y == fa: continue
                res += dfs(y, x)
            r2 = values[x] + res
            # print(x, max(r1, r2))
            return max(r1, r2)
        return dfs(0, -1)



so = Solution()
print(so.maximumScoreAfterOperations(edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], values = [20,10,9,7,4,3,5]))
print(so.maximumScoreAfterOperations(edges = [[0,1],[0,2],[0,3],[2,4],[4,5]], values = [5,2,5,2,1,1]))




