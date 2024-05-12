

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        ans = -inf
        @cache
        def dfs(row, col):
            nonlocal ans
            if row >= r or col >= c:
                return -inf
            if row == r - 1 and col == c - 1:
                return grid[row][col]
            res1 = dfs(row + 1, col)
            res2 = dfs(row, col + 1)
            res = max(res1, res2)
            ans = max(ans, res - grid[row][col])
            return max(res, grid[row][col])
        dfs(0, 0)
        return ans


so = Solution()
print(so.maxScore(grid = [[4,3,2],[3,2,1]]))
print(so.maxScore(grid = [[9,5,7,3],[8,9,6,1],[6,7,14,3],[2,5,3,1]]))




