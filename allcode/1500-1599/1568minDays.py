# 给你一个大小为 m x n ，由若干 0 和 1 组成的二维网格 grid ，其中 1 表示陆地， 0 表示水。岛屿 由水平方向或竖直方向上相邻的 1 （陆地）连接形成。
#
# 如果 恰好只有一座岛屿 ，则认为陆地是 连通的 ；否则，陆地就是 分离的 。
#
# 一天内，可以将 任何单个 陆地单元（1）更改为水单元（0）。
#
# 返回使陆地分离的最少天数。
#
#
#
# 示例 1：
#
#
# 输入：grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
# 输出：2
# 解释：至少需要 2 天才能得到分离的陆地。
# 将陆地 grid[1][1] 和 grid[0][2] 更改为水，得到两个分离的岛屿。
# 示例 2：
#
#
# 输入：grid = [[1,1]]
# 输出：2
# 解释：如果网格中都是水，也认为是分离的 ([[1,1]] -> [[0,0]])，0 岛屿。
#
#
# 提示：
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 30
# grid[i][j] 为 0 或 1

from leetcode.allcode.competition.mypackage import *

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:


so = Solution()
print(so.minDays())




