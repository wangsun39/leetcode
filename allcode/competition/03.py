

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:

        @cache
        def dfs(r1, r2, c1, c2):
            # print(r1, r2, c1, c2)
            if r2 - r1 <= 1 and c2 - c1 <= 1:
                return 0
            res = inf
            for i in range(r2 - r1 - 1):
                x = dfs(r1, r1 + 1 + i, c1, c2) + dfs(r1 + 1 + i, r2, c1, c2) + horizontalCut[r1 + i]
                res = min(res, x)
            for i in range(c2 - c1 - 1):
                x = dfs(r1, r2, c1, c1 + 1 + i) + dfs(r1, r2, c1 + 1 + i, c2) + verticalCut[c1 + i]
                res = min(res, x)
            return res

        return dfs(0, m, 0, n)



so = Solution()
print(so.minimumCost(m = 3, n = 2, horizontalCut = [1,3], verticalCut = [5]))
print(so.minimumCost(m = 2, n = 2, horizontalCut = [7], verticalCut = [4]))




