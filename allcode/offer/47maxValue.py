# 在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？
#
#
#
# 示例 1:
#
# 输入:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 12
# 解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
#
#
# 提示：
#
# 0 < grid.length <= 200
# 0 < grid[0].length <= 200


from leetcode.allcode.competition.mypackage import *



class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        dp = [[0] * c for _ in range(r)]
        # dp[0][0] = grid[0][0]
        for i in range(r):
            for j in range(c):
                if i > 0:
                    dp[i][j] = dp[i - 1][j]
                if j > 0:
                    dp[i][j] = max(dp[i][j - 1], dp[i][j])
                dp[i][j] += grid[i][j]
        return dp[-1][-1]



so = Solution()
print(so.maxValue([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))




