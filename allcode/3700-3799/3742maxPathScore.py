# 给你一个 m x n 的网格 grid，其中每个单元格包含以下值之一：0、1 或 2。另给你一个整数 k。
#
# 你从左上角 (0, 0) 出发，目标是到达右下角 (m - 1, n - 1)，只能向 右 或 下 移动。
#
# 每个单元格根据其值对路径有以下贡献：
#
# 值为 0 的单元格：分数增加 0，花费 0。
# 值为 1 的单元格：分数增加 1，花费 1。
# 值为 2 的单元格：分数增加 2，花费 1。
# 返回在总花费不超过 k 的情况下可以获得的 最大分数 ，如果不存在有效路径，则返回 -1。
#
# 注意： 如果到达最后一个单元格时总花费超过 k，则该路径无效。
#
#
#
# 示例 1：
#
# 输入： grid = [[0, 1],[2, 0]], k = 1
#
# 输出： 2
#
# 解释：
#
# 最佳路径为：
#
# 单元格	grid[i][j]	当前分数	累计分数	当前花费	累计花费
# (0, 0)	0	0	0	0	0
# (1, 0)	2	2	2	1	1
# (1, 1)	0	0	2	0	1
# 因此，可获得的最大分数为 2。
#
# 示例 2：
#
# 输入： grid = [[0, 1],[1, 2]], k = 1
#
# 输出： -1
#
# 解释：
#
# 不存在在总花费不超过 k 的情况下到达单元格 (1, 1) 的路径，因此答案是 -1。
#
#
#
# 提示：
#
# 1 <= m, n <= 200
# 0 <= k <= 103
# grid[0][0] == 0
# 0 <= grid[i][j] <= 2

from leetcode.allcode.competition.mypackage import *

MIN = lambda a, b: b if b < a else a
MAX = lambda a, b: b if b > a else a

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        r, c = len(grid), len(grid[0])
        k = min(k, r + c)
        dp = [[[-1] * (k + 1) for _ in range(c)] for _ in range(r)]  # 到达[i,j],花费kk的最大收益为 dp[i][j][kk]
        dp2 = [[0 for _ in range(c)] for _ in range(r)]   # 是否能到达[i,j]
        dp[0][0][0] = 0
        dp2[0][0] = 1
        for i in range(r):
            for j in range(c):
                cost = int(grid[i][j] != 0)
                flg = 0
                if (i == 0 or dp2[i - 1][j] == 0) and (j == 0 or dp2[i][j - 1] == 0): continue  # 小优化
                for kk in range(k + 1):
                    cc = kk + cost
                    if cc > k:
                        break
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
print(so.maxPathScore(grid = [[0, 1, 1, 1],[1, 2, 2, 0],[1, 0, 1, 2]], k = 4))  #
print(so.maxPathScore(grid = [[0, 1],[1, 2]], k = 1))  # -1
print(so.maxPathScore(grid = [[0, 1],[2, 0]], k = 1))




