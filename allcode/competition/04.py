

from leetcode.allcode.competition.mypackage import *

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        product = 1
        r, c = len(grid), len(grid[0])
        for i in range(r):
            for j in range(c):
                product *= grid[i][j]
                product %= MOD
        ans = [[0] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if grid[i][j] % MOD:
                    x = product // (grid[i][j] % MOD)
                else:
                    x = product
                ans[i][j] = x

        # nums = []
        # for x in grid:
        #     nums += x
        # n = len(nums)
        #
        # @cache
        # def dfs(i, j):
        #     if i > j:
        #         return 1
        #     if i == j:
        #         return nums[i] % MOD
        #     mid = (i + j) // 2
        #     return (dfs(i, mid) * dfs(mid + 1, j)) % MOD
        #
        # res = [0] * (r * c)
        # for i in range(r * c):
        #     res[i] = dfs(0, i - 1) * dfs(i + 1, n - 1)
        # ans = [[0] * c for _ in range(r)]
        # for i in range(r):
        #     for j in range(c):
        #         ans[i][j] = res[i * c + j]
        return ans


so = Solution()
print(so.constructProductMatrix(grid = [[12345],[2],[1]]))
print(so.constructProductMatrix(grid = [[3,2,5],[6,4,3],[6,3,1]]))
print(so.constructProductMatrix(grid = [[1,2],[3,4]]))




