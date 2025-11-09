

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        r, c = len(grid), len(grid[0])
        k = min(k, r + c)
        dp = [[[-1] * (k + 1) for _ in range(r)] for _ in range(c)]  # 到达[i,j],花费kk的最大收益为 dp[i][j][kk]
        dp2 = [[0 for _ in range(r)] for _ in range(c)]   # 是否能到达[i,j]
        dp[0][0][0] = 0
        dp2[0][0] = 1
        for i in range(r):
            for j in range(c):
                cost = int(grid[i][j] == 0)
                flg = 0
                if (i == 0 or dp2[i - 1][j] == 0) and (j == 0 or dp2[i][j - 1] == 0): continue  # 小优化
                for kk in range(k + 1):
                    cc = kk + cost
                    if cc > k: break
                    if i and dp[i - 1][j][kk] != -1:
                        dp[i][j][cc] = MAX(dp[i][j][cc], dp[i - 1][j][kk] + grid[i][j])
                        flg = 1
                    if j and dp[i][j - 1][kk] != -1:
                        dp[i][j][cc] = MAX(dp[i][j][cc], dp[i][j - 1][kk] + grid[i][j])
                        flg = 1
                dp2[i][j] = flg
        ans = max(dp[-1][-1])
        return ans



so = Solution()
print(so.maxPathScore(grid = [[0, 1],[2, 0]], k = 1))




