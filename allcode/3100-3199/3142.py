

from leetcode.allcode.competition.mypackage import *

class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        r, c = len(grid), len(grid[0])
        for i in range(r):
            for j in range(c):
                if i < r - 1 and grid[i][j] != grid[i + 1][j]:
                    return False
                if j < c - 1 and grid[i][j] == grid[i][j + 1]:
                    return False
        return True


so = Solution()
print(so.satisfiesConditions(grid = [[1,0,2],[1,0,2]]))
print(so.satisfiesConditions(grid = [[1,1,1],[0,0,0]]))
print(so.satisfiesConditions(grid = [[1],[2],[3]]))




