

from leetcode.allcode.competition.mypackage import *

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])

        mask = 0
        ans = 0

        # @cache
        def dfs(i, val):  # 从第i行开始，之前选过的数值掩码
            nonlocal mask, ans
            if i == r:
                if val > ans:
                    ans = val
                return
            dfs(i + 1, val)
            for j in range(c):
                if (1 << grid[i][j]) & mask == 0:
                    mask |= (1 << grid[i][j])
                    dfs(i + 1, val + grid[i][j])
                    mask ^= (1 << grid[i][j])
            return

        dfs(0, 0)
        return ans


so = Solution()
print(so.maxScore(grid = [[1,5,20,18],[19,6,17,3],[12,10,6,3],[1,20,12,15]]))  # 69
print(so.maxScore(grid = [[5,5],[5,5],[11,5]]))  # 16
print(so.maxScore(grid = [[1,2,3],[4,3,2],[1,1,1]]))
print(so.maxScore(grid = [[8,7,6],[8,3,2]]))




